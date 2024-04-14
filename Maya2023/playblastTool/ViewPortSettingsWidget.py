from PyQt5.QtWidgets import (QComboBox, QWidget, QHBoxLayout, QLabel, QCheckBox,
                             QSizePolicy, QGroupBox)
from PyQt5.QtCore import Qt


class ViewPortSettingsItem(QWidget):
    def __init__(self, settingName):
        super().__init__()

        self.text = settingName

        grouplayout = QHBoxLayout()
        containerBox = QGroupBox()
        self.checkBox = QCheckBox("Toggle")
        self.label = QLabel(self.text)
        grouplayout.addWidget(self.label)
        grouplayout.addWidget(self.checkBox)
        containerBox.setLayout(grouplayout)

        self.layout = QHBoxLayout()
        self.layout.addWidget(containerBox)
        self.setLayout(self.layout)
