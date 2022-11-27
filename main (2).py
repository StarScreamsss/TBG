import sys
import random
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer, QTime


class Window(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('TBGProject.ui', self)
        self.operation = str()
        self.init_ui()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        self.setFixedSize(self.size())

    def init_ui(self):
        self.pushButton.clicked.connect(self.found_game)
        self.pushButton_2.clicked.connect(self.found_random)
        self.pushButton_3.clicked.connect(self.add_game)

# поиск игры
    def found_game(self):
        self.listWidget.clear()
        dbg = sqlite3.connect('base_of_games.db')
        cursor = dbg.cursor()
        if self.radioButton.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
              FROM games
             WHERE genre = 'хоррор' AND
                   style = 'одиночный' AND
                   platform = 'пк';
                   """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(i[0])
            dbg.close()
        elif self.radioButton.isChecked() and self.radioButton_8.isChecked()\
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
              FROM games
             WHERE genre = 'хоррор' AND 
                    style = 'одиночный' AND 
                    platform = 'телефон';
            """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton.isChecked() and self.radioButton_7.isChecked()\
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
              FROM games
             WHERE genre = 'хоррор' AND 
                    style = 'сетевой' AND 
                    platform = 'пк';
            """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton.isChecked() and self.radioButton_7.isChecked()\
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
              FROM games
             WHERE genre = 'хоррор' AND 
                    style = 'сетевой' AND 
                    platform = 'телефон';
            """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_2.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
                              FROM games
                             WHERE genre = 'стратегия' AND
                                    style = 'одиночный' AND
                                    platform = 'пк';
                            """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_2.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
                  FROM games
                 WHERE genre = 'стратегия' AND
                        style = 'одиночный' AND
                        platform = 'телефон';
                """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_2.isChecked() and self.radioButton_7.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
                  FROM games
                 WHERE genre = 'стратегия' AND
                        style = 'сетевой' AND
                        platform = 'пк';
                """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_2.isChecked() and self.radioButton_7.isChecked() \
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
                  FROM games
                 WHERE genre = 'стратегия' AND
                        style = 'сетевой' AND
                        platform = 'телефон';
                """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_3.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
                                  FROM games
                                 WHERE genre = 'шутер' AND
                                        style = 'одиночный' AND
                                        platform = 'пк';
                                """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_3.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
                      FROM games
                     WHERE genre = 'шутер' AND
                            style = 'одиночный' AND
                            platform = 'телефон';
                    """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_3.isChecked() and self.radioButton_7.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
                      FROM games
                     WHERE genre = 'шутер' AND
                            style = 'сетевой' AND
                            platform = 'пк';
                    """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_3.isChecked() and self.radioButton_7.isChecked() \
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
                      FROM games
                     WHERE genre = 'шутер' AND
                            style = 'сетевой' AND
                            platform = 'телефон';
                    """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_4.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
                                      FROM games
                                     WHERE genre = 'гонка' AND
                                            style = 'одиночный' AND
                                            platform = 'пк';
                                    """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_4.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
                          FROM games
                         WHERE genre = 'гонка' AND
                                style = 'одиночный' AND
                                platform = 'телефон';
                        """).fetchall()
            dbg.commit()
            for i in result[::-1]:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_4.isChecked() and self.radioButton_7.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
                          FROM games
                         WHERE genre = 'гонка' AND
                                style = 'сетевой' AND
                                platform = 'пк';
                        """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_4.isChecked() and self.radioButton_7.isChecked() \
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
                          FROM games
                         WHERE genre = 'гонка' AND
                                style = 'сетевой' AND
                                platform = 'телефон';
                        """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_5.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
  FROM games
 WHERE genre = 'файтинг' AND
       style = 'одиночный' AND
       platform = 'пк';

                                        """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_5.isChecked() and self.radioButton_8.isChecked() \
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
                              FROM games
                             WHERE genre = 'файтинг' AND
                                    style = 'одиночный' AND
                                    platform = 'телефон';
                            """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_5.isChecked() and self.radioButton_7.isChecked() \
                and self.radioButton_12.isChecked():
            result = cursor.execute("""SELECT title
                              FROM games
                             WHERE genre = 'файтинг' AND
                                    style = 'сетевой' AND
                                    platform = 'пк';
                            """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()
        elif self.radioButton_5.isChecked() and self.radioButton_7.isChecked() \
                and self.radioButton_13.isChecked():
            result = cursor.execute("""SELECT title
                              FROM games
                             WHERE genre = 'файтинг' AND
                                    style = 'сетевой' AND
                                    platform = 'телефон';
                            """)
            dbg.commit()
            for i in result:
                self.listWidget.addItem(str(i[0]))
            dbg.close()

    # находит рандомную игру из файла
    def found_random(self):
        self.lineEdit.setText(random.choice(list(open('dict_of_games_copy.txt'))))

    # выводит время
    def showTime(self):
        current_time = QTime.currentTime()
        label_time = current_time.toString('hh:mm:ss')
        self.label_9.setText(label_time)
        self.label_6.setText(label_time)

    # добавление игры
    def add_game(self):
        dbg = sqlite3.connect('base_of_games.db')
        cursor = dbg.cursor()
        if self.radioButton_6.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'хоррор', 'одиночный', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_6.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'хоррор', 'одиночный', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_6.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'хоррор', 'сетевой', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_6.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'хоррор', 'сетевой', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_9.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'стратегия', 'одиночный', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_9.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'стратегия', 'одиночный', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_9.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'стратегия', 'сетевой', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_9.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'стратегия', 'сетевой', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_10.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'шутер', 'одиночный', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_10.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'шутер', 'одиночный', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_10.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'шутер', 'сетевой', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_10.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'шутер', 'сетевой', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_11.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'гонка', 'одиночный', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_11.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'гонка', 'одиночный', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_11.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'гонка', 'сетевой', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_11.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'гонка', 'сетевой', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_14.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'файтинг', 'одиночный', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_14.isChecked() and self.radioButton_16.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'файтинг', 'одиночный', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_14.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_17.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'файтинг', 'сетевой', 'пк'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')
        elif self.radioButton_14.isChecked() and self.radioButton_15.isChecked() \
                and self.radioButton_18.isChecked():
            if cursor.fetchone() is None:
                cursor.execute("INSERT INTO games VALUES(?, ?, ?, ?);",
                               (self.lineEdit_2.text(), 'файтинг', 'сетевой', 'телефон'))
                dbg.commit()
            dbg.close()
            self.label_14.setText(f'Игра "{self.lineEdit_2.text()}" успешно добавлена')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    exe = Window()
    exe.show()
    sys.exit(app.exec())
