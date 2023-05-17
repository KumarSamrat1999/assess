import calendar

class Loan:
    def __init__(self, principal, tenure, interest_rate):
        self.principal = principal
        self.tenure = tenure
        self.interest_rate = interest_rate

    def calculate_emis(self):
        monthly_interest_rate = self.interest_rate / 12 / 100
        emi = (self.principal * monthly_interest_rate * (1 + monthly_interest_rate) ** self.tenure) / (
                (1 + monthly_interest_rate) ** self.tenure - 1)
        remaining_balance = self.principal

        print("Month\t\tPrincipal Payment\t\tInterest\t\tEMI\t\tRemaining Balance")
        print("---------------------------------------------------------------------------------------------------------------------")
        month_names = calendar.month_abbr[1:self.tenure+1]  # Get the abbreviated month names

        for i, month in enumerate(month_names):
            interest = remaining_balance * monthly_interest_rate
            principal_payment = emi - interest
            remaining_balance -= principal_payment

            print(f"{month}\t\t\t{principal_payment:.2f}\t\t\t{interest:.2f}\t\t\t{emi:.2f}\t\t{remaining_balance:.2f}")

loan_amount = float(input("Enter the principal amount: "))
loan_tenure = int(input("Enter the tenure in months: "))
interest_rate = float(input("Enter the interest rate (in percentage): "))

loan = Loan(loan_amount, loan_tenure, interest_rate)
loan.calculate_emis()
