import sys
import pickle
import os

from PySide6 import QtWidgets, QtCore, QtGui
from widgets.actionbar import ActionBar
from widgets.bookdialogs import BookCreationDialog, BookDetailsDialog


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.load_books()

        self._layout = QtWidgets.QVBoxLayout()
        self.setLayout(self._layout)

        # action bar
        actions = [
            ("New", self.book_new),
            ("Details", self.book_details),
            ("Delete", self.book_delete),
        ]

        self.action_bar = ActionBar(actions)
        self._layout.addWidget(self.action_bar)

        # books table
        self.table_books = QtWidgets.QTableWidget()
        self._layout.addWidget(self.table_books)

        self.table_books.horizontalHeader().setStretchLastSection(True)
        self.table_books.setAlternatingRowColors(True)
        self.table_books.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.table_books.setSelectionMode(
            QtWidgets.QTableView.SingleSelection)
        self.table_books.setEditTriggers(QtWidgets.QTableView.NoEditTriggers)

        self.table_books.itemSelectionChanged.connect(self.print_row)

        self.columns = ["title", "authors", "publication year"]
        self.field_names = ["title", "authors", "pub_year"]

        self.initialize_table()

    def initialize_table(self):
        self.table_books.setRowCount(len(self.books))
        self.table_books.setColumnCount(len(self.columns))

        for col, colname in enumerate(self.columns):
            self.table_books.setHorizontalHeaderItem(
                col, QtWidgets.QTableWidgetItem(colname))

        for row, book in enumerate(self.books):
            for col, field in enumerate(self.field_names):
                self.table_books.setItem(
                    row, col, QtWidgets.QTableWidgetItem(
                        str(getattr(book, field))))

    @QtCore.Slot()
    def book_new(self):
        dialog = BookCreationDialog()
        value = dialog.exec()

        if value:
            book = dialog.book
            row = len(self.books)
            self.books.append(book)
            self.table_books.insertRow(row)
            for col, field in enumerate(self.field_names):
                self.table_books.setItem(
                    row, col, QtWidgets.QTableWidgetItem(
                        str(getattr(book, field))))

    @QtCore.Slot()
    def book_details(self):
        selection = self.table_books.selectedItems()
        if not selection or len(selection) == 0:
            return

        selected_row = selection[0].row()
        book = self.books[selected_row]

        self._book_details_dialog = BookDetailsDialog(book)
        self._book_details_dialog.show()

    @QtCore.Slot()
    def book_delete(self):
        selection = self.table_books.selectedItems()
        if not selection or len(selection) == 0:
            return

        selected_row = selection[0].row()
        self.table_books.removeRow(selected_row)
        del self.books[selected_row]

    @QtCore.Slot()
    def print_row(self):
        selection = self.table_books.selectedItems()
        if not selection or len(selection) == 0:
            return

        selected_row = selection[0].row()
        print(selected_row)

    def load_books(self):
        # self. books = [
        #    Book("Crooked House", "Agatha Christie", "1949"),
        #    Book("Life of Pi", "Yann Martel", "2006")
        # ]
        if not os.path.exists('db.pickle'):
            self.books = []
            return

        with open('db.pickle', 'rb') as file_handle:
            self.books = pickle.load(file_handle)

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        with open('db.pickle', 'wb') as file_handle:
            pickle.dump(self.books, file_handle,
                        protocol=pickle.HIGHEST_PROTOCOL)
        return super().closeEvent(event)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    widget = MainWindow()
    widget.resize(400, 400)
    widget.show()

    with open("src/style.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)

    sys.exit(app.exec())
