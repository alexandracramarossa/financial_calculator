#By: Alexandra Cramarossa, 20213311
#For: CISC 101
#Date: May 28, 2021

def main():
    
    #Principal 
    input_okay = False
    while not input_okay:
        try:
            principal = float(input("Please Enter the Total Amount Borrowed in Dollars: "))

            if principal <1000 or principal >500000:  
                print("Principal Must Lie Between 1000 and 500000 Inclusive.")

            else:
                input_okay = True
        except ValueError :
            print("You did not enter a number, please try again")
            return

    #Payment Term in Years
    input_okay = False
    while not input_okay:
        try:
            term = float(input("Next Enter the Term of Repayment in Years: "))

            if term <1 and term >30: 
                print("Term For Repayment Must Lie Between 1 and 30 Years.")
                
            else:
                input_okay = True
        except ValueError:
            print("You did not enter a number, please try again")
            return

    #Annual Interest Rate
    input_okay = False
    while not input_okay:
        try:
            interest_rate = float(input("Finally, Enter the APR, or Annual Interest Rate as a Percentage: "))

            if interest_rate <1 and interest_rate >10: 
                print("APR must lie between 1 and 10 Percent Inclusive.")

            else:
                input_okay = True
        except ValueError:
            print("You did not enter a number, please try again")
            return

    #Calculate Monthly Payment and Total 
    term_months = term * 12 
    monthly_interest_rate = interest_rate/1200
    monthly_payment = (principal * monthly_interest_rate) / (1 -(1 + monthly_interest_rate)**(-1 * term_months)) 
    total_interest = term_months * monthly_payment - principal

    print("The Value for the Monthly Payment is: $ {:.2f}".format(round(monthly_payment, 2))) #Prints monthly payment and rounds to 2 decimals

    user_input = str(input("Would you Like to Make Anniversary Payments? Answer yes or no: "))

    counter = 1
    if user_input == 'yes':

        total_mortgage = principal
        total_monthly = 0
        total_interest = 0
        anniversary = 5000
        total_anniversary = 0

        print("Month:     Principal:")
        while principal > 0:
            interest_monthly = monthly_interest_rate * principal
            principal_new = monthly_payment - interest_monthly

            if principal_new > principal:
                principal = 0

            else:
                principal = principal - principal_new
            print(counter, "        ",format(round(principal, 2)))

            if counter % 12 == 0 and counter => 12:
                if principal < 100000:
                    anniversary = principal * 0.05
                    principal = principal - anniversary
                    
                elif anniversary > principal:
                    principal = 0

                else:
                    principal = principal - anniversary
                print("\nAnniversary Payment: $ {:.2f}".format(round(anniversary, 2)))
                print("Remaining Principal: $ {:.2f}\n".format(round(principal, 2)))
                total_anniversary = anniversary + total_anniversary
            counter += 1
            counter_total = counter - 1
            
            total_months_saved = term_months - counter_total
            total_interest = interest_monthly + total_interest
        total_mortgage = total_interest + total_mortgage
        total_monthly = total_mortgage - total_anniversary

        print("\nWith Anniversary Payments, you Have Saved", total_months_saved, " Months Paying off Your Mortgage.")
        print("TOTAL Anniversary Payments: $ {:.2f}".format(round(total_anniversary, 2)))
        print("TOTAL Interest Payments: $ {:.2f}".format(round(total_interest, 2)))
        print("TOTAL Monthly Payments: $ {:.2f}".format(round(total_monthly, 2)))
        print("\nMORTGAGE TOTAL COST: $ {:.2f}".format(round(total_mortgage, 2)))
        

    elif user_input == 'no':

        total_interest = 0

        print("Month:     Principal:")
        while counter <= term_months:
            interest_monthly = monthly_interest_rate * principal
            principal_new = monthly_payment - interest_monthly

            if principal_new > principal:
                principal = 0

            else:
                principal = principal - principal_new
            print(counter, "        ",format(round(principal, 2)))
            counter += 1

            total_interest = interest_monthly + total_interest
        total_monthly = term_months * monthly_payment
        total_mortgage = total_monthly

        print("\nMORTGAGE TOTAL COST: $ {:.2f}".format(round(total_mortgage, 2)))
        print("\nTOTAL Monthly Payments: $ {:.2f}".format(round(total_monthly, 2)))
        print("TOTAL Interest Payments: $ {:.2f}".format(round(total_interest, 2)))

main()
            

