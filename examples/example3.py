from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.checkbox = QtWidgets.QCheckBox("checkbox")
        self.label = QtWidgets.QLabel("False")

        self.checkbox.stateChanged.connect(self.changeLabelText)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.checkbox)
        self.setLayout(layout)

    @QtCore.Slot(int)
    def changeLabelText(self, check):
        if check == 0:
            self.label.setText("False")
        else:
            self.label.setText("True")


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.resize(400, 300)
    window.show()

    app.exec()
