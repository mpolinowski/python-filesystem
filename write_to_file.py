from pathlib import Path

file_path = Path('files/projectB/test1.md')
root_dir = Path('files/projectA')
content = """# Test 1

this is a test
"""

# Create empty files

for i in range(0, 3):
    filename = 'test' + str(i) + '.md'
    filepath = root_dir / Path(filename)
    filepath.touch()


# Create file if not exists and add content

if not file_path.exists():
    with open(file_path, 'w') as file:
        file.write(content)    

# Read all files in directory

for item in root_dir.iterdir():
    with open(item, 'w') as file:
        file.write(content) 
    with open(item, 'r') as file:
        print(file.read())