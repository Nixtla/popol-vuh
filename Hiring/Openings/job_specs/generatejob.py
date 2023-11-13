import argparse
import re


def load_definitions(file_paths):
    # Dictionary to hold definitions
    definitions = {}
    # Variables to keep track of the current definition and its content
    current_def = None
    current_text = []

    def save_definition():
        # If a definition is being tracked, save it to the dictionary
        if current_def and current_text:
            definitions[current_def] = "\n".join(current_text).strip()

    # Process each file path provided
    for file_path in file_paths:
        print(f"Loading definitions from {file_path}")
        with open(file_path, "r") as f:
            # Read file line by line
            for line in f:
                # Ignore HTML comment lines
                if re.match(r"^\s*<!--.*-->\s*$", line):
                    continue

                # Look for lines that define a new definition
                match = re.match(r"^\s*Def (\w+):\s*(.*)", line)
                if match:
                    # Save any ongoing definition to the dictionary
                    save_definition()
                    # Start tracking a new definition
                    current_def = f"{{{{Def {match.group(1)}}}}}"
                    current_text = [match.group(2).strip()]
                elif current_def:
                    # If we're inside a definition, append line content
                    current_text.append(line.rstrip())

        # After reading a file, save the last definition
        save_definition()

    return definitions


def preprocess_markdown(definitions):
    # Markdown template with placeholders for definitions
    template = """
# {{Def Title}}

**Location**: Remote. | **Job Type**: Full-time.

**Salary**: Competitive.
**Equity**: Competitive.
**Experience**: 4+ years.

## About Nixtla
{{Def Nixtla_Short}}

## This is our creed.
{{Def Creed}}

## About the Role
{{Def Role}}

## Key Responsibilities
{{Def Responsibilities}}

## What We Look For
{{Def Requirements}} 

## What We Offer
{{Def Benefits}}

## About the Interview Process
{{Def Interview}}

## Diversity Encouraged
{{Def Diversity}}\
    """

    # Replace placeholders in the template with actual definitions
    for placeholder, replacement in definitions.items():
        template = template.replace(placeholder, replacement)

    # Write the processed content to the output file
    output_file = definitions["{{Def OutputFile}}"]
    with open(output_file, "w") as f:
        # Write a comment indicating the file is auto-generated at the top
        f.write("<!-- Auto Generated file, do not modify -->")
        f.write(template)


DEFINITIONS_FILE_PATH = "../../../GeneralDefinitions.md"


def main(file: str):
    # Always read the hardcoded definitions file in addition to those passed as arguments
    definitions_files = [DEFINITIONS_FILE_PATH, file]
    # Load definitions from all provided definition files and the hardcoded file
    definitions = load_definitions(definitions_files)
    # Preprocess with the loaded definitions and output the result
    preprocess_markdown(definitions)


# Entry point of the script
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate Job Posting")
    parser.add_argument("--file", help="File to load", required=True)
    args = parser.parse_args()
    main(args.file)
