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
        self.setStyleSheet(f"background-color: {self.background_color};")
        self.symbols = list("!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷")
        self.invalid = QLabel("Invalid Data" , self)
        self.invalid.setGeometry(210,365 ,100,50)
        self.invalid.setStyleSheet("background-color:#0D0D0D ; color: #FFDF00;")
        self.invalid.hide()
        self.start()
        

    def start(self):
        self.title()
        self.encrypt_tx()
        self.decrypt()

    def title(self):
        self.label = QPushButton("Welcome to the Enc/Decrypt App", self)
        self.label.setDisabled(True)
        self.label.setStyleSheet("background-color: transparent; border: none;")
        self.label.setGeometry(0, 0, 350, 50) 
        self.label.setGeometry((self.width() - self.label.width()) // 2, 20, self.label.width(), self.label.height())
        self.label.setFont(QFont("Arial", 16, QFont.Bold))
        self.label.setStyleSheet("color: #FFDF00;")

    def encrypt_tx(self):
        self.e_button = QPushButton("Encrypt Text",self)
        self.e_button.setCheckable(True)
        self.e_button.setGeometry(150,100,200,50)
        self.e_button.setFont(QFont("Arial",17 ,QFont.Bold))
        self.e_button.setStyleSheet("background-color: #1E1E1E; color: #FFDF00; border-radius: 5px;")
        self.e_button.clicked.connect(self.encrypt_txt)
   

    def decrypt(self):
            self.d_button = QPushButton("Decrypt Text",self)
            self.d_button.setCheckable(True)
            self.d_button.setGeometry(150,175,200,50)
            self.d_button.setFont(QFont("Arial",17 ,QFont.Bold))
            self.d_button.setStyleSheet("background-color: #1E1E1E; color: #FFDF00; border-radius: 5px;")
            self.d_button.clicked.connect(self.decrypt_txt)

    def go_back(self):
        self.back_button = QPushButton("Go Back",self)
        self.back_button.setGeometry(25,400,100,50)
        self.back_button.setFont(QFont("Arial",17 ,QFont.Bold))
        self.back_button.setStyleSheet("background-color: #1E1E1E; color: #FFDF00; border-radius: 5px;")
        self.back_button.show()
        self.back_button.clicked.connect(self.back_to_main)
        
    def back_to_main(self):
        print("Went Back to Menu")
        self.e_button.setDisabled(False)
        self.d_button.setDisabled(False)
        self.e_button.setChecked(False)
        self.d_button.setChecked(False)
        self.back_button.hide()
        self.input_box.hide()
        self.enter.hide()
        if self.invalid.isVisible():
           self.invalid.hide()
        else:
            pass

    def Enter(self):
        self.enter = QPushButton("Enter",self)
        self.enter.setGeometry(175, 315, 150, 50)
        self.enter.setStyleSheet("background-color: #FFFFFF; color: #000000; border-radius: 5px; padding: 5px;")
        self.enter.setFont(QFont("Arial", 25 , QFont.Bold))
        self.enter.setStyleSheet("color: #FFDF00;")
        self.enter.show()
        self.enter.clicked.connect(self.check)

    def Text_box(self):
            self.input_box = QLineEdit(self)
            self.input_box.setPlaceholderText("Enter text to encrypt/decrypt")            
            self.input_box.setGeometry(80, 250, 350, 50)
            self.input_box.setStyleSheet("background-color: #FFFFFF; color: #000000; border-radius: 10px; padding: 5px; border: 10px solid #FFDF00; border-width: 2px; border-style: solid;")
            self.input_box.setFont(QFont("Arial", 19 , QFont.Bold))
            self.input_box.setStyleSheet("color: #FFDF00;")
            self.input_box.show()

    def encrypt_txt(self):
            print("Encrypt button clicked")
            self.e_button.setDisabled(True)
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
        return self.out

    def decrypt_data(self):
        with open("Data/data.json" , "r") as file:
            self.data = json.load(file)
            for x in self.data:
                if x == self.dp:
                    self.effect()
                    print(f"your decrypted string is:  {self.data[x]} ")


    def check(self):
        if self.e_button.isChecked():
            self.cd = self.input_box.text()
            if self.cd == "" or self.cd.isdigit():
                self.invalid.show()
                pass
            else : 
                self.encrypt()
            return self.cd
        
        elif self.d_button.isChecked():
            self.dp = self.input_box.text()
            if self.dp == "" or self.dp.isdigit():
                self.invalid.show()
                pass
            else : 
               self.decrypt_data()
            return self.dp


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
        self.d_button.setDisabled(True)
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
