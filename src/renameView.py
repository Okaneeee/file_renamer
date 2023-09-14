"""
Visual GUI for the file renamer.

Author: Okane (Zinnia Scans)
    - Twitter: @Okaneeeeeeeee_e / @ZinniaScans
    - Github: https://github.com/Okaneeee
    - MangaDex: https://mangadex.org/group/8bd939e5-dbcd-4ec8-b105-e6a19e8d8862/zinnia-scans
"""

# imports
from PyQt6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QFileDialog, QLabel, QHBoxLayout
from fileRenamer import FileRenamer

# class
class renameView(QWidget):
    def __init__(self) -> None:
        # default
        super().__init__()
        self.setWindowTitle("File Renamer")
        self.resize(500, 500)

        # main layout
        self.topLayout : QVBoxLayout = QVBoxLayout()
        self.setLayout(self.topLayout)
        self.load : QPushButton = QPushButton("Select folder") ; self.topLayout.addWidget(self.load)

        # signals
        self.load.clicked.connect(self.open)
        
        # show GUI
        self.show()

    # callbacks
    def open(self) -> None:
        folder = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        print(folder)

# test
if __name__ == "__main__":
    from PyQt6.QtWidgets import QApplication
    from sys import argv, exit
    app : QApplication = QApplication(argv)
    window = renameView()

    # show GUI
    exit(app.exec())