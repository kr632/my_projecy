import sys
import os
from PySide6.QtWidgets import (
    QApplication, QWidget, QPushButton, QVBoxLayout,
    QFileDialog, QLineEdit, QLabel
)

class RenameTool(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Image Sequence Renamer")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        self.label = QLabel("Select Folder:")
        layout.addWidget(self.label)

        self.btn_browse = QPushButton("Browse Folder")
        self.btn_browse.clicked.connect(self.select_folder)
        layout.addWidget(self.btn_browse)

        self.start_input = QLineEdit()
        self.start_input.setPlaceholderText("Start Frame (e.g. 1001)")
        layout.addWidget(self.start_input)

        self.rename_btn = QPushButton("Rename Sequence")
        self.rename_btn.clicked.connect(self.rename_files)
        layout.addWidget(self.rename_btn)

        self.setLayout(layout)
        self.folder_path = ""

    def select_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "Select Folder")
        if folder:
            self.folder_path = folder
            self.label.setText(folder)

    def rename_files(self):
        if not self.folder_path:
            self.label.setText("Please select folder first!")
            return

        try:
            start_frame = int(self.start_input.text())
        except:
            self.label.setText("Enter valid number!")
            return

        files = sorted([f for f in os.listdir(self.folder_path) if f.endswith(".jpg")])

        # Step 1: temp rename
        for f in files:
            os.rename(
                os.path.join(self.folder_path, f),
                os.path.join(self.folder_path, "temp_" + f)
            )

        temp_files = sorted([f for f in os.listdir(self.folder_path) if f.startswith("temp_")])

        # Step 2: final rename
        for i, f in enumerate(temp_files):
            new_name = f"image_{start_frame + i:04d}.jpg"

            os.rename(
                os.path.join(self.folder_path, f),
                os.path.join(self.folder_path, new_name)
            )

        self.label.setText("Done!")

app = QApplication(sys.argv)
window = RenameTool()
window.show()
sys.exit(app.exec())