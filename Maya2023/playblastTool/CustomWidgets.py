from PyQt5.QtWidgets import QComboBox, QPushButton, QGroupBox
from PyQt5.QtGui import QFontMetrics, QPainter, QTextOption
from PyQt5.QtCore import Qt



class CheckableCombobox(QComboBox):
    def __init__(self, parent=None):
        super(CheckableCombobox, self).__init__(parent)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)
        self.closeOnLineEditClick = False
        self.lineEdit().installEventFilter(self)
        self.model().dataChanged.connect(self.updateLineEditField)

    def addItems(self, items):
        super(CheckableCombobox, self).addItems(items)
        for item in items:
            self.addItem(item)

    def addItem(self, item=None, data=None):
        super(CheckableCombobox, self).addItem(item)
        item = self.model().item(self.count() - 1, 0)
        item.setFlags(Qt.ItemIsUserCheckable | Qt.ItemIsEnabled)
        item.setCheckState(Qt.Unchecked)
        if data:
            self.setItemData(self.count()-1, data)

    def updateLineEditField(self):
        text_container = self.getCheckedItems()
        text_string = ', '.join(text_container)
        option = QTextOption()
        option.setAlignment(self.lineEdit().alignment())
        metrics = QFontMetrics(self.font())
        elided_text = metrics.elidedText(text_string,
                                         Qt.ElideRight,
                                         self.lineEdit().width())
        self.lineEdit().setText(elided_text)
        self.updateToolTip(text_container)

    def getCheckedData(self):
        checkedItemsData = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                checkedItemsData.append(self.itemData(i))
        return checkedItemsData

    def getCheckedItems(self):
        checkedItems = []
        for i in range(self.model().rowCount()):
            if self.model().item(i).checkState() == Qt.CheckState.Checked:
                checkedItems.append(self.model().item(i).text())
        return checkedItems

    def updateToolTip(self, checkedItems):
        toolTipText = "Please select one or more Cameras"
        if checkedItems:
            toolTipText = "\n".join(checkedItems)
        self.setToolTip(toolTipText)


def applyStyle(MainWindow):

    for widget in MainWindow.findChildren(QPushButton):
        widget.setStyleSheet("""
        QPushButton {
            border: 0.5px solid lightgreen;
            border-radius: 5px; /* Rounded corners */
            padding: 5px; /* Padding inside the button */
        }

        QPushButton:hover {
            background-color: lightgray;
        }

        QPushButton:pressed {
            background-color: gray;
        }""")






