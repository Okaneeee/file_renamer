"""
Visual GUI for the file renamer.

Author: Okane (Zinnia Scans)
    - Twitter: @Okaneeeeeeeee_e / @ZinniaScans
    - Github: https://github.com/Okaneeee
    - MangaDex: https://mangadex.org/group/8bd939e5-dbcd-4ec8-b105-e6a19e8d8862/zinnia-scans
"""

# imports
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QHBoxLayout, QLineEdit, QComboBox
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
from fileRenamer import FileRenamer

# class
class renameView(QWidget):
    def __init__(self) -> None:
        # default
        super().__init__()
        self.setWindowTitle("Files Renamer")
        self.setWindowIcon(QIcon("assets/icon.png"))
        self.resize(500, 220)
        self.setFixedSize(self.size())
        self.fr: FileRenamer = FileRenamer()

        # main layout
        self.topLayout: QVBoxLayout = QVBoxLayout()
        self.setLayout(self.topLayout)
        
        # QLine layout
        self.lineLayout1: QHBoxLayout = QHBoxLayout()
        self.lineLayout2: QHBoxLayout = QHBoxLayout()
        self.linesLayout: QVBoxLayout = QVBoxLayout()

        self.linesLayout.addLayout(self.lineLayout1) ; self.linesLayout.addLayout(self.lineLayout2)
        self.topLayout.addLayout(self.linesLayout)

        # Buttons layout
        self.buttonsLayout: QVBoxLayout = QVBoxLayout()
        self.topLayout.addLayout(self.buttonsLayout)

        # Folder selection layout
        self.folderLayout: QVBoxLayout = QVBoxLayout() ; self.folderLayout.addStretch()
        self.buttonsLayout.addLayout(self.folderLayout)

        # widgets
        # --- folder selection ---
        self.folderLoader: QPushButton = QPushButton("Select folder") ; self.folderLayout.addWidget(self.folderLoader)
        self.selectedFolder: QLabel = QLabel("No folder selected") ; self.folderLayout.addWidget(self.selectedFolder)
        self.selectedFolder.setAlignment(Qt.AlignmentFlag.AlignCenter) ; self.folderLayout.addStretch()

        # --- rename ---
        self.renameButton: QPushButton = QPushButton("Rename") ; self.buttonsLayout.addWidget(self.renameButton)

        # --- rename parameters ---
        self.startFileName : QLineEdit = QLineEdit() ; self.startFileName.setPlaceholderText("Name of the first file to rename (+1)")
        self.startFileName.setFixedWidth(235) ; self.lineLayout1.addWidget(self.startFileName)
        
        self.startNumber : QLineEdit = QLineEdit() ; self.startNumber.setPlaceholderText("Name of the first file to rename (+1)")
        self.startNumber.setFixedWidth(235) ; self.lineLayout1.addWidget(self.startNumber)
        
        self.renameFormat : QLineEdit = QLineEdit() ; self.renameFormat.setPlaceholderText("Format of the renamed files")
        self.renameFormat.setFixedWidth(235) ; self.lineLayout2.addWidget(self.renameFormat)
        
        self.fileExtension : QComboBox = QComboBox() ; self.fileExtension.addItems(["File extension (customizable)", ".jpg", ".jpeg", ".png ", ".psd" , ".txt"]) ; self.fileExtension.setEditable(True)
        self.fileExtension.setFixedWidth(235) ; self.lineLayout2.addWidget(self.fileExtension)

        # signals
        self.folderLoader.clicked.connect(self.open)
        self.renameButton.clicked.connect(self.rename)
        
        # show GUI
        self.show()

    # callbacks
    def open(self) -> None:
        folder = str(QFileDialog.getExistingDirectory(self, "Select Folder"))
        self.selectedFolder.setText(folder)

    def rename(self) -> None:
        print("rename")

# test
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    from sys import argv, exit
    app: QApplication = QApplication(argv)
    window = renameView()

    # show GUI
    exit(app.exec())