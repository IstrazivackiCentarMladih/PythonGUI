from PySide6 import QtWidgets, QtCore


class MainWindow(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.calendar = QtWidgets.QCalendarWidget()
        self.label = QtWidgets.QLabel("Date isn't selected.")

        self.calendar.selectionChanged.connect(self.changeLabelText)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.calendar)
        self.setLayout(layout)

    @QtCore.Slot()
    def changeLabelText(self):
        date = self.calendar.selectedDate()
        self.label.setText(date.toString())


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = MainWindow()
    window.resize(400, 300)
    window.show()

    app.exec()
