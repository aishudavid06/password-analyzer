# Password Strength Analyzer

A web-based tool that evaluates the strength of user-entered passwords using security rules and basic cryptographic concepts.

---
## Features

*  Checks password length and complexity
*  Classifies password as **Weak / Medium / Strong**
*  Live password strength tracking
*  Detects common patterns (like 123, abc)
*  Suggests strong passwords
*  Stores passwords securely using **SHA-256 hashing**
*  Prevents reuse of previously used passwords (internally)
*  Show/Hide password option

---
## Concepts Used

* Password Security
* Hashing (SHA-256)
* Pattern Detection
* Basic Cybersecurity Practices

---

## Technologies Used

* Python (Flask)
* HTML, CSS, JavaScript
* SQLite Database

---

## How to Run

1. Install Flask:

   ```
   pip install flask
   ```

2. Run the application:

   ```
   python app.py
   ```

3. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

---

## Output

* Displays password strength (Weak / Medium / Strong)
* Provides suggestions for weak passwords
* Shows live strength indicator while typing

---

## Future Improvements

* Use bcrypt instead of SHA-256
* Add user login system
* Integrate real-world breach password API

---

## Author

* Aishwariya E
