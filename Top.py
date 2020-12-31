import sys
import PySide2.QtCore as QtCore
from PySide2.QtWidgets import QApplication, QMainWindow, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QFileDialog, QErrorMessage
from PySide2.QtGui import QPixmap, QFont, QColor
from editor import Editor
from backend import compile


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainW = QWidget(self)
        self.compile = QPushButton(self, text="Compile")
        self.browse = QPushButton(self, text="Browse")
        self.editor = Editor()
        
        buttonsLau = QHBoxLayout()
        buttonsLau.addWidget(self.compile)
        buttonsLau.addWidget(self.browse)

        self.setCentralWidget(self.mainW)
        self.mainW.setLayout(QVBoxLayout())
        self.mainW.layout().addWidget(self.editor)
        self.mainW.layout().addLayout(buttonsLau)

        self.browse.clicked.connect(self._on_browse_clicked)
        self.compile.clicked.connect(self._on_compile_clicked)
    
    def _on_browse_clicked(self):
        files = QFileDialog.getOpenFileNames(self, "Open File", None, None)[0]
        if len(files) > 0:
            path = files[0]
            f = open(path, "r")
            content = "".join(f.readlines())
            self.editor.setPlainText(content)
    
    def _on_compile_clicked(self):
        try:
            content = self.editor.toPlainText()
            compile(content)
        except:
            error_dialog = QErrorMessage(self)
            error_dialog.showMessage('Unknown token')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    m = MainWindow()

    m.show()
    sys.exit(app.exec_())

