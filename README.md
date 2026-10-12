# Password Strength Analyzer Using Hashing

A beginner-friendly Python project built in three progressive modules.

## Files

- `module2.py` — SHA-256 hash generation, common-password lookup, and a basic 5-point checklist.
- `module3.py` — imports Module 2 and adds repeated-character, sequential-pattern, and excessive-same-character checks.
- `module4.py` — imports Module 3 and combines the checks into a final strength label and suggestions.
- `common_passwords.txt` — small educational dataset of common passwords.

## Requirements

Python 3.8 or newer. No third-party packages are required.

## Run

Open a terminal in this folder and run:

```bash
python module2.py
python module3.py
python module4.py
```

For Module 4, use a terminal that supports `getpass`; the password is hidden while typing.

## Notes

This is an educational demonstration, not a production password-security system. A plain SHA-256 hash is not appropriate for storing real user passwords. Real applications should use a dedicated password-hashing algorithm such as Argon2id, scrypt, or bcrypt. The common-password file is a small sample dataset, not a comprehensive list.
