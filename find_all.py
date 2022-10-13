from pathlib import Path

root_dir = Path('files')
search_term = 'test'

for path in root_dir.rglob('*'):
    if search_term in path.stem:
        print(path.absolute())
