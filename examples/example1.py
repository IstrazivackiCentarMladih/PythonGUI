from PySide6 import QtWidgets

if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = QtWidgets.QMainWindow()
    window.resize(800, 600)
    window.show()

    app.exec()