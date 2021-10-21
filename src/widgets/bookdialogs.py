from PySide6 import QtWidgets, QtCore
from models.book import Book


class BookDetailsDialog(QtWidgets.QDialog):
    def __init__(self, book: Book):
        super().__init__()

        self.setWindowTitle(f"Book details - {book.title}")

        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("Title:", QtWidgets.QLabel(book.title))
        formLayout.addRow("Author:", QtWidgets.QLabel(book.authors))
        formLayout.addRow("Publication year:", QtWidgets.QLabel(book.pub_year))
        self.setLayout(formLayout)


class BookCreationDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        self.book = None

        self.setWindowTitle("New book")
        layout = QtWidgets.QVBoxLayout()

        self.ln_title = QtWidgets.QLineEdit("")
        self.ln_author = QtWidgets.QLineEdit("")
        self.ln_year = QtWidgets.QLineEdit("")

        formLayout = QtWidgets.QFormLayout()
        formLayout.addRow("Title:", self.ln_title)
        formLayout.addRow("Author:", self.ln_author)
        formLayout.addRow("Publication year:", self.ln_year)

        btnBox = QtWidgets.QDialogButtonBox()
        btnBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save
        )
        btnBox.accepted.connect(self.on_save)
        btnBox.rejected.connect(self.reject)

        layout.addLayout(formLayout)
        layout.addWidget(btnBox)
        self.setLayout(layout)

    @QtCore.Slot()
    def on_save(self):
        if self.validate():
            self.accept()
        else:
            error_dialog = QtWidgets.QErrorMessage(self)
            error_dialog.showMessage("Title is required.")

    def validate(self):
        if len(self.ln_title.text()) > 0:
            self.book = Book(self.ln_title.text(),
                             self.ln_author.text(), self.ln_year.text())
            return True
        return False
