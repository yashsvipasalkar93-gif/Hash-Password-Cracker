# Hash-Password-Cracker

## What This Project Does
This project has two Python scripts built to demonstrate how password hashing and password cracking work:

1. **Hash Generator** – Takes a plain text password and converts it into a hash (a scrambled, one-way version of the password), similar to how real systems store passwords.
2. **Password Cracker (GUI)** – Uses a Tkinter graphical interface to try passwords from a wordlist against the hash, to find a match — this simulates how attackers perform "dictionary attacks" against weak passwords.

## Why I Built This
To understand how password hashing works, why weak passwords are easy to crack, and why strong password policies matter in cybersecurity.

## Tools & Tech Used
- Python
- Spyder (IDE)
- Tkinter (for GUI)
- Hashing (mention your algorithm here — MD5/SHA-256/etc.)

## How It Works
1. Run the hash generator script to create a hash from a password.
2. Run the cracker script, load a wordlist file, and it attempts to match wordlist entries against the hash.
3. If a match is found, the original password is revealed.

## What I Learned
- How hashing algorithms work
- Why weak/common passwords are vulnerable to dictionary attacks
- Basics of building a simple GUI in Python using Tkinter

## Disclaimer
This project is for educational purposes only, built as part of my cybersecurity coursework, to understand password security concepts.
