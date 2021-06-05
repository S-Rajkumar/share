import sys
from PyQt5 import (
    QtCore, 
    QtWidgets,
)
from PyQt5.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QWidget,
)

TEMPLATE_FILE_PATH = ""
BATCH_NAME = ""
TEST_FILES_LIST = []

class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDF Testing Tool")
        self.initUI()

    def initUI(self):
        layout = QGridLayout()

        self.batchNameLabel = QLabel("Batch Name")
        self.batchNameTextBox = QLineEdit()

        self.templateLabel = QLabel("Template Path")
        self.templateTextBox = QLineEdit()
        self.templateBrowseButton = QPushButton("Browse")
        self.templateBrowseButton.clicked.connect(self.getTemplateFile)

        self.compareLabel = QLabel("Path to Compare")
        self.compareTextbox = QLineEdit()
        self.compareBrowseButton = QPushButton("Browse")
        self.compareBrowseButton.clicked.connect(self.getTestFiles)
        self.testRangeLabel = QLabel("Range Of Testing")
        self.testRangeTextBox = QLineEdit()
        self.testRangeRadioButton1 = QRadioButton("All")
        self.testRangeRadioButton2 = QRadioButton("Custom")
        
        self.emptyLabel = QLabel("")

        self.startTestButton = QPushButton("Begin Test")
        self.startTestButton.clicked.connect(self.startTest)
        self.resetButton = QPushButton("Reset")
        self.resetButton.clicked.connect(self.resetWindow)
        self.closeButton = QPushButton("Close")
        self.closeButton.clicked.connect(self.close)

        layout.addWidget(self.batchNameLabel, 0, 0) # 0 = Row, 0 = Column
        layout.addWidget(self.batchNameTextBox, 0, 1, 1, 3) # 0 = fromRow, 1 = fromColumn, 1 = RowSpan, 3 = ColumnSpan
        layout.addWidget(self.templateLabel, 1, 0)
        layout.addWidget(self.templateTextBox, 1, 1, 1, 2)
        layout.addWidget(self.templateBrowseButton, 1, 3)
        layout.addWidget(self.compareLabel, 2, 0)
        layout.addWidget(self.compareTextbox, 2, 1, 1, 2)
        layout.addWidget(self.compareBrowseButton, 2, 3)
        layout.addWidget(self.testRangeLabel, 3, 0)
        layout.addWidget(self.testRangeTextBox, 3, 1)
        layout.addWidget(self.testRangeRadioButton1, 3, 2)
        layout.addWidget(self.testRangeRadioButton2, 3, 3)
        layout.addWidget(self.emptyLabel, 4, 0, 1, 4)
        layout.addWidget(self.emptyLabel, 5, 0)
        layout.addWidget(self.startTestButton, 5, 1)
        layout.addWidget(self.resetButton, 5, 2)
        layout.addWidget(self.closeButton, 5, 3)

        self.setLayout(layout)

    def getTestFiles(self) :
        filePath = QtWidgets.QFileDialog.getOpenFileNames(self, 'Template File', QtCore.QDir.rootPath(), '*.pdf')
        TEST_FILES_LIST = filePath[0]
        #print(filePath)

    def resetWindow(self) :
        self.templateTextBox.setText('')
        self.batchNameTextBox.setText('')
        self.testRangeTextBox.setText('')

    def getTemplateFile(self) :
        filePath = QtWidgets.QFileDialog.getOpenFileName(self, 'Template File', QtCore.QDir.rootPath(), '*.pdf')
        TEMPLATE_FILE_PATH = filePath[0]
        self.templateTextBox.setText(TEMPLATE_FILE_PATH)

    def startTest(self) :
        BATCH_NAME = self.batchNameTextBox.text
        print(BATCH_NAME)
        print(TEMPLATE_FILE_PATH)
        print(TEST_FILES_LIST)

def main() :
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()