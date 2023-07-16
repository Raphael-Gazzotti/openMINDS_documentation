import json
import os.path
import re
from typing import List, Optional, Dict

from rstcloth import RstCloth


class InstancesLibraryBuilder(object):

    def __init__(self):
        self.instances_libraries = {
            "terminologies": {},
            "contentTypes": {},
            "licenses": {},
            "brainAtlases": {},
            "commonCoordinateSpaces": {},
            "_common": {}
        }
    def load_instance(self, instance_file_path:str, root_path:str):
        _relative_path_without_extension = instance_file_path[len(root_path)+1:].replace(".jsonld", "").split("/")
        self.relative_path_without_extension = "/".join(_relative_path_without_extension[1:])
        self.instance_basename = os.path.basename(self.relative_path_without_extension)
        with open(instance_file_path, "r") as instance_f:
            self._instance_payload = json.load(instance_f)

    def _add_instance_to_terminologies_libraries(self):
        terminology_name = self.relative_path_without_extension.split("/")[1]
        if terminology_name in self.instances_libraries["terminologies"]:
            self.instances_libraries["terminologies"][terminology_name][self.instance_basename] = self._instance_payload
        else:
            self.instances_libraries["terminologies"][terminology_name] = {
                self.instance_basename: self._instance_payload
            }

    def _add_instance_to_content_types_library(self):
        self.instances_libraries["contentTypes"][self.instance_basename] = self._instance_payload

    def _add_instance_to_licenses_library(self):
        self.instances_libraries["licenses"][self.instance_basename] = self._instance_payload

    def _add_instance_to_common(self):
        common_type = self.relative_path_without_extension.split("/")[2]
        if common_type in self.instances_libraries["_common"]:
            self.instances_libraries["_common"][common_type][self.instance_basename] = self._instance_payload

    def _add_instance_to_brainAtlases_libraries(self):
        ba_name = self.relative_path_without_extension.split("/")[2]
        if ba_name not in self.instances_libraries["brainAtlases"]:
            self.instances_libraries["brainAtlases"][ba_name] = {
                "atlas": None,
                "parcellation_entities": {},
                "versions": {}
            }
        if ba_name == self.instance_basename:
            self.instances_libraries["brainAtlases"][ba_name]["atlas"] = self._instance_payload
        else:
            if f"/parcellationEntities/{ba_name}" in self.relative_path_without_extension:
                pe_name = self.instance_basename
                self.instances_libraries["brainAtlases"][ba_name]["parcellation_entities"][pe_name] = self._instance_payload
            if f"/versions/{ba_name}" in self.relative_path_without_extension:
                bav_name = self.relative_path_without_extension.split("/")[4]
                bav_id = bav_name.split("_")[-1]
                if bav_name not in self.instances_libraries["brainAtlases"][ba_name]["versions"]:
                    self.instances_libraries["brainAtlases"][ba_name]["versions"][bav_name] = {
                        "atlas": None,
                        "parcellation_entities": {}
                    }
                if bav_name == self.instance_basename:
                    self.instances_libraries["brainAtlases"][ba_name]["versions"][bav_name]["atlas"] = self._instance_payload
                else:
                    if f"/parcellationEntities_{bav_id}/" in self.relative_path_without_extension:
                        pev_name = self.instance_basename
                        self.instances_libraries["brainAtlases"][ba_name]["versions"][bav_name]["parcellation_entities"][pev_name] = self._instance_payload

    def _add_instance_to_common_coordinate_space_libraries(self):
        ccs_name = self.relative_path_without_extension.split("/")[2]
        if ccs_name not in self.instances_libraries["commonCoordinateSpaces"]:
            self.instances_libraries["commonCoordinateSpaces"][ccs_name] = {
                "space": None,
                "versions": {}
            }
        if ccs_name == self.instance_basename:
            self.instances_libraries["commonCoordinateSpaces"][ccs_name]["space"] = self._instance_payload
        else:
            if f"versions/{ccs_name}" in self.relative_path_without_extension:
                ccsv_name = self.instance_basename
                self.instances_libraries["commonCoordinateSpaces"][ccs_name]["versions"][ccsv_name] = self._instance_payload

    def add_instance_to_library(self):
        if self.relative_path_without_extension.startswith("terminologies"):
            self._add_instance_to_terminologies_libraries()
        if self.relative_path_without_extension.startswith("contentTypes"):
            self._add_instance_to_content_types_library()
        if self.relative_path_without_extension.startswith("licenses"):
            self._add_instance_to_licenses_library()
        if self.relative_path_without_extension.startswith("graphStructures/common"):
            self._add_instance_to_common()
        if self.relative_path_without_extension.startswith("graphStructures/brainAtlases"):
            self._add_instance_to_brainAtlases_libraries()
        if self.relative_path_without_extension.startswith("graphStructures/commonCoordinateSpaces"):
            self._add_instance_to_common_coordinate_space_libraries()

class InstancesDocBuilder(object):

    def __init__(self, instances_version:str, instances_libraries:Dict):
        self.readthedocs_url = "https://openminds-documentation.readthedocs.io/en/"
        self.version = instances_version
        self.instances_libraries = instances_libraries

    def _target_file_without_extension(self, target_basename:str) -> str:
        return os.path.join("target", self.version, "docs", "libraries", f"{target_basename}")

    def _build_single_term_links(self, termReference:Dict, terminology:str) -> str:
        term = termReference["@id"].split("/")[-1]
        name = self.instances_libraries["terminologies"][term]["name"]
        link = os.path.join(self.readthedocs_url, self.version, "libraries", "terminologies", f"{terminology}.html#{name.replace(' ', '-')}")
        return f"`{name} <{link}>`_"

    def _build_multi_term_links(self, termReferenceList:List, terminology:str) -> str:
        linklist = []
        for termReference in termReferenceList:
            linklist.append(self._build_single_term_links(termReference, terminology))
        return ", ".join(linklist)

    def _build_product_version_links(self, versions:Dict, productType:str) -> str:
        linklist = []
        for name, data  in sorted(versions.items()):
            vID = data['versionIdentifier']
            space_html_title = f"{data['shortName'].replace(' ', '%20')}.html#version-{vID.replace(' ', '-')}"
            link = os.path.join(self.readthedocs_url, self.version, "libraries", productType, space_html_title)
            linklist.append(f"`{vID} <{link}>`_")
        return ", ".join(linklist)

    def _build_terminology(self, target_file:str, name:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            name_CamelCase = "".join([name[0].capitalize(), name[1:]])
            doc.heading(f"{name_CamelCase}", char="#", overline=True)
            doc.newline()
            schema_link = os.path.join(self.readthedocs_url, self.version, "specifications", "controlledTerms", f"{name}.html")
            doc.content(f"All instances listed below can be validated against the `{name_CamelCase} <{schema_link}>`_ schema specification.")
            doc.newline()
            doc.content("------------")
            doc.newline()
            doc.content("------------")
            doc.newline()
            for term_name, term_data in sorted(data_to_display.items()):
                doc.heading(term_data["name"], char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                doc.newline()
                field_list_indent = 3
                doc.field(name="semantic name", value=term_data['@id'], indent=field_list_indent)
                definition = term_data["definition"] if "definition" in term_data and term_data["definition"] else "\-"
                doc.field(name="definition", value=definition, indent=field_list_indent)
                description = term_data["description"] if "description" in term_data and term_data["description"] else "\-"
                doc.field(name="description", value=description, indent=field_list_indent)
                synonym = ", ".join(term_data["synonym"]) if "synonym" in term_data and term_data["synonym"] else "\-"
                doc.field(name="synonyms", value=synonym, indent=field_list_indent)
                doc.content("------------", indent=field_list_indent)
                ontologyID = term_data["preferredOntologyIdentifier"] if "preferredOntologyIdentifier" in term_data and term_data["preferredOntologyIdentifier"] else "\-"
                doc.field(name="preferred ontology ID", value=ontologyID, indent=field_list_indent)
                interlexID = term_data["interlexIdentifier"] if "interlexIdentifier" in term_data and term_data["interlexIdentifier"] else "\-"
                doc.field(name="InterLex ID", value=interlexID, indent=field_list_indent)
                ksEntry = term_data["knowledgeSpaceLink"] if "knowledgeSpaceLink" in term_data and term_data["knowledgeSpaceLink"] else "\-"
                doc.field(name="KnowledgeSpace entry", value=ksEntry, indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <{name}_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_content_types(self, target_file:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading("ContentTypes", char="#", overline=True)
            doc.newline()
            for ct_name, ct_data in sorted(data_to_display.items()):
                doc.heading(ct_data["name"], char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                doc.newline()
                field_list_indent = 3
                doc.field(name="semantic name", value=ct_data["@id"], indent=field_list_indent)
                displaylabel = ct_data["displayLabel"] if "displayLabel" in ct_data and ct_data["displayLabel"] else "\-"
                doc.field(name="display label", value=displaylabel, indent=field_list_indent)
                extensions = ", ".join(ct_data["fileExtension"]) if "fileExtension" in ct_data and ct_data["fileExtension"] else "\-"
                doc.field(name="file extensions", value=extensions, indent=field_list_indent)
                synonyms = ", ".join(ct_data["synonym"]) if "synonym" in ct_data and ct_data["synonym"] else "\-"
                doc.field(name="synonyms", value=synonyms, indent=field_list_indent)
                description = ct_data["description"] if "description" in ct_data and ct_data["description"] else "\-"
                doc.field(name="description", value=description, indent=field_list_indent)
                specification = ct_data["specification"] if "specification" in ct_data and ct_data["specification"] else "\-"
                doc.field(name="specification", value=specification, indent=field_list_indent)
                datatypes = self._build_multi_term_links(ct_data["dataType"], "dataType") if "dataType" in ct_data and ct_data["dataType"] else "\-"
                doc.field(name="data types", value=datatypes, indent=field_list_indent)
                mediatype = ct_data["relatedMediaType"] if "relatedMediaType" in ct_data and ct_data["relatedMediaType"] else "\-"
                doc.field(name="related media type", value=mediatype, indent=field_list_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <ContentTypes_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_licenses(self, target_file:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading("Licenses", char="#", overline=True)
            doc.newline()
            for license_name, license_data in sorted(data_to_display.items()):
                doc.heading(license_data["shortName"], char="-")
                doc.newline()
                doc.directive(name="admonition", arg="metadata sheet")
                doc.newline()
                field_list_indent = 3
                doc.field(name="semantic name", value=license_data["@id"], indent=field_list_indent)
                fullName = license_data["fullName"] if "fullName" in license_data and license_data["fullName"] else "\-"
                doc.field(name="full name", value=fullName, indent=field_list_indent)
                legalCode = license_data["legalCode"] if "legalCode" in license_data and license_data["legalCode"] else "\-"
                doc.field(name="legal code", value=legalCode, indent=field_list_indent)
                webpage = license_data["webpage"] if "webpage" in license_data and license_data["webpage"] else "\-"
                field_name = "webpages"
                doc.field(name=field_name, value=webpage[0], indent=field_list_indent)
                if len(webpage) > 1:
                    multiline_indent = len(field_name) + 3 + field_list_indent
                    doc.content(webpage[1], indent=multiline_indent)
                doc.newline()
                doc.content(f"`BACK TO TOP <Licenses_>`_")
                doc.newline()
                doc.content("------------")
                doc.newline()

    def _build_brain_atlas(self, target_file:str, name:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            atlas = data_to_display["atlas"]
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{name}", char="#", overline=True)
            doc.newline()
            doc.directive(name="admonition", arg="metadata sheet")
            doc.newline()
            field_list_indent = 3
            doc.field(name="semantic name", value=atlas["@id"], indent=field_list_indent)
            space_fullName = atlas["fullName"] if "fullName" in atlas and atlas["fullName"] else "\-"
            doc.field(name="full name", value=space_fullName, indent=field_list_indent)
            space_abbr = atlas["abbreviation"] if "abbreviation" in atlas and atlas["abbreviation"] else "\-"
            doc.field(name="abbreviation", value=space_abbr, indent=field_list_indent)
            usedSpecies = self._build_single_term_link(atlas["usedSpecies"], "species") if "usedSpecies" in atlas and atlas["usedSpecies"] else "\-"
            doc.field(name="used species", value=usedSpecies, indent=field_list_indent)
            space_digitalID = atlas["digitalIdentifier"] if "digitalIdentifier" in atlas and atlas["digitalIdentifier"] else "\-"
            doc.field(name="digital ID", value=space_digitalID, indent=field_list_indent)
            space_ontologyID = atlas["ontologyIdentifier"] if "ontologyIdentifier" in atlas and atlas["ontologyIdentifier"] else "\-"
            doc.field(name="ontology ID", value=space_ontologyID, indent=field_list_indent)
            space_homepage = atlas["homepage"] if "homepage" in atlas and atlas["homepage"] else "\-"
            doc.field(name="homepage", value=space_homepage, indent=field_list_indent)
            space_citation = atlas["howToCite"] if "howToCite" in atlas and atlas["howToCite"] else "\-"
            doc.field(name="howToCite", value=space_citation, indent=field_list_indent)

    def _build_common_coordinate_space(self, target_file:str, title:str, data_to_display:Dict):
        with open(f"{target_file}.rst", "w") as output_file:
            data = data_to_display["space"]
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(f"{title}", char="#", overline=True)
            doc.newline()
            doc.directive(name="admonition", arg="metadata sheet")
            doc.newline()
            field_list_indent = 3
            doc.field(name="semantic name", value=data["@id"], indent=field_list_indent)
            d_fullName = data["fullName"] if "fullName" in data and data["fullName"] else "\-"
            doc.field(name="full name", value=d_fullName, indent=field_list_indent)
            d_abbr = data["abbreviation"] if "abbreviation" in data and data["abbreviation"] else "\-"
            doc.field(name="abbreviation", value=d_abbr, indent=field_list_indent)
            d_species = self._build_single_term_link(data["usedSpecies"], "species") if "usedSpecies" in data and data["usedSpecies"] else "\-"
            doc.field(name="used species", value=d_species, indent=field_list_indent)
            d_digitalID = data["digitalIdentifier"] if "digitalIdentifier" in data and data["digitalIdentifier"] else "\-"
            doc.field(name="digital ID", value=d_digitalID, indent=field_list_indent)
            d_ontologyID = data["ontologyIdentifier"] if "ontologyIdentifier" in data and data["ontologyIdentifier"] else "\-"
            doc.field(name="ontology ID", value=d_ontologyID, indent=field_list_indent)
            d_homepage = data["homepage"] if "homepage" in data and data["homepage"] else "\-"
            doc.field(name="homepage", value=d_homepage, indent=field_list_indent)
            d_citation = data["howToCite"] if "howToCite" in data and data["howToCite"] else "\-"
            doc.field(name="howToCite", value=d_citation, indent=field_list_indent)
            if "hasVersion" in data and data["hasVersion"]:
                version_link_list = self._build_product_version_links(data_to_display["versions"], "commonCoordinateSpaces")
                doc.field(name="has versions", value=version_link_list, indent=field_list_indent)
                doc.newline()
                doc.content("------------")
                doc.newline()
                doc.content("------------")
                doc.newline()
                doc.heading(f"Versions", char="#")
                for _, vdata in sorted(data_to_display["versions"].items()):
                    subtitle = vdata['versionIdentifier']
                    doc.heading(f"{subtitle}", char="*", overline=True)
                    doc.newline()
                    doc.directive(name="admonition", arg="metadata sheet")
                    doc.newline()
                    field_list_indent = 3
                    doc.field(name="semantic name", value=vdata["@id"], indent=field_list_indent)
                    doc.newline()
                    dv_fullName = vdata["fullName"] if "fullName" in vdata and vdata["fullName"] else "\-"
                    if dv_fullName != d_fullName:
                        doc.field(name="full name", value=dv_fullName, indent=field_list_indent)
                    dv_abbr = vdata["abbreviation"] if "abbreviation" in vdata and vdata["abbreviation"] else "\-"
                    if dv_abbr != d_abbr:
                        doc.field(name="abbreviation", value=dv_abbr, indent=field_list_indent)
                    dv_digitalID = vdata["digitalIdentifier"] if "digitalIdentifier" in vdata and vdata["digitalIdentifier"] else "\-"
                    doc.field(name="digital ID", value=dv_digitalID, indent=field_list_indent)
                    dv_ontologyID = vdata["ontologyIdentifier"] if "ontologyIdentifier" in vdata and vdata["ontologyIdentifier"] else "\-"
                    doc.field(name="ontology ID", value=dv_ontologyID, indent=field_list_indent)
                    dv_homepage = vdata["homepage"] if "homepage" in vdata and vdata["homepage"] else "\-"
                    if dv_homepage != d_homepage:
                        doc.field(name="homepage", value=dv_homepage, indent=field_list_indent)
                    dv_citation = vdata["howToCite"] if "howToCite" in vdata and vdata["howToCite"] else "\-"
                    doc.field(name="howToCite", value=dv_citation, indent=field_list_indent)
                    doc.content("------------", indent=field_list_indent)
                    dv_access = self._build_single_term_link(vdata["accessibility"], "accessibility") if "accessibility" in vdata and vdata["accessibility"] else "\-"
                    doc.field(name="accessibility", value=dv_access, indent=field_list_indent)
                    doc.newline()
                    doc.content(f"`BACK TO TOP <{title}_>`_")
                    doc.newline()
                    doc.content("------------")
                    doc.newline()
    def build(self):
        # build RST docu for each terminology
        for terminology_name, terms in self.instances_libraries["terminologies"].items():
            target_file = self._target_file_without_extension("/".join(["terminologies", terminology_name]))
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            self._build_terminology(target_file, terminology_name, terms)

        # build RST docu for content types
        target_file = self._target_file_without_extension("contentTypes")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        self._build_content_types(target_file, self.instances_libraries["contentTypes"])

        # build RST docu for licenses
        target_file = self._target_file_without_extension("licenses")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        self._build_licenses(target_file, self.instances_libraries["licenses"])

        # build RST docu for each brain atlas
        for ba_name, ba_data in self.instances_libraries["brainAtlases"].items():
            ba_title = ba_data["atlas"]["shortName"]
            target_file = self._target_file_without_extension("/".join(["brainAtlases", ba_title]))
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            self._build_brain_atlas(target_file, ba_title, ba_data)

        # build RST docu for each common coordinate space
        for ccs_name, ccs_data in self.instances_libraries["commonCoordinateSpaces"].items():
            ccs_title = ccs_data["space"]["shortName"]
            target_file = self._target_file_without_extension("/".join(["commonCoordinateSpaces", ccs_title]))
            os.makedirs(os.path.dirname(target_file), exist_ok=True)
            self._build_common_coordinate_space(target_file, ccs_title, ccs_data)