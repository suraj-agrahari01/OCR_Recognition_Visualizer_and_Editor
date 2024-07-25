def convert_format(file2_path, output_path):
    with open(file2_path, 'r') as file2, open(output_path, 'w') as output:
        for line in file2:
            parts = line.strip().split()
            if len(parts) < 2:
                continue  # skip malformed lines
            filename = parts[0]
            code = parts[1]

            # Default comment to be added
            comment = code

            # Write the converted line to the output file
            output.write(f'{filename}\t{comment}\n')


# File paths
file2_path = r'sangeet\labels.txt'  # Update this with the actual path to file 2
output_path = 'converted_file1_format.txt'  # The output file path

# Convert the format
convert_format(file2_path, output_path)

print(f'File has been converted and saved to {output_path}')
