from PyQt6.QtWidgets import (
    QApplication,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QWidget,
    QLabel,
    QFileDialog
)
from pathlib import Path

def open_files():
    global filenames
    # return absolute path of user selected files
    filenames, _ = QFileDialog.getOpenFileNames(window, 'Select files')
    message.setText('\n'.join(filenames))

def delete_files():
    for filename in filenames:
        path = Path(filename)
        with open(path, 'wb') as file:
            file.write(b'')
        path.unlink()
        message.setText('Deleted!')


app = QApplication([])
window = QWidget()
window.setWindowTitle('Destroyer of Worlds')

# set layout

layout_main = QVBoxLayout()
layout_top_container = QHBoxLayout()
layout_main.addLayout(layout_top_container)
layout_bottom_container = QHBoxLayout()
layout_main.addLayout(layout_bottom_container)

# select files to delete

description = QLabel('Select files for <font color="red">deletion</font>: ')
layout_top_container.addWidget(description)

open_btn = QPushButton('Open Files')
open_btn.setToolTip('Open files and select for deletions.')
layout_top_container.addWidget(open_btn)
open_btn.clicked.connect(open_files)

# delete selected files

del_btn = QPushButton('Delete Files')
del_btn.setToolTip('Permanently delete all selected files.')
layout_bottom_container.addWidget(del_btn)
del_btn.clicked.connect(delete_files)

# show filepath of selected files

message = QLabel('')
layout_main.addWidget(message)

# run app

window.setLayout(layout_main)
window.show()
app.exec()