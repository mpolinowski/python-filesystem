 
from pathlib import Path
from datetime import datetime

path = Path('files/test1.md')
stats = path.stat()

# Get file size and set unit
def get_size():
    file_bytes = stats.st_size
    file_kilobytes = file_bytes / 1024
    file_megabytes = file_kilobytes / 1024

    if file_megabytes > 1:
        return str(file_megabytes) + ' MB'
    elif file_kilobytes > 1:
        return str(file_kilobytes) + ' kB'
    else:
        return str(file_bytes) + ' B'

# Get date last accessed and process timestamp
last_accessed = stats.st_ctime
date_accessed = datetime.fromtimestamp(last_accessed).strftime("%Y-%m-%d_%H:%M:%S")



# Append timestamp to file
with open(path, 'a') as file:
    file.write('\n' + date_accessed + ' | ' + get_size() + '\n') 