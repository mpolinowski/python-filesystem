from pathlib import Path

root_dir = Path('files/projectA')

for path in root_dir.rglob("*.zip"):
    with open(path, 'wb') as file:
        # overwrite with empty bytes to delete secure
        file.write(b'')
    # delete all zip files
    path.unlink()