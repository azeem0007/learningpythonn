import random

print("flip a coin")


print("heads" if random.randint(0,1)==0 else "tails")

countries = ["USA" , "INDIA" , "ENGLAND"]
print("random country is " + random.choice(countries)  )