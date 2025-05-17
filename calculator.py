print("welcome to the tip calcualtor")
total_bill = input("what was the total bill? $")
tip = input("what percentage tip would you like to give? 10, 12, or 15?")
no_of_people = int(input("how many people to split the bill?"))

final_bill = float(total_bill) + float(total_bill) * (int(tip)/100)
per_person_bill= final_bill / no_of_people

print(f"each person should pay : {round(per_person_bill,2)}")