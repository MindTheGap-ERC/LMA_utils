import os
import yaml

def generate_parameters(directory_path, output_file):
    hdf5_files = [os.path.relpath(os.path.join(root, file), directory_path)
                  for root, dirs, files in os.walk(directory_path)
                  for file in files if file.endswith('.hdf5')]

    yaml_data = {'Solution_path': hdf5_files}

    with open(output_file, 'w') as yaml_file:
        yaml.dump(yaml_data, yaml_file)

generate_parameters('../data/jghsx/', 'parameters.yaml')
