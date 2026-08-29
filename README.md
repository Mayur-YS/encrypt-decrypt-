# encrypt-decrypt-

🔐 Simple Python Encryption & Decryption (educational)

This is a beginner-friendly command-line program that "encrypts" text by replacing each character with a randomly selected symbol and stores the mapping so the program can decrypt it later. This proje[...] 

---
Reworked the QSS (Qt Style Sheets) styling with:
✅ A gold/amber gradient theme for a more premium feel
✅ Proper hover, pressed, and disabled states on buttons (not just flat colors)
✅ Focus states on input fields for better UX feedback
✅ Custom-styled scrollbars and tooltips to keep things consistent
✅ Subtle depth using layered rgba backgrounds instead of flat transparency

## What changed (updated to match the code)
- Persistently stores encryption pairs in `Data/data.json` (created automatically if missing).
- Added a "Clear data" option to wipe stored pairs.
- The CLI menu has 4 options: Encrypt, Decrypt, Clear data, Quit.
- Uses a custom time-based random implementation located at `Main/MyRandom/ranT1.py`.
- Minor user-facing formatting: encryption output prints with square brackets for display, but the stored key is the raw generated string (without the display brackets).

---

## Features
- Encrypt an input string into a randomly generated symbol sequence.
- Decrypt previously generated encrypted strings (must match stored encrypted string exactly).
- Save and load encrypted ↔ original mappings from `Data/data.json`.
- Loading-style animation during encryption/decryption.
- Lightweight: no external dependencies (Python 3 standard library only).

---

## How it works (high level)
1. Encryption:
   - For each character in the input, the program picks a symbol from a symbol list using `MyRandom.ranT1.random.choice`.
   - The program joins chosen symbols into an encrypted string (this string is stored as the key and the original text as the value in `Data/data.json`).
   - The encrypted string is shown to the user (displayed inside square brackets for readability).

2. Decryption:
   - You enter the encrypted string (exactly as the stored key — do not include the display brackets/spaces).
   - The program looks up the encrypted string in `Data/data.json` and prints the original text if found.

---

## CLI Menu
When you run the program, you will see:
```
**********************
Welcome to Encrypting
**********************
1. Encrypt
2. Decrypt
3. clear data
4. Quit
```

- Option 1 — Encrypt: enter a statement to encrypt and save the pair.
- Option 2 — Decrypt: enter an encrypted string (the stored key) to recover the original text.
- Option 3 — Clear data: removes all mappings from `Data/data.json`.
- Option 4 — Quit: exit the program.

---

## Example session
1) Encrypt:
- Input: hello
- Output shown: your encrypted string is: [  @#×!$  ]
- Stored mapping: `{"@#×!$": "hello"}` inside `Data/data.json`

2) Decrypt:
- Input (exact stored key): @#×!$
- Output: your decrypted string is: hello

Note: the printed display includes brackets and spacing for readability; when decrypting, enter the raw encrypted string (without the visible brackets/spaces).

---

## Files & structure
- Main/main.py — main GUI application (PyQt5) and the UI styling (object-name based stylesheet).
- Main/MyRandom/ranT1.py — custom random.choice implementation
- Data/data.json — persistent storage (created automatically)
- README.md — this file

---

## How to run
1. Ensure Python 3 is installed:
   python --version

2. Install PyQt5 if you are using the GUI build (required for `Main/main.py`):
   python -m pip install PyQt5

3. Run the script from the repository root:
   python Main/main.py

---

## Data format
Data is stored as a JSON object mapping encrypted strings to original text:
```json
{
  "encrypted_string_here": "original text here",
  "@#×!$": "hello"
}
```

---

## Known issues & suggestions
- Security: This is NOT cryptographically secure. Do not use it for real passwords or sensitive information.
- Bug risk: In the code, when the input length is larger than the symbol list, integers (0–9) are appended to the symbol list as Python ints. That can cause TypeError when the program tries to [...]
  - Append string digits instead (e.g., `symbols.extend(list("0123456789"))`) or expand the symbol set with only string elements.
  - Prefer using Python's built-in `random.choice` from the `random` module (and remove the custom time-based random) for more consistent behavior.
- Decrypt input: The program prints the encrypted string with square brackets and spaces for readability; users must input the raw stored key (without brackets/spaces) to decrypt.
- Duplicate checking: The code checks whether the original text already exists in saved values before encrypting; this prevents duplicate originals but does not prevent duplicate encrypted output[...] 
- Improvements you might consider:
  - Use built-in `random` or `secrets` for randomness.
  - Always use strings in the symbols list.
  - Add unit tests, better error handling, and option to remove individual entries.
  - Optionally add password protection or adopt real encryption (AES) for secure use-cases.

---

## Contributing
This repository is a learning project. Contributions are welcome — consider opening issues or pull requests for bug fixes (especially the int-vs-str bug) and small improvements.

---

## License & Author
Author: Mayur Shirodkar

This project is intended for learning; no license file is included in the repository. Add a LICENSE to clarify reuse terms if needed.
