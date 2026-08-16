
import time
import json
from MyRandom.ranT1 import random

def effect():
    eff = ["."] * 5
    for x in eff:
        time.sleep(.5)
        print(x,end="")
    print()

def cipher(cd , out):
    box = {out:cd}
    return box

def store():

    with open("Data/data.json", "r") as file:
        data = json.load(file)
        data.update(box)
            
    with open("Data/data.json","w") as file:
        json.dump(data,file,indent=4)
        print("Data successfully added")
     
    return data    
    

def encrypt(cd):
    oux = []
    for ch in cd:
        oux.append(random.choice(symbols))
    out = ''.join(oux)
    effect()
    print(f"your encrypted string is: [  {''.join(out)}  ]")
    return out
   
        
def decrypt(dp):
    with open("Data/data.json" , "r") as file:
        data = json.load(file)
        for x in data:
            if x == dp:
                effect()
                print(f"your decrypted string is:  {data[x]} ")
 

run = True

print("**********************")
print("Welcome to Encrypting")
while run:
        print("**********************")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3: clear data")
        print("4: Quit")
        choice = input("enter your choice:")
        if not choice.isdigit():
            print("****invalid choice****")
            continue
        choice = int(choice)

        if choice == 1:
            cd = input("enter ur statement to encrypt:")
            symbols = list("!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷!@#$%^&*()-_=+[{]};:',<.>/?~|`«»±×÷")
            if len(cd) > len(symbols):
                for x in range(0, 10):
                    symbols.append(x)
            try:
                with open("Data/data.json" , "r") as file:
                    if cd in json.load(file).values(): 
                        print("the encrypted version already exist")
                        continue
                    else:
                        out = encrypt(cd)
                        box = cipher(cd, out)
                        data = store()
            except FileNotFoundError:
                with open("Data/data.json", "w",) as file:
                    file.write("{}")
                with open("Data/data.json" , "r") as file:
                    if cd in json.load(file).values(): 
                        print("the encrypted version already exist")
                        continue
                    else:
                        out = encrypt(cd)
                        box = cipher(cd, out)
                        data = store()
                 
                                
        elif choice == 2:
                dp = input("enter ur statement to decrypt:")
                decrypt(dp)
        elif choice == 3:
            with open("Data/data.json" , "r") as file:
                cl = json.load(file)
                cl.clear()
                
            with open("Data/data.json" , "w") as file: 
                json.dump(cl , file,indent=4)
                print("**data cleared**")
        elif choice == 4:
            break
               
            
        








