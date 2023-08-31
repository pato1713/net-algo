from PySide6.QtWidgets import QVBoxLayout, QPushButton


class ActionsSidebar(QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.randomize_bttn = QPushButton(
            text="Reload",
        )
        self.calculate_path_bttn = QPushButton(text="Calculate path")

        self.addWidget(self.randomize_bttn)
        self.addWidget(self.calculate_path_bttn)
