import json
import re
import os.path
from typing import List, Optional, Dict

from rstcloth import RstCloth


class SchemaDocBuilder(object):

    def __init__(self, schema_file_path:str, schema_name:str, version:str, relative_paths_for_schema_docu:Dict, instancelib_docu_path_for_schema:Optional[str]):
        # load schema payload
        with open(schema_file_path, "r") as schema_f:
            self._schema_payload = json.load(schema_f)
        # set version, name, and paths
        self.version = version
        self.schema_name = schema_name
        self.schema_relative_path = relative_paths_for_schema_docu[schema_name]
        self.relative_paths_for_schema_docu = relative_paths_for_schema_docu
        self.instancelib_docu_path_for_schema = instancelib_docu_path_for_schema
        self.readthedocs_url = "https://openminds-documentation.readthedocs.io/en/"

    def _generate_template_instance(self, property_namespace, short_namespace):
        return f""".. raw:: html
            
            <script>
            const properties = {json.dumps(self._extract_properties_value())};
            
            function generateTemplate(properties) {{
                const template = {{
                  "@context": {{
                    "@vocab": "{property_namespace}",
                    "inst": "{short_namespace+"/instances/"}"
                  }},
                  "@id": "inst:{self._schema_payload["name"][0].lower() + self._schema_payload["name"][1:]}/null",
                  "@type": "{self._schema_payload["_type"]}",
                }}
                
                // Fulfill the template with required properties
                for (const property in properties) {{
                    if (requiredProperties.hasOwnProperty(property)) {{
                        const prop = properties[property];
                        
                        if (prop.hasOwnProperty('type')) {{
                            if (prop.type === 'string') {{
                                template[property] = null;
                            }} else if (prop.type === 'array') {{
                                if (prop.hasOwnProperty('items') && prop.items.type === 'string') {{
                                    template[property] = [];
                                }} else if (prop.hasOwnProperty('_linkedTypes') && prop._linkedTypes.length === 1) {{
                                    const linkedType = prop._linkedTypes[0].split('/').pop();
                                    const linkedTypeFormatted = linkedType.charAt(0).toLowerCase() + linkedType.slice(1);
                                    template[property] = [{{ "@id": `inst:${{linkedTypeFormatted}}/null` }}];
                                }} else {{
                                    template[property] = [{{ "@id": "inst:null" }}];
                                }}
                            }}
                        }} else {{
                            if (prop.hasOwnProperty('_linkedTypes') && prop._linkedTypes.length === 1) {{
                                const linkedType = prop._linkedTypes[0].split('/').pop();
                                const linkedTypeFormatted = linkedType.charAt(0).toLowerCase() + linkedType.slice(1);
                                template[property] = {{ "@id": `inst:${{linkedTypeFormatted}}/null` }};
                            }} else {{
                                template[property] = {{ "@id": "inst:null" }};
                            }}
                        }}
                    }}
                }}
                
                const formattedTemplate = JSON.stringify(template, null, 2);
    
                // Create a Blob object
                const blob = new Blob([formattedTemplate], {{ type: 'application/ld+json' }});
                
                // Create a temporary URL for the Blob
                const url = URL.createObjectURL(blob);
                
                // Create a hidden anchor element
                const link = document.createElement('a');
                link.href = url;
                link.setAttribute('download', 'instance_template.jsonld');
                document.body.appendChild(link);
                
                // Simulate a click on the link to trigger the download
                link.click();
                
                // Clean up (optional)
                URL.revokeObjectURL(url); 
                document.body.removeChild(link);
            }}
            </script>

            Generate a template instance of the {self._schema_payload["label"]} schema with the following button: <button onclick="generateTemplate(properties)">Instance template</button>
            To help you complete the instance template, we’ve included an example using realistic mock data and guidance:
            """

    def _target_file_without_extension(self) -> str:
        return os.path.join(self.version, "docs", "schema_specifications", self.schema_relative_path)

    def build(self):
        target_file = os.path.join("target", f"{self._target_file_without_extension()}.rst")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        with open(target_file, "w") as output_file:
            doc = RstCloth(output_file, line_width=100000)
            doc.heading(self.schema_name, char="#", overline=True)
            doc.newline()
            doc.field(name="Semantic name", value=self._schema_payload["_type"])
            doc.newline()
            doc.field(name="Display as", value=self._schema_payload["label"])
            doc.newline()
            if "description" in self._schema_payload and self._schema_payload["description"]:
                doc.content(self._schema_payload["description"])
                doc.newline()
            semantic_equivalent = self._extract_semantic_equivalents()
            if semantic_equivalent:
                doc.field(name="Semantic equivalents", value=semantic_equivalent)
                doc.newline()
            doc.newline()
            if self.instancelib_docu_path_for_schema:
                library_link = os.path.join(self.readthedocs_url, self.version, "instance_libraries", self.instancelib_docu_path_for_schema)
                doc.content(f"For this schema openMINDS provides a `library of instances <{library_link}.html>`_.")
                doc.newline()

            property_namespace = None
            short_namespace = None
            if "properties" in self._schema_payload and self._schema_payload["properties"]:
                for p in self._schema_payload["properties"].keys():
                    match = re.match(r'^(https?:\/\/[^\/]+\/[^\/]+\/)', p)
                    property_namespace = match.group(1) if match else None
                    match = re.match(r'^(https?:\/\/[^\/]+)', p)
                    short_namespace = match.group(1) if match else None
                    break

            doc.content("------------")
            doc.newline()
            doc.heading("Build instance template", char="#")
            doc.newline()
            template_instance_content = self._generate_template_instance(property_namespace, short_namespace)
            # Hacky method, RstCloth does not consider the addition of JavaScript code
            doc._add(template_instance_content)
            doc.content("------------")
            doc.newline()
            doc.heading("Properties", char="#")
            doc.newline()
            doc.field(name="Required", value=self._extract_required_properties())
            doc.field(name="Optional", value=self._extract_optional_properties())
            doc.newline()
            doc.content("------------")
            doc.newline()
            if "properties" in self._schema_payload and self._schema_payload["properties"]:
                for p_qname, p_info in sorted(self._schema_payload["properties"].items()):
                    # property subsection title
                    p_name = p_info["name"]
                    doc.content(f".. _{p_name}_heading:")
                    doc.newline()
                    doc.heading(p_name, char="*", overline=True)
                    doc.newline()
                    # property subsection description
                    if "description" in p_info.keys():
                        doc.content(p_info["description"])
                        doc.newline()
                    # property subsection specification box
                    doc.directive(name="admonition", arg="schema_specifications")
                    doc.newline()
                    field_list_indent = 3
                    doc.field(name="semantic name", value=p_qname, indent=field_list_indent)
                    # multiline field list item for value types
                    value_specs = self.extract_value_specs(p_info)
                    field_name = "value type"
                    doc.field(name=field_name, value=value_specs[0], indent=field_list_indent)
                    if len(value_specs) > 1:
                        multiline_indent = len(field_name)+3+field_list_indent
                        doc.content(value_specs[1], indent=multiline_indent)
                    doc.field(name="instructions", value=p_info["_instruction"], indent=field_list_indent)
                    doc.newline()
                    doc.content(f"`BACK TO TOP <{self.schema_name}_>`_")
                    doc.newline()

    def _extract_properties_value(self) -> dict:
        properties = {}
        if "properties" in self._schema_payload and self._schema_payload["properties"]:
            for p in self._schema_payload["properties"].keys():
                p_split = p.split("/")[-1]
                properties[p_split] = self._schema_payload["properties"][p]
        return properties

    def _extract_required_properties_value(self) -> dict:
        required_properties = {}
        if "required" in self._schema_payload and self._schema_payload["required"]:
            for p in self._schema_payload["required"]:
                p_split = p.split("/")[-1]
                if p in self._schema_payload["properties"]:
                    required_properties[p_split] = self._schema_payload["properties"][p]
        return required_properties

    def _extract_optional_properties_value(self) -> dict:
        optional_properties = {}
        if "properties" in self._schema_payload and self._schema_payload["properties"]:
            for p in self._schema_payload["properties"].keys():
                if "required" not in self._schema_payload or not self._schema_payload["required"] or p not in self._schema_payload["required"]:
                    p_split = p.split("/")[-1]
                    optional_properties[p_split] = self._schema_payload["properties"][p]
        return optional_properties

    def _extract_required_properties(self) -> str:
        required_properties = []
        if "required" in self._schema_payload and self._schema_payload["required"]:
            for p in self._schema_payload["required"]:
                p_split = p.split("/")[-1]
                required_properties.append(f"`{p_split} <{p_split}_heading_>`_")
        return ", ".join(required_properties)

    def _extract_optional_properties(self) -> str:
        optional_properties = []
        if "properties" in self._schema_payload and self._schema_payload["properties"]:
            for p in self._schema_payload["properties"].keys():
                if "required" not in self._schema_payload or not self._schema_payload["required"] or p not in self._schema_payload["required"]:
                    p_split = p.split("/")[-1]
                    optional_properties.append(f"`{p_split} <{p_split}_heading_>`_")
        return ", ".join(optional_properties)

    def _extract_semantic_equivalents(self) -> Optional[str]:
        if "semanticEquivalent" in self._schema_payload:
            semantic_equivalents = []
            for se in self._schema_payload["semanticEquivalent"]:
                semantic_equivalents.append(se)
            return ", ".join(semantic_equivalents)
        return None

    def _identify_value_type(self, property) -> str:
        v_type = property["type"] if "type" in property else "object"
        if isinstance(v_type, list):
            if len(v_type) > 1:
                v_type = "or ".join([", ".join(v_type[:-1]), v_type[-1]])
        value_type = [v_type]
        if v_type == "array":
            i_type = property["items"]["type"] if "items" in property and "type" in property["items"] else "object"
            min_items = str(property["minItems"]) if "minItems" in property else "0"
            max_items = str(property["maxItems"]) if "maxItems" in property else "N"
            array_spec = f"\({min_items}-{max_items}\)"
            value_type = [i_type, v_type, array_spec]
        return " ".join(value_type)

    def _extract_edge_type(self, property):
        if "_embeddedTypes" in property:
            edge_type = "embedded"
        elif "_linkedTypes" in property:
            edge_type = "linked"
        else:
            edge_type = None
        return edge_type

    def _define_target_objects(self, object_list) -> str:
        if object_list:
            object_name_list = []
            for object in object_list:
                object_name = object.split('/')[-1]
                if object_name in self.relative_paths_for_schema_docu:
                    object_html_path = f"{self.readthedocs_url}{self.version}/schema_specifications/{self.relative_paths_for_schema_docu[object_name]}.html"
                    object_name_list.append(f"`{object_name} <{object_html_path}>`_")
                else:
                    object_name_list.append(f"{object_name} \[TYPE_ERROR\]")
            if len(object_name_list) > 1:
                target_objects = " or ".join([", ".join(object_name_list[:-1]), object_name_list[-1]])
            else:
                target_objects = object_name_list[0]
            return target_objects
        return "undefined"

    def extract_value_specs(self, property):
        value_type = self._identify_value_type(property)
        if "object" in value_type:
            edge_type = self._extract_edge_type(property)
            v_1st_line = f"| {edge_type} {value_type} of type"
            target_objects = self._define_target_objects(property[f"_{edge_type}Types"])
            v_2nd_line = f"| {target_objects}"
            value_type = [v_1st_line, v_2nd_line]
        elif "string" in value_type:
            v_1st_line = f"| {value_type}"
            formatting = property["formatting"] if "formatting" in property else "undefined"
            multiline = "multiline" if "multiline" in property and property["multiline"] else "singleline"
            value_type = [v_1st_line, f"| formatting: {formatting}; {multiline}"]
        else:
            value_type = [f"{value_type}"]
        return value_type
