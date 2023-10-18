'''day = input("Enter the day hot or cool \n")
day = day.lower()
if day == 'hot':
    print("It's a hot day")
    print("Drink Plenty of water")
elif day == 'cool':
    print("It's a cold day")
    print("Wear a warm cloth")
else:
    print("It's a Lovely day")
print("Don't forget to went outside")


price_of_the_house = 10000000
loan_months = 60
credit_score = int(input("Enter your Credit Score :"))
if credit_score >= 8:
    new_price = price_of_the_house * 20 / 100
    new_price = round(new_price)
    emi = new_price / loan_months
    emi = round(emi)
    print(f"Price after discount is {new_price} and the emi is {emi} per month ")
else:
    new_price = price_of_the_house * 10 / 100
    new_price = round(new_price)
    emi = new_price / loan_months
    emi = round(emi)
    print(f"You will get only 10 % discount . And the price is {new_price} and the emi is {emi} per month")
'''

