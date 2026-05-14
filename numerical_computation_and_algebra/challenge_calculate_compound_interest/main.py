def calculate_compound_interest(principal, rate, times_compounded, years):
    # Write your code here
    amount = principal * (1+rate/times_compounded)**(times_compounded*years)
    return amount

final_amount = calculate_compound_interest(1500, 0.043, 4, 6)
print(final_amount)