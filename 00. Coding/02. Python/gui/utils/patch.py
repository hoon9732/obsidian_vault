import os

def replace_strings_in_file(file_path, replacements):
    # Read the content of the file
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Apply all replacements
    for old, new in replacements.items():
        content = content.replace(old, new)
    
    # Write the modified content back to the file
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def process_ui_main_in_modules(folder_path):
    # Define the path to ui_main.py within the folder
    file_path = os.path.join(folder_path, 'ui_main.py')
    
    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    # Define the replacements
    replacements = {
        'import resources_rc': 'from .resources_rc import *',
        'Qt.AlignmentFlag.Qt.AlignmentFlag.AlignTop': 'Qt.AlignTop',
        'Qt.AlignmentFlag.Qt.AlignmentFlag.AlignBottom': 'Qt.AlignBottom',
        'font1.setWeight(QFont.)': 'font1.setBold(False)'
    }
    
    # Replace strings in the file
    replace_strings_in_file(file_path, replacements)
    print(f"Replacements made in {file_path}")



# Example usage
folder_path = 'modules'
process_ui_main_in_modules(folder_path)
