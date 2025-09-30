
- [Task 6 : Create a Strong Password and Evaluate Its Strength](#task-6--create-a-strong-password-and-evaluate-its-strength)
- [Objective](#objective)
- [Tools](#tools)
- [Deliverables](#deliverables)
- [Guide](#guide)
    - [Create Multiple Passwords](#create-multiple-passwords)
    - [Use a Mix of Characters](#use-a-mix-of-characters)
    - [Test Passwords on a Strength Checker](#test-passwords-on-a-strength-checker)
    - [Record Scores and Feedback](#record-scores-and-feedback)
    - [Identify Best Practices](#identify-best-practices)
    - [Tips for Creating Strong Passwords](#tips-for-creating-strong-passwords)
    - [Tips Learned from the Evaluation](#tips-learned-from-the-evaluation)
    - [Common Password Attacks](#common-password-attacks)
    - [Common Password Auditing Tools — High level](#common-password-auditing-tools--high-level)
    - [How Password Complexity Affects Security](#how-password-complexity-affects-security)
- [Outcome](#outcome)



## Task 6 : Create a Strong Password and Evaluate Its Strength

## Objective

Understand what makes a password strong and test it against password strength tools

## Tools

- [PasswordMonster](https://www.passwordmonster.com/)

## Deliverables

Report showing password strength results and explanation

## Guide

1.Create multiple passwords with varying complexity.

2.Use uppercase, lowercase, numbers, symbols, and length variations.

3.Test each password on password strength checker.

4.Note scores and feedback from the tool.

5.Identify best practices for creating strong passwords.

6.Write down tips learned from the evaluation.

7.Research common password attacks (brute force, dictionary).

8.Summarize how password complexity affects security

---


### Create Multiple Passwords
Generate a variety of passwords with different levels of complexity. Examples:
- simplepassword
- testinghellosd  
- testinghellod12
- !s@Niraj+    
- tY7#vW9q*2eLzB  

###  Use a Mix of Characters
When creating passwords, vary the following elements:
- **Uppercase letters** (A-Z)
- **Lowercase letters** (a-z)
- **Numbers** (0-9)
- **Symbols** (!, @, #, $, etc.)
- **Length** (Aim for at least 14 characters)

I construct my own Python script for password creation.
![python script password generator](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-6/images/python_script_password_generator.png)


### Test Passwords on a Strength Checker
Use reliable password strength tools like:
- [How Secure Is My Password](https://howsecureismypassword.net/)
- [Password Monster](https://www.passwordmonster.com/)
- [NordPass Strength Checker](https://nordpass.com/password-strength-checker/)

###  Record Scores and Feedback

Check out [PasswordMonster](https://www.passwordmonster.com/) for testing your password strength.

| **Password**         | **Strength Rating** | **Estimated Time to Crack**     |
|----------------------|---------------------|----------------------------------|
| simplepassword       | Very Weak           | 0.02 seconds                     |
| testinghellosd       | Weak                | 8.27 minutes                     |
| testinghellod12      | Medium              | 4 hours                          |
| !s@Niraj+            | Strong              | 13 days                          |
| tY7#vW9q*2eLzB       | Very Strong         | 174 trillion years              |


![weak\_password](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-6/images/weak_password.png)
![weak\_pp](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-6/images/weak_pp.png)
![medium](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-6/images/medium.png)
![strong](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-6/images/strong.png)
![verystrong](https://raw.githubusercontent.com/hackThacker/internship-projects/main/Day-6/images/verystrong.png)


**Specific Feedback / Warnings**

- Too short  
- Common pattern detected  
- Uses only lowercase letters  
- Contains keyboard sequences (e.g., "12345", "qwerty")  
- Includes common substitutions (e.g., "@" for "a")  
- Repeated characters  
- Predictable phrases or dictionary words  


###  Identify Best Practices
From the test results, identify patterns in strong passwords. Common features include:
- 12+ characters
- Mix of all character types
- Avoiding dictionary words
- No personal information (names, birthdates)

###  Tips for Creating Strong Passwords
- Use a **random passphrase** or **password manager** to generate/store passwords.
- Avoid using the same password across multiple sites.
- Consider using a **password formula** (e.g., base + site-specific tag).
- Regularly update important passwords.
- Test new passwords using a strength checker before using them.


### Tips Learned from the Evaluation
- Use longer passwords (12+ characters recommended)
- Avoid common words and predictable patterns
- Mix uppercase, lowercase, numbers, and special characters
- Avoid simple substitutions (e.g., "@" for "a")
- Use passphrases or random combinations for better security

###  Common Password Attacks
- **Brute Force:** Attempts every possible combination until the password is found
- **Dictionary Attack:** Uses a list of common words and variations to guess the password
- **Rainbow Table Attack:** Uses precomputed hash tables to reverse hashed passwords quickly
- **Credential Stuffing:** Reuses leaked passwords from other breaches to gain access

### Common Password Auditing Tools — High level

- **Hydra (THC‑Hydra)**  
  A network login cracker framework that supports many protocols (SSH, HTTP(s), FTP, SMB, etc.). Often used in authorized assessments to test remote authentication resilience.

- **John the Ripper**  
  A password‑hash analysis and cracking tool primarily used for offline hash cracking (analyzes password hashes rather than live online services). Used by defenders to verify strength of stored password hashes.

- **Hashcat**  
  A high‑performance GPU‑accelerated password recovery tool for offline cracking of hashed passwords. Common in research and defensive lab work to benchmark hash schemes.

- **Ncrack**  
  A high‑speed network authentication cracking tool focused on network protocols and resilient connection handling. Used in authorized penetration tests to evaluate network auth.

- **Medusa**  
  A parallel, modular login brute‑forcer for network protocols (similar use‑case to Hydra).

- **RainbowCrack**  
  Uses precomputed rainbow tables to reverse hashed passwords; conceptually demonstrates why salts and strong hashing matter.



### How Password Complexity Affects Security
- Increasing length exponentially raises the number of possible combinations
- Mixing character types (letters, numbers, symbols) increases complexity
- Complex passwords resist brute force and dictionary attacks better
- Simple or predictable passwords are cracked quickly, compromising security

## Outcome

- Understanding password security and best practices.
