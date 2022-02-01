print("Welcome to the tip calculator.")
total_bill = input("What was the total bill?$ ")
percentage = input("What percentage would you like to give? ")
totalbill_asfloat = float(total_bill)
percentage_asfloat = float(percentage)
person = input("How many people do you want to split? ")
personasint = int(person)
total_tip = (totalbill_asfloat * percentage_asfloat) / 100
topay = totalbill_asfloat + total_tip
eachcost = round(topay/personasint)
print(f"Each person has to pay $ {eachcost} .")
