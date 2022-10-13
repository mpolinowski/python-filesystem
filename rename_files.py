from pathlib import Path

root_dir = Path('files')

# Replace the file extension

file = Path('files/test2.md')
filename = file.with_suffix('.csv')
file.rename(filename)

# Add static prefix to filename

file_paths = root_dir.iterdir()

for path in file_paths:
    if path.is_file():
        new_filename = "prefix_" + path.stem + path.suffix
        # print(new_filename)
        new_path = path.with_name(new_filename)
        path.rename(new_path)

# Add suffix based on sub directory

recursive_paths = root_dir.glob('**/*')

for path in recursive_paths:
    if path.is_file():
        parent_folder = path.parts[-2]
        # print(parent_folder)
        new_filename = path.stem + '_' + parent_folder + path.suffix
        # print(new_filename)
        new_path = path.with_name(new_filename)
        path.rename(new_path)

    

