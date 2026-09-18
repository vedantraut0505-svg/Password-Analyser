# Algorithm — Module 1

## Basic Password Hashing & Common-Password Detection

### Input
User password

### Output
Password strength and common-password status

### Steps

1. Start.
2. Create a list of commonly used passwords.
3. Take the password as input from the user.
4. Generate the hash of the user's password.
5. Store the generated hash as `user_hash`.
6. Take each password from the common-password list.
7. Generate the hash of each common password.
8. Compare `user_hash` with the common-password hashes.
9. If a matching hash is found:
   - Mark the password as commonly used.
   - Classify it as weak.
10. If no matching hash is found:
    - Mark the password as not found in the common-password list.
    - Continue with basic strength checks.
11. Display the result.
12. Stop.