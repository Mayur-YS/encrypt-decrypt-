# encrypt-decrypt-
🔐 Python Encryption & Decryption Tool

A simple Python-based encryption and decryption program that converts text into a randomly generated sequence of symbols and stores the encrypted/decrypted pairs temporarily while the program is running.

This project was created as a beginner-friendly Python project to practice functions, lists, dictionaries, loops, conditionals, user input, randomness, and basic data storage.

⚠️ Note: This is an educational project and is not a secure encryption system for protecting real passwords or sensitive information.

✨ Features
🔒 Encrypt text using randomly selected symbols
🔓 Decrypt previously encrypted text
🎲 Random symbol generation
💾 Temporarily stores encrypted/decrypted pairs
⏳ Loading-style effect during encryption/decryption
🖥️ Simple command-line interface
🚪 Option to quit the program
🛠️ Technologies Used
Python 3
random — for randomly selecting encryption symbols
time — for creating the loading effect

No external libraries are required.

📂 How It Works
1. Encryption

When you choose Encrypt, the program:

Takes your input text.
Generates a random symbol for each character.
Creates an encrypted string.
Stores the encrypted string together with the original text.
Displays the encrypted result.

Example:

Enter your choice: 1

Enter ur statement to encrypt: hello

your encrypted string is: [  @#×!$  ]

The encrypted text is then stored temporarily in the program.

2. Decryption

When you choose Decrypt, you enter the encrypted string.

The program searches through the stored encryption pairs and checks whether the encrypted string exists.

If it finds a match, it displays the original text.

Example:

Enter your choice: 2

Enter ur statement to decrypt: @#×!$

your decrypted string is: hello
📋 Menu

The program provides three options:

**********************
Welcome to Encrypting
**********************
1. Encrypt
2. Decrypt
3. Quit
Option 1 — Encrypt 🔒

Enter a statement and receive a randomly generated encrypted string.

Option 2 — Decrypt 🔓

Enter an encrypted string that was generated earlier to recover the original text.

Option 3 — Quit 🚪

Stops the program.

💾 Data Storage

Currently, the program stores encryption pairs inside a Python list:

store = []

Each encryption is stored as a dictionary:

{
    encrypted_text: original_text
}

For example:

{
    "@#×!$": "hello"
}
Important

The stored data exists only while the Python program is running.

If you close the program, the stored encryption pairs are lost.

▶️ How to Run
1. Install Python

Make sure Python 3 is installed on your computer.

You can check using:

python --version
2. Clone the repository
git clone YOUR_REPOSITORY_URL
3. Open the project folder
cd YOUR_REPOSITORY_FOLDER
4. Run the program
python main.py
📁 Project Structure
Encryption-Project/
│
├── main.py
└── README.md
🧠 Python Concepts Practiced

This project helped practice:

Functions
if / elif / else
while loops
for loops
Lists
Dictionaries
Strings
input()
Type conversion
random.choice()
time.sleep()
.append()
.join()
.isdigit()
len()
Basic program flow
⚠️ Limitations

This project is mainly for learning Python and has some limitations:

Encryption pairs are stored only in memory.
Closing the program deletes the stored data.
The encryption method is not cryptographically secure.
Random symbols can potentially repeat.
The program currently does not use modern encryption algorithms such as AES or RSA.
Decryption only works for encrypted strings stored during the current session.
🚀 Future Improvements

Possible improvements for future versions:

Save encrypted data to a file

Add permanent storage using JSON

Improve the encryption algorithm

Add password protection

Add a GUI

Add error handling

Allow users to manage multiple encrypted messages

Add secure encryption algorithms

Improve the loading animation

Add timestamps for stored messages

🎯 Purpose

The main purpose of this project is to learn and practice Python programming by building something interactive rather than just writing individual practice programs.

It demonstrates how multiple basic Python concepts can be combined to create a functional command-line application.

👨‍💻 Author

Mayur Shirodkar

📜 License

This project is intended for educational and learning purposes.
