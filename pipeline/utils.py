import json
import glob
import os
import shutil
from typing import List, Dict, Tuple

from git import Repo, GitCommandError


def copy_static_structures(version:str):
    shutil.copytree("static", f"target/{version}")


def clone_sources():
    # cloning central repo (for schemas)
    if os.path.exists("sources_schemas"):
        shutil.rmtree("sources_schemas")
    Repo.clone_from("https://github.com/openMetadataInitiative/openMINDS.git", to_path="sources_schemas", depth=1)

    # cloning instances repo (for instances)
    if os.path.exists("sources_instances"):
        shutil.rmtree("sources_instances")
    Repo.clone_from("https://github.com/openMetadataInitiative/openMINDS_instances.git", to_path="sources_instances", depth=1)

class SchemaLoader(object):

    def __init__(self):
        self._root_directory = os.path.realpath(".")
        self.schemas_sources = os.path.join(self._root_directory, "sources_schemas", "schemas")

    def get_schema_versions(self) -> List[str]:
        return os.listdir(self.schemas_sources)

    def find_schemas(self, version:str) -> List[str]:
        return glob.glob(os.path.join(self.schemas_sources, version, f'**/*.schema.omi.json'), recursive=True)

    def get_schema_name(self, absolute_path_schema:str, extension=".schema.omi.json") -> str:
        schema_name = os.path.basename(absolute_path_schema).replace(extension, '')
        return f"{schema_name[0].upper()}{schema_name[1:]}"

    def get_relative_paths_for_schema_docu(self, absolute_paths_for_schemas:List[str], version:str) -> Dict:
        relative_paths_for_schema_docu = {}
        for absolute_path_schema in absolute_paths_for_schemas:
            schema_name = self.get_schema_name(absolute_path_schema)
            relative_schema_path = os.path.relpath(absolute_path_schema, start=os.path.join(self.schemas_sources, version)).replace('.schema.omi.json', '')
            relative_paths_for_schema_docu[schema_name] = relative_schema_path
        return relative_paths_for_schema_docu

class InstanceLoader(object):

    def __init__(self):
        self._root_directory = os.path.realpath(".")
        self.instances_sources = os.path.join(self._root_directory, "sources_instances", "instances")

    def get_instance_versions(self) -> List[str]:
        return os.listdir(self.instances_sources)

    def find_instances(self, version:str) -> List[str]:
        return glob.glob(os.path.join(self.instances_sources, version, f'**/*.jsonld'), recursive=True)

    def get_relative_paths_and_schemas_for_instancelib_docu(self, absolute_paths_for_instances:List[str], version:str) -> Tuple[Dict,Dict]:
        relative_paths_for_instancelib_docu = {}
        instancelib_docu_path_for_schemas = {}
        for absolute_path_instance in absolute_paths_for_instances:
            # define relative path of instance library docu (with list to absolute paths of all related instances)
            relative_instance_path = os.path.relpath(absolute_path_instance, start=os.path.join(self.instances_sources, version)).replace('.jsonld', '')
            relative_instancelib_path = "/".join(relative_instance_path.split("/")[:-1])
            if relative_instancelib_path in relative_paths_for_instancelib_docu:
                relative_paths_for_instancelib_docu[relative_instancelib_path].append(absolute_path_instance)
            else:
                relative_paths_for_instancelib_docu[relative_instancelib_path] = [absolute_path_instance]
            # associate relative instance library docu path to schema type
            with open(absolute_path_instance, "r") as instance_f:
                instance_payload = json.load(instance_f)
            instance_schema = instance_payload["@type"].split("/")[-1]
            if instance_schema in ["BrainAtlasVersion", "CommonCoordinateSpaceVersion", "ParcellationEntity", "ParcellationEntityVersion"]:
                instancelib_docu_path_for_schemas[instance_schema] = "/".join(relative_instance_path.split("/")[:-2])
            elif instance_schema == "Technique": #FIXME
                if relative_instance_path.split("/")[-2] == "analysisTechnique":
                    instancelib_docu_path_for_schemas["AnalysisTechnique"] = relative_instancelib_path
                else:
                    instancelib_docu_path_for_schemas[instance_schema] = relative_instancelib_path
            else:
                instancelib_docu_path_for_schemas[instance_schema] = relative_instancelib_path
        return relative_paths_for_instancelib_docu, instancelib_docu_path_for_schemas

    def get_path_for_instances(self, instance_paths:List[str], version:str) -> Dict:
        path_by_instance = {}
        for instance_path in instance_paths:
            instance_filename = os.path.basename(instance_path).replace('.jsonld', '')
            path_by_instance[instance_filename] = instance_path
        return path_by_instance

class GitPusher(object):

    def __init__(self):
        self.upload_dir = "../upload"
        self._repo = Repo(self.upload_dir)

    def upload(self, version):
        print(f"Uploading version {version}")
        self._checkout(version)
        self._clear_directory()
        shutil.copytree(f"target/{version}", self.upload_dir, dirs_exist_ok=True)
        self._repo.git.add('--all')
        diff_list = self._repo.head.commit.diff()
        if diff_list:
            print(f"{len(diff_list)} changes found - pushing to origin")
            self._repo.index.commit(f'Updating documentation for version {version}')
            self._repo.git.push("origin", version)
        else:
            print("No changes - nothing to commit")

    def _clear_directory(self):
        for item in os.listdir(self.upload_dir):
            if os.path.isdir(f"{self.upload_dir}/{item}") and not item.startswith("."):
                shutil.rmtree(f"{self.upload_dir}/{item}")
            elif os.path.isfile(f"{self.upload_dir}/{item}"):
                os.remove(f"{self.upload_dir}/{item}")

    def _checkout(self, version):
        self._repo.git.fetch()
        try:
            self._repo.git.checkout(version)
        except GitCommandError as e:
            self._repo.git.checkout("-b", version)
