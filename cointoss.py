def toss():
    import random
    while True:
        choice = input("Enter your Choice for toss: ").lower()
        tosses = ["heads", "tails"]
        random.shuffle(tosses)
        if choice == "heads":
            if tosses[0] == "heads":
                print("You won the toss")
                return True
            else:
                print("You lost the toss")
                return False

            break
        elif choice == "tails":
            if tosses[0] == "tails":
                print("You won the toss")
                return True
            else:
                print("You lost the toss")
                return False
            break
        else:
            print("Invalid")
#toss()