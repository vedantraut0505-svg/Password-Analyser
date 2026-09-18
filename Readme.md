# Password Strength Analyzer Using Hashing

## Module 1: Basic Password Hashing and Common Password Detection

### About the Project

This project is a basic password strength analyzer developed using Python. The main idea is to check whether a password entered by the user is present in a list of commonly used passwords.

Instead of directly comparing passwords, the project uses hashing. The entered password is converted into a hash value, and the same process is applied to the common passwords. These hash values are then compared to find a match.

This module is the starting point of the complete Password Strength Analyzer project.

## Objective

The main objectives of Module 1 are:

* Understand the basic concept of hashing.
* Take a password from the user.
* Generate a hash value for the password.
* Generate hash values for common passwords.
* Compare the hash values.
* Identify whether the password is commonly used.
* Give a basic password strength result.

## Technologies Used

* Python
* Python `hashlib` module

## Concepts Used

The following Python concepts are used in this module:

* Variables
* Strings
* User input
* Lists
* Loops
* Functions
* Conditional statements
* Hashing

## How It Works

The basic working of the project is:

```text
User enters password
        ↓
Password is hashed
        ↓
Common passwords are hashed
        ↓
Hash values are compared
        ↓
Match found?
    ↓           ↓
   Yes          No
    ↓           ↓
  Weak       Further
 password    analysis
```

For example, if the user enters `admin` and `admin` is present in the common-password list, the hash generated for `admin` will match the corresponding stored hash.

The program will then identify it as a commonly used password.

## Example

### Input

```
Enter password: admin
```

### Output

```
Common Password: YES
Strength: WEAK
```

If the entered password is not present in the common-password list, the program will report that it was not found and can continue with other basic strength checks.

## Module 1 Structure

```
Module 1
│
├── Get Password
│
├── Generate Password Hash
│
├── Generate Common Password Hashes
│
├── Compare Hashes
│
└── Display Result
```

## Planned Functions

```
get\_password()
hash\_password()
create\_common\_hashes()
check\_common\_password()
display\_result()
```

Each function will have a specific responsibility, which will make the program easier to understand and improve later.

## Project Modules

The project is divided into four modules. Each module increases the difficulty and adds new functionality.

---

## Module 1 — Basic Hashing

### What to do

Take a password from the user, generate its hash, and compare it with the hashes of a small list of commonly used passwords.

### Flow

```text
Password
   ↓
Generate Hash
   ↓
Hash Common Passwords
   ↓
Compare Hashes
   ↓
Match?
 ├── YES → Common Password → Weak
 └── NO  → Not Found
```

### Main Concepts

* User input
* Strings
* Functions
* Lists
* Loops
* `if/else`
* `hashlib`
* SHA-256 hashing

### Output

Identify whether the password is present in the common-password list and give a basic result.

---

## Module 2 — File & Fast Lookup

### What to do

Use a larger list of common passwords stored in a file. Read the file, generate hashes, and use a hash-based data structure for faster searching.

### Flow

```text
Common Password File
        ↓
     Read File
        ↓
    Generate Hashes
        ↓
    Store in Set
        ↓
User Password → Hash
        ↓
     Fast Lookup
        ↓
      Result
```

### Main Concepts

* File handling
* Reading `.txt` files
* `set`
* Dictionaries
* Hash-based lookup
* Functions
* Exception handling

### Output

Check whether the user's password exists in the larger common-password dataset efficiently.

---

## Module 3 — Advanced Strength Analyzer

### What to do

Improve the analyzer so that it checks more than just common passwords.

Analyze:

* Password length
* Uppercase letters
* Lowercase letters
* Numbers
* Special characters
* Common-password match
* Repeated characters
* Simple/predictable patterns

### Flow

```text
             Password
                 ↓
        ┌────────┼────────┐
        ↓        ↓        ↓
     Length   Characters  Common?
        │        │        │
        └────────┼────────┘
                 ↓
          Strength Engine
                 ↓
       Weak / Medium / Strong
```

### Main Concepts

* OOP
* Classes and objects
* Regular expressions
* Validation
* Scoring logic
* Python modules
* Error handling

---

## Module 4 — Complete Application

### What to do

Combine all previous modules into a complete, well-structured Python application.

### Features

* User input and validation
* Hashing
* Common-password dataset
* Fast lookup
* Advanced strength analysis
* Clean modular architecture
* Error handling
* Testing
* Performance optimization
* Proper documentation

### Structure

```text
Password Strength Analyzer
            ↓
      Input & Validation
            ↓
          Hashing
            ↓
     Common Password Check
            ↓
      Strength Analysis
            ↓
       Final Report
```

### Main Concepts

* Advanced OOP
* Multiple Python modules
* Testing
