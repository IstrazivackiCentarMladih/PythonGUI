from PySide6 import QtWidgets, QtCore

class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Basic")

        self.button = QtWidgets.QPushButton("Toggle")
        self.label = QtWidgets.QLabel("OFF")

        self.button.clicked.connect(self.changeLabelText)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        self.setLayout(layout)

    @QtCore.Slot()
    def changeLabelText(self):
        if self.label.text() == "OFF":
            self.label.setText("ON")
        else:
            self.label.setText("OFF")

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.resize(800, 600)
    window.show()

    app.exec()