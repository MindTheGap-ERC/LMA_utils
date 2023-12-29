import os

def generate_parameters(directory_path, output_file):
    hdf5_files = [os.path.relpath(os.path.join(root, file), directory_path)
                  for root, dirs, files in os.walk(directory_path)
                  for file in files if file.endswith('.hdf5')]

    with open(output_file, 'w') as yaml_file:
        for file in hdf5_files:
            yaml_file.write(f"'Solution_path': {directory_path}{file}\n")

generate_parameters('../../data/', 'parameters.yaml')