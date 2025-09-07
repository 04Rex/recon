# recon/converter.py

import json
import yaml
import xmltodict
import markdown

def load_data(input_path):
    """
    Load data from the given input file path into a Python object.
    Supports JSON, YAML, XML, and Markdown (as raw text).
    """
    data = None
    ext = input_path.lower().split('.')[-1]
    with open(input_path, 'r', encoding='utf-8') as f:
        text = f.read()
    if ext in ("json",):
        # Parse JSON
        data = json.loads(text)
    elif ext in ("yaml", "yml"):
        # Parse YAML using PyYAML
        data = yaml.safe_load(text)
    elif ext == "xml":
        # Parse XML into dict using xmltodict
        data = xmltodict.parse(text)
    elif ext in ("md", "markdown"):
        # Treat markdown as raw text (store under 'content' key)
        # Python-Markdown could parse to HTML if needed:
        html = markdown.markdown(text)
        data = {"markdown_content": text, "html": html}
    else:
        raise ValueError(f"Unsupported input format: .{ext}")
    return data

def dump_data(data, output_format):
    """
    Dump the Python object `data` to a string in the specified format.
    Supports 'json', 'yaml', 'xml', and 'md' (markdown).
    """
    fmt = output_format.lower()
    if fmt == "json":
        # Convert to JSON string with indentation
        return json.dumps(data, indent=2)
    elif fmt == "yaml":
        # Convert to YAML string
        return yaml.dump(data, sort_keys=False)
    elif fmt == "xml":
        # Convert dict back to XML. xmltodict expects a dict with a single root element.
        return xmltodict.unparse(data, pretty=True)
    elif fmt in ("md", "markdown"):
        # Convert data to Markdown format (simple YAML-style block)
        # Here we convert dict to a Markdown code block for demonstration.
        md_text = "```\n" + yaml.dump(data, sort_keys=False) + "```"
        return md_text
    else:
        raise ValueError(f"Unsupported output format: {output_format}")

def convert_file(input_path, output_format):
    """
    Read the input file, convert its content, and return the result string.
    """
    # Load data from input
    data = load_data(input_path)
    # Dump data to target format
    return dump_data(data, output_format)
