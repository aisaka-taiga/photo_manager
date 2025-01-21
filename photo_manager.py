import sys
import os
import shutil
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QLabel, QVBoxLayout, QWidget, QPushButton, QMessageBox
from PySide6.QtCore import Qt

class FileMover(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RAW & JPG File Mover")
        self.setGeometry(100, 100, 400, 200)

        self.label = QLabel("Drag & Drop a folder here or select a folder.", self)
        self.label.setAlignment(Qt.AlignCenter)

        self.setAcceptDrops(True)

        layout = QVBoxLayout()
        layout.addWidget(self.label)

        self.button = QPushButton("Select Folder", self)
        self.button.clicked.connect(self.select_folder)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        for url in event.mimeData().urls():
            folder_path = url.toLocalFile()
            if os.path.isdir(folder_path):
                self.move_files(folder_path)

    def select_folder(self):
        folder_path = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder_path:
            self.move_files(folder_path)

    def move_files(self, folder_path):
        raw_folder = os.path.join(folder_path, "RAW")
        jpg_folder = os.path.join(folder_path, "JPG")

        # 폴더가 없으면 생성
        os.makedirs(raw_folder, exist_ok=True)
        os.makedirs(jpg_folder, exist_ok=True)

        # 파일 이동
        for filename in os.listdir(folder_path):
            file_path = os.path.join(folder_path, filename)
            if os.path.isfile(file_path):
                if filename.lower().endswith((
                    '.arw', '.cr2', '.cr3',  # Canon
                    '.nef', '.nrw',          # Nikon
                    '.pef', '.dng',          # Pentax
                    '.raf',                  # Fujifilm
                    '.dng',                  # Apple, Google
                    '.srw',                  # Samsung
                    '.orf',                  # Olympus
                    '.srf', '.sr2', '.arw',  # Sony
                    '.rw2',                  # Panasonic
                    '.3fr',                  # Hasselblad
                    '.dcr', '.kdc',         # Kodak
                    '.mrw',                  # Konica Minolta
                    '.rwl', '.dng',          # Leica
                    '.mos',                  # Mamiya
                    '.x3f', '.dng',          # Sigma
                    '.gpr',                  # GoPro
                    '.r3d',                  # RED
                    '.braw',                 # Blackmagic Design
                    '.ari'                   # ARRI
                )):
                    shutil.move(file_path, raw_folder)
                elif filename.lower().endswith(('.jpeg', '.jpg')):
                    shutil.move(file_path, jpg_folder)

        QMessageBox.information(self, "완료", "파일 이동이 완료되었습니다.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileMover()
    window.show()
    sys.exit(app.exec())
