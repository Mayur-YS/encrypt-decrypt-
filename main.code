
import time
import random

def effect():
    eff = ["."] * 5
    for x in eff:
        time.sleep(.5)
        print(x,end="")
    print()

def cipher(cd , out):
    box = {out:cd}
    return box

def encrypt(cd):
    oux = []
    for ch in cd:
        oux.append(random.choice(symbols))
    out = ''.join(oux)
    effect()
    print(f"your encrypted string is: [  {''.join(out)}  ]")
    return out


def decrypt(dp):
    for x in range(len(store)):
        verify = ''.join(store[x].keys())
        if verify == dp:
            effect()
            print(f"your decrypted string is:  {''.join(store[x].values())} ")
        if dp.isalpha:
            print("invalid string")

store = []

run = True

print("**********************")
print("Welcome to Encrypting")
while run:
        print("**********************")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3: Quit")
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
            out = encrypt(cd)
            box = cipher(cd, out)
            store.append(box)
        if choice == 2:
                dp = input("enter ur statement to decrypt:")
                decrypt(dp)
        if choice == 3:
            break










