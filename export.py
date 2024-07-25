import os
import shutil
import yaml


def create_image_label_files(input_image_folder, input_label_file, output_folder):
    # Create the output folder if it doesn't exist
    os.makedirs(output_folder, exist_ok=True)

    # Read the label.txt file
    with open(input_label_file, 'r') as label_file:
        lines = label_file.readlines()

        for line in lines:
            if line.strip():  # Check if the line is not empty
                # Split the line to get the image name and label
                parts = line.split('\t#')
                if len(parts) == 2:
                    image_name = parts[0].strip()
                    label = parts[1].strip()

                    # Copy the image to the output folder
                    image_path = os.path.join(input_image_folder, image_name)
                    if os.path.exists(image_path):
                        shutil.copy(image_path, output_folder)

                    # Create the label.txt file with the corresponding label
                    label_file_path = os.path.join(
                        output_folder, os.path.splitext(image_name)[0] + '.txt')
                    with open(label_file_path, 'w') as label_file:
                        label_file.write('# ' + label)
                # For cases where there is no tab but a different separator (e.g., '*', '##')
                elif len(parts) == 1:
                    image_name = parts[0].strip().split()[0]
                    label = parts[0].strip().split(
                        ' ', 1)[1] if ' ' in parts[0] else ""

                    # Copy the image to the output folder
                    image_path = os.path.join(input_image_folder, image_name)
                    if os.path.exists(image_path):
                        shutil.copy(image_path, output_folder)

                    # Create the label.txt file with the corresponding label
                    label_file_path = os.path.join(
                        output_folder, os.path.splitext(image_name)[0] + '.txt')
                    with open(label_file_path, 'w') as label_file:
                        label_file.write(parts[0].strip().replace(
                            image_name, '').strip())


# Read the config.yaml file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

input_image_folder = config['input_image_folder']
input_label_file = config['input_label_file']
output_folder = 'output'


create_image_label_files(input_image_folder, input_label_file, output_folder)
