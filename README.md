# Python-Project
<h1>Project 1: ATM Simulator</h1>
Starter data:
correct_pin = "1234"
balance = 10000

Stage 1: PIN check
Give the user 3 attempts to enter the PIN using a while loop. After 3 wrong attempts, stop the program.
Expected output (for three wrong attempts):
Wrong PIN. Attempts left: 2
Wrong PIN. Attempts left: 1
Card blocked.

Stage 2: Menu
After a correct PIN, show a while True menu: 1. Balance, 2. Deposit, 3. Withdraw, 4. Exit. The menu repeats
until the user chooses 4.
Expected output on exit:
Thank you!

Stage 3: Deposit and withdraw
Deposit adds money (the amount must be above 0). Withdraw must reject amounts above the balance.
Expected output (depositing 2000, then withdrawing 50000):
New balance: 12000
Insufficient balance

Stage 4: Extension
Store each transaction in a list and print the history when the user exits.
Expected output:
Deposit 2000
Withdraw 500

<h1>Project 2: Student Marks Manager</h1>
Starter data:
students = {"Aman": [85, 90, 78], "Riya": [92, 88, 95], "Zoya": [70, 65, 80]}

Stage 1: Averages
Use a for loop to print each student's average rounded to 2 decimals.
Expected output:
Aman 84.33
Riya 91.67
Zoya 71.67

Stage 2: Grades
Add a grade using if / elif / else: A (85 and above), B (70 and above), C (50 and above), F (below 50).
Expected output:
Aman 84.33 B
Riya 91.67 A
Zoya 71.67 B

Stage 3: Topper
Find and print the topper using a loop that tracks the highest average.
Expected output:
Topper: Riya

Stage 4: Menu
Build a while True menu: 1. Add student, 2. View all, 3. Show topper, 4. Exit. The menu repeats until the
user chooses 4.
Expected output on exit:
Goodbye!

Stage 5 (optional): Validation
When adding a student, keep asking until all 3 marks are between 0 and 100, and reject names that already
exist.
Expected output (for a mark of 105 or an existing name):
Invalid mark, try again.
Student already exists.
