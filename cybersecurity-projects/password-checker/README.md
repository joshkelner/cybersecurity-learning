# Password Checker

Python script that evaluates the strength of a user's password and checks if it has appeared in known data breaches using the [HaveIBeenPwned API](https://haveibeenpwned.com/API/v3)

*Security Disclaimer*: **This script never uploads your full password.** Only the first 5 characters of its SHA-1 hash are sent to the HaveIBeenPwned API per their k-Anonymity model. 

## Features

* **Two Input Methods**
    * Command line arguments
        * Users can input any number of passwords as command line arguments and it will check all of them
        * Allows efficient checking of many passwords
    * Secure User Input
        * If no passwords are input through the command line it will prompt the user to enter one
        * Uses getpass for secure input
* **Password Strength Check**
    * Uses common password complexity standards from NIST and general best practices
    * Minimum length (8+), upper case, lower case, number, special character requirements
    * Returns a strength rating and suggestions for improving strength
* **Breach Check**
    * Compares password against the HaveIBeenPwned API to check against an up-to-date list of breached passwords
    * Displays a warning if the password has been detected
    * Never uploads the full password to the API (see security disclaimer above)
## Installation
1. **Clone the full repository**:
   ```bash
   git clone https://github.com/joshkelner/cybersecurity-learning.git
   cd cybersecurity-learning/cybersecurity-projects/password-checker
   ```
2. **(Optional) Create virtual environment**

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```
4. **Ready to Run!**
    * Either input any number of passwords as command line arguments
    ```bash
    python3 password-checker.py myPassword1 myPassword2 ...
    ```
    * Or run without arguments and the script will prompt you to input a password securely
    ```bash
    python3 password-checker.py
    ```


