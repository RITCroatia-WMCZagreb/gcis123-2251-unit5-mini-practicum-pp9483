'''
@ASSESSME.USERID: pp9483
@ASSESSME.AUTHOR: Patrik Pavlovic
@ASSESSME.DESCRIPTION: MiniPractical
@ASSESSME.ANALYZE: YES
'''



# The  thecima values of PI
PI_VALUE = "3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679"

def pi_tester():
    picounter = 1
    pisplit = PI_VALUE.strip()
    index = 2
    pin = input("Enter the "+str(picounter)+"-th digit of pi: ")
    while pin == pisplit[index]:
        picounter += 1
        index += 1
        pin = input("Enter the "+str(picounter)+"-th digit of pi: ")
        if picounter == 100:
            print("You win! ","\n","Number of correct decimal digits:",picounter-1)
            return "Your title",display_score(picounter)
    print("Incorrect digit. The correct digit is",pisplit[index]+".","\n"+"Number of correct decimal digits:",picounter-1)
    return print("Your title:",display_score(picounter))
        




def display_score(score):
    if score >= 0 and score <= 4:
        return "PI Neophyte"
    elif score >= 5 and score <= 9:
        return "PI Novice"
    elif score >= 10 and score <= 24:
        return "PI Journeyman"
    elif score >= 25 and score <= 49:
        return "PI Enthusiast"
    elif score >= 50 and score <= 96:
        return "PI Connoisseur"
    elif score >= 97 and score <= 100:
        return "PI Expert"
    elif score >100:
        return "PI Imposter"

def main():
    pi_tester()

if __name__ == "__main__":
    main()