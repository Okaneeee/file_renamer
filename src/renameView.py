"""
Visual GUI for the file renamer.

Author: Okane (Zinnia Scans)
    - Twitter: @Okaneeeeeeeee_e / @ZinniaScans
    - Github: https://github.com/Okaneeee
    - MangaDex: https://mangadex.org/group/8bd939e5-dbcd-4ec8-b105-e6a19e8d8862/zinnia-scans
"""

# imports
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QHBoxLayout, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from fileRenamer import FileRenamer

# class
class renameView(QWidget):
    def __init__(self) -> None:
        # default
        super().__init__()
        self.setWindowTitle("File Renamer")
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.resize(500, 500)

        # main layout
        self.topLayout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.topLayout)
        
        # QLine layout
        self.lineLayout: QHBoxLayout = QHBoxLayout()
        self.topLayout.addLayout(self.lineLayout)

        # Buttons layout
        self.buttonsLayout: QVBoxLayout = QVBoxLayout()
        self.topLayout.addLayout(self.buttonsLayout)

        # Folder selection layout
        self.folderLayout: QVBoxLayout = QVBoxLayout() ; self.folderLayout.addStretch()
        self.buttonsLayout.addLayout(self.folderLayout)

        # widgets
        self.folderLoader: QPushButton = QPushButton("Select folder") ; self.folderLayout.addWidget(self.folderLoader)
        self.selectedFolder: QLabel = QLabel("No folder selected") ; self.folderLayout.addWidget(self.selectedFolder)
        self.selectedFolder.setAlignment(Qt.AlignmentFlag.AlignCenter) ; self.folderLayout.addStretch()

        self.renameButton: QPushButton = QPushButton("Rename") ; self.buttonsLayout.addWidget(self.renameButton)

        # signals
        self.folderLoader.clicked.connect(self.open)
        self.renameButton.clicked.connect(self.rename)
        
        # show GUI
        self.show()

    # callbacks
    def open(self) -> None:
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.selectedFolder.setText(f"𝐒𝐞𝐥𝐞𝐜𝐭𝐞𝐝 𝐅𝐨𝐥𝐝𝐞𝐫: {folder}")

    def rename(self) -> None:
        ...

# test
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    from sys import argv, exit
    app: QApplication = QApplication(argv)
    window = renameView()

    # show GUI
    exit(app.exec())