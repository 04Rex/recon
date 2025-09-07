**Recon** is a command-line tool for converting data between **JSON**, **YAML**, **XML**, and **Markdown** formats. It reads an input file of one format and outputs in another.

**Requires Python 3.8+**

## Installation

Clone the repository and install with pip:

```bash
pip install -e .
```

## Usage

Run Recon with the `-convert` flag to specify the input file, and one output format flag (`-json`, `-yaml`, `-xml`, or `-md`). For example:
```bash
recon -convert ./example.json -xml
```
This reads example.json and converts it into XML.

## Updating

Remember to update the requirements in both `setup.py` and `requirements.txt`
