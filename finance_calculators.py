#Finance Calculators Task

#Import libraries
import math

#Display instructions and ask for input
print("Choose either 'investment' or 'bond' from the menu below to proceed: ")
print("\n")
print("investment \t - to calculate the amount of interest you'll earn on interest")
print("bond \t\t - to calculate the amount you'll have to pay on a home loan")
calculation_type = input("Selection: ").lower() #Standardise the input to a lowercase string

#check if user input something
if calculation_type=="":
    print("\nError: nothing entered. User was supposed to enter either 'investment' or 'bond'.")
    
else:
    
    print(f"\nYou've selected {calculation_type}")
    #Now check if calculation_type is investment or bond
    
    
    if calculation_type=="investment":
        
        #additional inputs for investment
        deposit = float(input("Enter the deposit amount: R"))
        interest_rate = float(input("Enter the interest rate %: "))
        years = int(input("Enter the number of years of the investment: "))
        interest = input("Choose either 'simple' or 'compound' interest: ").lower() #standardise the input to a lowercase string
        
        #change interest rate into a decimal
        int_rate_decimal = interest_rate*0.01
        
        #now calculate and print total amount at end of investment based on interest type
        if interest=="simple":
            total_amount = round(deposit*(1+int_rate_decimal*years),2) #also round off to 2 decimal places
            print(f"Total amount at end of investment period: R{total_amount}")
            
        elif interest=="compound":
            total_amount = round(deposit*math.pow((1+int_rate_decimal),years),2)
            print(f"Total amount at end of investment period: R{total_amount}")
        
        else:
            #print an error message to the user
            print("\nError: incorrect input on interest. User was supposed to choose either 'simple' or 'compound'.")
        
    
    elif calculation_type=="bond":
        
        #additional inputs for bond
        house_pv = float(input("Enter the present value of the house: R"))
        ann_interest_rate = float(input("Enter the annual interest rate %: "))
        num_months = float(input("Enter the number of months to repayment of the bond: ")) #float variable in case it is e.g. 7.5 months
        
        #first calculate monthly interest rate
        mon_int_rate = ann_interest_rate/12
        
        #now change the interest rate into a decimal
        decimal_int_rate = mon_int_rate*0.01
        
        #now calculate and print repayment amount
        repayment = round((decimal_int_rate*house_pv)/(1-math.pow((1+decimal_int_rate), -num_months)),2)
        print(f"Your monthly repayment is: R{repayment}")
