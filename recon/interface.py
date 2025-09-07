# recon/interface.py

import argparse
import sys
from . import __version__
from .converter import convert_file

def main():
    parser = argparse.ArgumentParser(
        description="Recon: Convert between JSON, YAML, XML, and Markdown."
    )
    # Custom -help alias since we use -convert instead of positional arguments
    parser.add_argument('-help', '--help', action='help',
                        help='Show a help message and exit')
    parser.add_argument('-v', '--version', '-version', action='version',
                        version=f'%(prog)s {__version__}',
                        help='Show program version and exit')
    parser.add_argument('-convert', metavar='FILE', type=str, required=True,
                        help='Path of input file to convert')
    # Define mutually exclusive output format flags
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-json', action='store_true', help='Convert to JSON')
    group.add_argument('-yaml', '-yml', action='store_true', help='Convert to YAML')
    group.add_argument('-xml', action='store_true', help='Convert to XML')
    group.add_argument('-md', action='store_true', help='Convert to Markdown')
    args = parser.parse_args()

    # Determine target format based on flags
    if args.json:
        target = "json"
    elif args.yaml:
        target = "yaml"
    elif args.xml:
        target = "xml"
    elif args.md:
        target = "md"
    else:
        print("Error: No output format specified.", file=sys.stderr)
        sys.exit(1)

    # Perform conversion and print result
    try:
        result = convert_file(args.convert, target)
        print(result)
    except Exception as e:
        print(f"Conversion failed: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
