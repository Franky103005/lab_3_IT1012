


monthly_salary = float(input("Enter your monthly salary: "))
loan_amount = float(input("Enter the loan amount you are requesting: "))

if monthly_salary >= 30000 and loan_amount <= 10 * monthly_salary:
    months_to_pay = int(input("How many months will you take to pay off the loan? "))
    total_repayment = loan_amount * 1.10
    monthly_payment = total_repayment / months_to_pay
    print(f"Loan approved! Total repayment with 10% interest: {total_repayment:.2f}")
    print(f"You will need to pay {monthly_payment:.2f} per month for {months_to_pay} months.")
else:
    if monthly_salary < 30000:
        print("Loan not approved due to low salary (must be at least 30,000).")
    elif loan_amount > 10 * monthly_salary:
        print("Loan not approved due to high loan request (must be 10 times or less of your salary).")

