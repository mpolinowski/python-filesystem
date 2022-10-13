from pathlib import Path
from datetime import datetime
import zipfile

root_dir = Path('files/projectA')
# get timestamp for archive name
now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
archive_name = now + '_archive.zip'
archive_path = root_dir / Path(archive_name)

# write all markdown pages in dir to zip container
with zipfile.ZipFile(archive_path, 'w') as zf:
    for path in root_dir.glob('*.md'):
        zf.write(path)
        # delete source files
        # path.unlink()


# unzip all containers in root dir recursively
destination_path = Path('files/unzipped')

for path in root_dir.rglob('*.zip'):
    with zipfile.ZipFile(path, 'r') as zf:
        sub_dir = destination_path / Path(path.stem)
        zf.extractall(path=sub_dir)