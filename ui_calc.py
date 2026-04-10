from PySide6.QtCore import (QCoreApplication, QRect, QMetaObject, Qt)
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QStatusBar, QWidget)

import urllib.request
import json

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(797, 600)

        self.centralwidget = QWidget(MainWindow)

        self.numberoutput = QLabel(self.centralwidget)
        self.numberoutput.setGeometry(QRect(20, 20, 391, 81))
        font = QFont()
        font.setPointSize(26)
        self.numberoutput.setFont(font)
        self.numberoutput.setFrameShape(QFrame.Shape.Box)
        self.numberoutput.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.ai_enswer = QLabel(self.centralwidget)
        self.ai_enswer.setGeometry(QRect(430, 30, 331, 521))
        font1 = QFont()
        font1.setPointSize(14)
        font1.setBold(True)
        self.ai_enswer.setFont(font1)
        self.ai_enswer.setFrameShape(QFrame.Shape.Box)
        self.ai_enswer.setWordWrap(True)

        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)

        positions = [
            (20,230,"1"), (130,230,"2"), (230,230,"3"),
            (20,300,"4"), (130,300,"5"), (230,300,"6"),
            (20,370,"7"), (130,370,"8"), (230,370,"9"),
        ]

        self.buttons = []
        for x,y,text in positions:
            btn = QPushButton(text, self.centralwidget)
            btn.setGeometry(QRect(x,y,81,51))
            btn.setFont(font2)
            btn.clicked.connect(lambda _, t=text: self.press_it(t))
            self.buttons.append(btn)

        self.zero = QPushButton("0", self.centralwidget)
        self.zero.setGeometry(QRect(130, 440, 81, 51))
        self.zero.setFont(font2)
        self.zero.clicked.connect(lambda: self.press_it("0"))

        self.plus = QPushButton("+", self.centralwidget)
        self.plus.setGeometry(QRect(330, 230, 81, 51))
        self.plus.setFont(font2)
        self.plus.clicked.connect(lambda: self.press_it("+"))

        self.moin = QPushButton("-", self.centralwidget)
        self.moin.setGeometry(QRect(330, 300, 81, 51))
        self.moin.setFont(font2)
        self.moin.clicked.connect(lambda: self.press_it("-"))

        self.fois = QPushButton("*", self.centralwidget)
        self.fois.setGeometry(QRect(330, 370, 81, 51))
        self.fois.setFont(font2)
        self.fois.clicked.connect(lambda: self.press_it("*"))

        self.division = QPushButton("/", self.centralwidget)
        self.division.setGeometry(QRect(330, 160, 81, 51))
        self.division.setFont(font2)
        self.division.clicked.connect(lambda: self.press_it("/"))

        self.egale = QPushButton("=", self.centralwidget)
        self.egale.setGeometry(QRect(230, 440, 81, 51))
        self.egale.setFont(font2)
        self.egale.clicked.connect(self.calculate)

        self.clear = QPushButton("C", self.centralwidget)
        self.clear.setGeometry(QRect(20, 160, 81, 51))
        self.clear.setFont(font2)
        self.clear.clicked.connect(lambda: self.numberoutput.setText("0"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QMenuBar(MainWindow)
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QStatusBar(MainWindow)
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QMetaObject.connectSlotsByName(MainWindow)

    def press_it(self, pressed):
        current = self.numberoutput.text()
        if current == "0":
            self.numberoutput.setText(pressed)
        else:
            self.numberoutput.setText(current + pressed)

    def calculate(self):
        try:
            expression = self.numberoutput.text()
            result = eval(expression)
            self.numberoutput.setText(str(result))
            self.ask_ai(expression)
        except:
            self.numberoutput.setText("Erreur")

    def ask_ai(self, expression):
        try:
            url = "http://localhost:11434/api/chat"

            data = {
                "model": "qwen2:0.5b",
                "messages": [
                    {"role": "user", "content": f"Explique simplement ce calcul : {expression}"}
                ],
                "stream": False
            }

            req = urllib.request.Request(
                url,
                data=json.dumps(data).encode("utf-8"),
                headers={"Content-Type": "application/json"}
            )

            response = urllib.request.urlopen(req)
            result = json.loads(response.read().decode())

            ai_text = result["message"]["content"]
            self.ai_enswer.setText(ai_text)

        except Exception as e:
            self.ai_enswer.setText("Erreur IA")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("CALCULATRICE_PRO_MAX")
        self.numberoutput.setText("0")
        self.ai_enswer.setText("AI ready")


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())