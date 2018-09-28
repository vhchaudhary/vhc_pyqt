import pdb

from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidget, QTableWidgetItem

from tw_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    _row = 0

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.btninsert.pressed.connect(lambda : self.insert_data(self.txtname.text(), self.txtcity.text(),
                                                                 'M' if self.radioMale.isChecked() else 'F'))

        self.show()

    def insert_data(self, name, city, gender):
        self.tw_display.insertRow(self._row)

        self.tw_display.setItem(self._row, 0, QTableWidgetItem(name))
        self.tw_display.setItem(self._row, 1, QTableWidgetItem(city))
        self.tw_display.setItem(self._row, 2, QTableWidgetItem(gender))

        self._row += 1


if __name__ == '__main__':
    app = QApplication([])
    app.setApplicationName('TW_Test')

    window = MainWindow()
    app.exec()