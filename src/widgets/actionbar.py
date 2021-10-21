from PySide6 import QtWidgets


class ActionBar(QtWidgets.QWidget):
    def __init__(self, actions):
        super().__init__()

        self._layout = QtWidgets.QHBoxLayout()
        self.setLayout(self._layout)

        for action in actions:
            btn = QtWidgets.QPushButton(action[0])
            btn.clicked.connect(action[1])
            self._layout.addWidget(btn)
