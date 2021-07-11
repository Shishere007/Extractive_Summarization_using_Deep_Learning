from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QDir
from pathlib import Path
import sys

import Summarizer

__name__ = "SummarizerGUI"


class Ui_MainWindow(object):
    def __init__(self) -> None:
        self.selected_files = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(987, 800)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 991, 841))
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setObjectName("tabWidget")
        self.single_tab = QtWidgets.QWidget()
        self.single_tab.setObjectName("single_tab")
        self.label_heading = QtWidgets.QLabel(self.single_tab)
        self.label_heading.setGeometry(QtCore.QRect(230, 0, 521, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading.setFont(font)
        self.label_heading.setTextFormat(QtCore.Qt.PlainText)
        self.label_heading.setObjectName("label_heading")
        self.label_summary = QtWidgets.QLabel(self.single_tab)
        self.label_summary.setGeometry(QtCore.QRect(500, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_summary.setFont(font)
        self.label_summary.setObjectName("label_summary")
        self.FileName_lineEdit = QtWidgets.QLineEdit(self.single_tab)
        self.FileName_lineEdit.setGeometry(QtCore.QRect(40, 100, 331, 31))
        self.FileName_lineEdit.setText("")
        self.FileName_lineEdit.setObjectName("FileName_lineEdit")
        self.Button_Generate = QtWidgets.QPushButton(self.single_tab, clicked=self.clickGenerate)  # invoking generate function
        # self.Button_Generate = QtWidgets.QPushButton(self.single_tab, clicked=lambda: self.clickGenerate())  # invoking generate function
        self.Button_Generate.setGeometry(QtCore.QRect(700, 70, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Generate.setFont(font)
        self.Button_Generate.setObjectName("Button_Generate")
        self.textEdit_input = QtWidgets.QTextEdit(self.single_tab)
        self.textEdit_input.setGeometry(QtCore.QRect(40, 170, 431, 551))
        self.textEdit_input.setObjectName("textEdit_input")
        self.textEdit_output = QtWidgets.QTextEdit(self.single_tab)
        self.textEdit_output.setGeometry(QtCore.QRect(500, 170, 431, 501))
        self.textEdit_output.setObjectName("textEdit_output")
        self.label_browse = QtWidgets.QLabel(self.single_tab)
        self.label_browse.setGeometry(QtCore.QRect(40, 70, 361, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_browse.setFont(font)
        self.label_browse.setObjectName("label_browse")
        self.Button_SaveTXT = QtWidgets.QPushButton(self.single_tab, clicked=lambda: self.clickSaveTXT())  # invoking savetext function
        self.Button_SaveTXT.setGeometry(QtCore.QRect(720, 690, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Button_SaveTXT.setFont(font)
        self.Button_SaveTXT.setObjectName("Button_SaveTXT")
        self.label_input = QtWidgets.QLabel(self.single_tab)
        self.label_input.setGeometry(QtCore.QRect(40, 140, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_input.setFont(font)
        self.label_input.setObjectName("label_input")
        self.Button_Browse = QtWidgets.QPushButton(self.single_tab, clicked=lambda: self.clickBrowse())  # invoking browse function
        self.Button_Browse.setGeometry(QtCore.QRect(380, 100, 91, 31))
        self.Button_Browse.setObjectName("Button_Browse")
        self.tabWidget.addTab(self.single_tab, "")
        self.multiple_tab = QtWidgets.QWidget()
        self.multiple_tab.setObjectName("multiple_tab")
        self.label_heading_2 = QtWidgets.QLabel(self.multiple_tab)
        self.label_heading_2.setGeometry(QtCore.QRect(240, 100, 531, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label_heading_2.setFont(font)
        self.label_heading_2.setTextFormat(QtCore.Qt.PlainText)
        self.label_heading_2.setObjectName("label_heading_2")
        self.label_browse_2 = QtWidgets.QLabel(self.multiple_tab)
        self.label_browse_2.setGeometry(QtCore.QRect(40, 230, 411, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.label_browse_2.setFont(font)
        self.label_browse_2.setObjectName("label_browse_2")
        # invoking browse function (Multiple Files)
        self.Button_Browse_2 = QtWidgets.QPushButton(self.multiple_tab, clicked=lambda: self.clickBrowse2())
        self.Button_Browse_2.setGeometry(QtCore.QRect(40, 310, 151, 51))
        self.Button_Browse_2.setObjectName("Button_Browse_2")
        # invoking generate function (Multiple FIles)
        self.Button_Generate_2 = QtWidgets.QPushButton(self.multiple_tab, clicked=lambda: self.clickGenerate2())
        self.Button_Generate_2.setGeometry(QtCore.QRect(690, 250, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Button_Generate_2.setFont(font)
        self.Button_Generate_2.setObjectName("Button_Generate_2")
        self.textEdit_output_2 = QtWidgets.QTextEdit(self.multiple_tab)
        self.textEdit_output_2.setGeometry(QtCore.QRect(40, 420, 901, 221))
        self.textEdit_output_2.setObjectName("textEdit_output_2")
        self.tabWidget.addTab(self.multiple_tab, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # Function that defines the browse function      (Single File)
    def clickBrowse(self):
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setFilter(QDir.Files)

        if dialog.exec_():
            file_name = dialog.selectedFiles()
            self.selected_files = file_name.copy()
            try:
                self.textEdit_input.setText(open(file_name[0], 'r', encoding='utf-8').read())
                self.FileName_lineEdit.setText(file_name[0])
            except Exception:
                print("UNSOPPORTED FILE")

    # Function to generate summary         (Single File)
    def clickGenerate(self):
        if self.selected_files:
            summary = Summarizer.executeForAFile(self.selected_files[0])
            self.textEdit_output.setText(summary)
            self.summarized_text_single_file = summary

    # Function to save generated summary to a text file         (Single File)
    def clickSaveTXT(self):
        mytext = self.textEdit_output.toPlainText()
        if self.selected_files and mytext:
            out_folder = QFileDialog.getExistingDirectory(None, "Select Output Folder")
            if out_folder:
                filename = Path(self.selected_files[0]).name
                if filename.endswith('.txt'):
                    out_file = out_folder + "/" + filename.replace(".txt",'_summary.txt')
                else:
                    out_file = out_folder + "/" + filename + "_summary"
                open(out_file, 'w',encoding='utf-8').write(mytext)

    # Function that defines the browse function      (Multiple Files)
    def clickBrowse2(self):
        filenames, _ = QFileDialog.getOpenFileNames(None,"QFileDialog.getOpenFileNames()","","All Files (*);;Python Files (*.py);;Text Files (*.txt)",)
        if filenames: # chnage this
            self.selected_files = filenames.copy()

    # Function to generate summary         (Multiple Files)
    def clickGenerate2(self):
        if self.selected_files:
            out_folder = QFileDialog.getExistingDirectory(None, "Select Output Folder")
            if out_folder:
                out_files = ["Files Generated"]
                for file in self.selected_files:
                    print(f"Generating Summary -> {file}")
                    summary = Summarizer.executeForAFile(file)
                    filename = Path(file).name
                    if filename.endswith('.txt'):
                        out_file = out_folder + "/" + filename.replace(".txt",'_summary.txt')
                    else:
                        out_file = out_folder + "/" + filename + "_summary"
                    out_files.append(out_file)
                    open(out_file,'w',encoding='utf-8').write(summary)
                out_files.append("Summary Generation Finished")
                self.textEdit_output_2.setText("\n".join(out_files))
                print(f"Summary Saved to -> {out_file}")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Summary Generator DL"))
        self.label_heading.setText(_translate("MainWindow", "Text Summarization using Deep Learning"))
        self.label_summary.setText(_translate("MainWindow", "Summary"))
        self.Button_Generate.setText(_translate("MainWindow", "Generate"))
        self.label_browse.setText(_translate("MainWindow", "Open the file for which the summary has to be generated"))
        self.Button_SaveTXT.setText(_translate("MainWindow", "Save as Text"))
        self.label_input.setText(_translate("MainWindow", "Input Document"))
        self.Button_Browse.setText(_translate("MainWindow", "Browse"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.single_tab), _translate("MainWindow", "Single File"))
        self.label_heading_2.setText(_translate("MainWindow", "Text Summarization using Deep Learning"))
        self.label_browse_2.setText(_translate("MainWindow", "Open the files for which the summary has to be generated"))
        self.Button_Browse_2.setText(_translate("MainWindow", "Browse"))
        self.Button_Generate_2.setText(_translate("MainWindow", "Generate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.multiple_tab), _translate("MainWindow", "Multiple Files"))


def start():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "SummarizerGUI":
    pass