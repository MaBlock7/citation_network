import os
import importlib.util

# Define a function to import dictionary from a Python file
def import_dictionary(module_name, file_path):
    spec = importlib.util.spec_from_file_location(module_name, file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return getattr(module, module_name)

# Directory containing your Python files
directory = 'data/raw'

# Initialize an empty dictionary to hold the combined dictionaries
combined_dict = {}

# Loop through each file in the directory
for filename in os.listdir(directory):
    print(filename)
    if filename.endswith('.py'):  # Check if file is a Python file
        file_path = os.path.join(directory, filename)
        # Import the dictionary from the file
        dictionary = import_dictionary('literature_titles', file_path)
        # Merge the dictionaries
        combined_dict.update(dictionary)

# Export the combined dictionary to a new file
with open('data/references.py', 'w') as f:
    f.write("reference_dict = " + str(combined_dict))