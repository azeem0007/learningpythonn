print('welcome to blind auction')
bidding={}

auction=True

def bidders():
    name=input("what is your name\n")
    value=int(input("what is your bid\n"))
    bidding[name]=value

def find_highest_bidder():
    highest_bidder= 0   
    for i in bidding:
        score = bidding[i]
        if score > highest_bidder:
            highest_bidder = score
            winner = i
    print(f"the winner is {winner} with a bid of {highest_bidder}")

bidders()
while auction is True:
    game = input("are there any other bidders? type 'yes' or 'no'").lower()
    print("\n" * 100)
    if game == "yes":
        bidders()
    else:
        find_highest_bidder()
        auction = False

print(bidding)


    