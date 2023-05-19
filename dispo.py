#disposition
import json
from collections import OrderedDict

def parse_sections(file_path):
    sections = []
    current_section = {}

    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

        for line in lines:
            line = line.strip()

            if line.startswith("Disposición"):
                if current_section:
                    sections.append(current_section)

                current_section = OrderedDict()  # Use OrderedDict to maintain key order
                current_section["type"] = ""  # Initialize "type" field
                current_section["title"] = line
                current_section["content"] = []
            elif current_section:
                    current_section["content"].append(line)

        if current_section:
            sections.append(current_section)

    # Join multiple content with a newline character
    for section in sections:
        section["content"] = "\n".join(section["content"])
        words = section["title"].split()
        if len(words) >= 2:
            section["type"] = words[1]

    return sections

def convert_to_json(sections, output_file_path):
    with open(output_file_path, 'w', encoding='utf-8') as file:
        json.dump(sections, file, indent=4, ensure_ascii=False)

# Provide the path to the input text file
input_file_path = "input.txt"

# Provide the path to the output JSON file
output_file_path = "output.json"

# Parse the sections from the input file
sections = parse_sections(input_file_path)

# Convert sections to JSON and save to the output file
convert_to_json(sections, output_file_path)
