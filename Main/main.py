import sys
from PyQt5.QtWidgets import QApplication , QMainWindow , QLabel, QStackedWidget , QWidget , QVBoxLayout , QHBoxLayout , QGridLayout, QLineEdit , QPushButton , QMessageBox , QGridLayout
from PyQt5.QtGui import QIcon   
from PyQt5.QtGui import QFont 
from PyQt5.QtCore import Qt  
from PyQt5.QtGui import QPixmap
import time
import json
from MyRandom.ranT1 import random


class MainWindows(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Enc/Decrypt App")
        self.setGeometry(700, 300, 500, 500)
        self.background_color = "#0D0D0D"
        central = QWidget()
        central.setStyleSheet(f"background-color: {self.background_color};")
        self.setCentralWidget(central)
        self.symbols = list("!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷")
        self.all_buttons()
        self.invalid.setGeometry(210,365 ,100,50)
        self.i = 1
        self.css()
        self.start()
        
    def css(self):
       self.label.setObjectName("title")
       self.e_button.setObjectName("eb")
       self.d_button.setObjectName("db")
       self.back_button.setObjectName("bb")
       self.input_box.setObjectName("ib")
       self.invalid.setObjectName("iv")
       self.enter.setObjectName("et")
       self.clip.setObjectName("Cb")
       self.display.setObjectName("dp")
       self.setStyleSheet("""
        /* ---------- Title ---------- */
        QPushButton#title {
            background-color: rgba(255, 223, 0, 40);
            color: #FFD700;
            border: 3px solid #FFEE55;
            border-radius: 10px;
            padding: 6px 14px;
            font-weight: 700;
            font-size: 13pt;
            letter-spacing: 1px;
        }

        /* ---------- Buttons ---------- */
        QPushButton#eb,
        QPushButton#db,
        QPushButton#bb,
        QPushButton#et,
        QPushButton#Cb {
            background-color: rgba(255, 223, 0, 12);
            color: #FFD700;
            border: 2px solid rgba(255, 223, 0, 90);
            border-radius: 8px;
            padding: 6px 12px;
            font-weight: 600;
        }

        QPushButton#eb:hover,
        QPushButton#db:hover,
        QPushButton#bb:hover,
        QPushButton#et:hover,
        QPushButton#Cb:hover {
            border: 2px solid #FFF176;
            color: #FFF8DC;
        }

        QLineEdit#ib {
            background-color: rgba(255, 223, 0, 8);
            color: #FFD700;
            border: 2px solid #FFD700;
            border-radius: 8px;
            padding: 5px 10px;
            selection-background-color: #FFEE55;
            selection-color: #1a1a1a;
        }

        QLineEdit#ib:hover {
            background-color: rgba(255, 223, 0, 25);
            border: 2px solid #FFEE55;
        }

        QLineEdit#ib:focus {
            border: 2px solid #FFF176;
            background-color: rgba(255, 223, 0, 35);
        }

        QLabel#dp {
            background-color: transparent;
            color: #FFF8DC;
            font-size: 10pt;
            font-style: italic;
        }

    """)


    def all_buttons(self):
        self.label = QPushButton("Welcome to the Enc/Decrypt App", self)
        self.e_button = QPushButton("Encrypt Text",self)
        self.d_button = QPushButton("Decrypt Text",self)
        self.back_button = QPushButton("Go Back",self)
        self.invalid = QLabel("Invalid Data" , self)
        self.input_box = QLineEdit(self)
        self.enter = QPushButton("Enter",self)
        self.clip = QPushButton("Clipboard copy",self)
        self.display = QLabel("", self)
        self.label.hide()
        self.e_button.hide()
        self.d_button.hide()
        self.back_button.hide()
        self.invalid.hide()
        self.input_box.hide()
        self.enter.hide()
        self.clip.hide()
        self.display.hide()
        self.enter.clicked.connect(self.check)
        self.back_button.clicked.connect(self.back_to_main)

    def start(self):
        self.title()
        self.encrypt_tx()
        self.decrypt()

    def title(self):
        self.label.show()
        self.label.setDisabled(True)
        self.label.setGeometry(0, 0, 350, 50) 
        self.label.setGeometry((self.width() - self.label.width()) // 2, 20, self.label.width(), self.label.height())
        self.label.setFont(QFont("Arial", 16, QFont.Bold))

    def encrypt_tx(self):
        self.e_button.show()
        self.e_button.setCheckable(True)
        self.e_button.setGeometry(150,100,200,50)
        self.e_button.setFont(QFont("Arial",17 ,QFont.Bold))
        self.e_button.clicked.connect(self.encrypt_txt)
   

    def decrypt(self):
            self.d_button.show()
            self.d_button.setCheckable(True)
            self.d_button.setGeometry(150,175,200,50)
            self.d_button.setFont(QFont("Arial",17 ,QFont.Bold))
            self.d_button.clicked.connect(self.decrypt_txt)

    def go_back(self):
        self.back_button.show()
        self.back_button.setStyleSheet("font-size: 16px")
        self.back_button.setGeometry(25,400,100,50)
        self.back_button.setFont(QFont("Arial",17 ,QFont.Bold))
        self.back_button.show()

    def coc(self):
        if self.e_button.isChecked():
            QApplication.clipboard().setText(self.clip_e)       
        elif self.d_button.isChecked():
            QApplication.clipboard().setText(self.clip_d)

    def coc_button(self):
        self.clip.show()
        self.clip.setGeometry(150,415,200,50)
        if self.i == 1:
            self.clip.clicked.connect(self.coc)
            self.i += 1
        else:
            pass

    def display_txt(self):
        self.display.show()
        self.display.setGeometry(150,370,200,50)
        self.display.setStyleSheet("font-size: 18px; border: 3px solid #FFEE55;")
        if self.e_button.isChecked():
            self.display.setText(f">>  {self.clip_e} ")
        elif self.d_button.isChecked():
            self.display.setText(f">>  {self.clip_d} ")

        
    def back_to_main(self):
        print("Went Back to Menu")
        self.e_button.blockSignals(False)
        self.d_button.blockSignals(False)
        self.enter.blockSignals(False)
        self.e_button.setChecked(False)
        self.d_button.setChecked(False)
        self.back_button.hide()
        self.input_box.hide()
        self.enter.hide()
        self.clip.hide()
        self.display.hide()
        self.i = 1
        self.file_e = ""
        if self.invalid.isVisible():
           self.invalid.hide()
        else:
            pass

    def Enter(self):
        self.enter.show()
        self.enter.setGeometry(175, 315, 150, 50)
        self.enter.setFont(QFont("Arial", 25 , QFont.Bold))
        self.enter.show()

    def Text_box(self):
            self.input_box.show()
            self.input_box.setPlaceholderText("Enter text to encrypt/decrypt")            
            self.input_box.setGeometry(80, 250, 350, 50)
            self.input_box.setFont(QFont("Arial", 19 , QFont.Bold))
            self.input_box.show()

    def encrypt_txt(self):
            self.e_button.blockSignals(True)
            print("Encrypt button clicked")
            self.e_button.setChecked(True)
            self.Text_box()
            self.Enter()
            self.go_back()


    def effect(self):
        self.eff = ["."] * 5
        for x in self.eff:
           time.sleep(.5)
           print(x,end="")
        print()

    def cipher(self):
        self.box = {self.out:self.cd}
        print(self.box)
        return self.box
    
    def store(self):
        with open("Data/data.json", "r") as file:
            self.data = json.load(file)
            self.data.update(self.box)
            
        with open("Data/data.json","w") as file:
            json.dump(self.data,file,indent=4)
            print("Data successfully added")
     
        return self.data
    
    
    def encrypt_data(self):
        self.oux = []
        for x in self.cd:
            self.oux.append(random.choice(self.symbols))
        self.out = ''.join(self.oux)
        self.effect()
        print(f"your encrypted string is: [  {''.join(self.out)}  ]")
        self.clip_e = ''.join(''.join(self.oux))
        self.coc_button()
        self.display_txt()
        return self.out 
    
    def decrypt_data(self):
        with open("Data/data.json" , "r") as file:
            self.data = json.load(file)
            for self.x in self.data:
                if self.x == self.dp:
                    self.effect()
                    print(f"your decrypted string is:  {self.data[self.x]} ")
                    self.clip_d = self.data[self.x]
                    self.coc_button()
                    self.display_txt()
        return self.clip_d
        

    def check(self):
        self.e_button.blockSignals(True)
        self.d_button.blockSignals(True)
        self.enter.blockSignals(True)
        if self.e_button.isChecked():
            self.cd = self.input_box.text()
            if self.cd == "" or self.cd.isdigit():
                self.invalid.show()
                pass
            else : 
                self.invalid.hide()
                self.encrypt()
                self.input_box.clear()
            return self.cd
        
        elif self.d_button.isChecked():
            self.dp = self.input_box.text()
            if self.dp == "" or self.dp.isdigit():
                self.invalid.show()
                pass
            else : 
               self.invalid.hide()
               self.decrypt_data()
               self.input_box.clear()
            return self.dp , 


    def encrypt(self):
            self.invalid.hide()
            try:
                with open("Data/data.json" , "r") as file:
                    if self.cd in json.load(file).values(): 
                        print("the encrypted version already exist")
                    else:
                        self.out = self.encrypt_data()
                        self.box = self.cipher()
                        self.data = self.store()
            except FileNotFoundError:
                with open("Data/data.json", "w",) as file:
                    file.write("{}")
                with open("Data/data.json" , "r") as file:
                    if self.cd in json.load(file).values(): 
                        print("the encrypted version already exist")
                        pass
                    else:
                        self.out = self.encrypt_data()
                        self.box = self.cipher()
                        self.data = self.store()

    def decrypt_txt(self):
        self.d_button.blockSignals(True)
        self.d_button.setChecked(True) 
        self.Text_box()
        self.Enter()
        self.go_back()



def main():
    app = QApplication(sys.argv)
    window = MainWindows()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
