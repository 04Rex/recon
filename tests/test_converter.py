# tests/test_converter.py

import json
import tempfile
import os
from recon.converter import convert_file

def test_json_to_yaml(tmp_path):
    # Create a temporary JSON file
    data = {"name": "Alice", "age": 30}
    json_file = tmp_path / "test.json"
    json_file.write_text(json.dumps(data), encoding='utf-8')
    # Convert to YAML
    yaml_output = convert_file(str(json_file), "yaml")
    # Check that YAML output contains keys/values
    assert "name: Alice" in yaml_output
    assert "age: 30" in yaml_output

def test_yaml_to_json(tmp_path):
    # Create a temporary YAML file
    yaml_data = "city: Wonderland\npopulation: 1000"
    yaml_file = tmp_path / "test.yaml"
    yaml_file.write_text(yaml_data, encoding='utf-8')
    # Convert to JSON
    json_output = convert_file(str(yaml_file), "json")
    parsed = json.loads(json_output)
    assert parsed["city"] == "Wonderland"
    assert parsed["population"] == 1000

def test_invalid_format(tmp_path):
    # Create a file with unsupported extension
    txt_file = tmp_path / "data.txt"
    txt_file.write_text("just text", encoding='utf-8')
    try:
        convert_file(str(txt_file), "json")
    except ValueError as e:
        assert "Unsupported input format" in str(e)
