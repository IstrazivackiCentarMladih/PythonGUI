from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.combobox = QtWidgets.QComboBox()
        self.label = QtWidgets.QLabel("apple")

        self.combobox.insertItems(0, ["apple", "banana", "citrus"])

        self.combobox.currentTextChanged.connect(self.changeLabelText)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combobox)
        self.setLayout(layout)

    @QtCore.Slot(str)
    def changeLabelText(self, text):
        self.label.setText(text)


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.resize(400, 300)
    window.show()

    app.exec()
