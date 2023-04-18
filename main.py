# Sprint week project 1
# Authors:                Date:

import datetime


# Define functions

# A function for the start and end dates of a trip, in YYY-MM-DD format.
def StartEndDates():
    while True:

        StartDateStr = input("Enter the start date of the trip (YYYY-MM-DD): ")
        if StartDateStr == "":
            print("Start date cannot be blank. Please re-enter.")

            continue

        try:
            StartDate = datetime.datetime.strptime(StartDateStr, "%Y-%m-%d")
        except:
            print("Date must be in YYYY-MM-DD format. Please re-enter.")
            continue
        break


def EmpClaimProc():
    # Inputs for Employee Travel Claim

    DAILY_RATE = 85
    MIL_RATE = 0.17
    MIL_RATE_RENT = 65.00
    BONUS_ABOVE_3 = 100.00
    BONUS_ABOVE_1000 = 0.04
    DEC_15_TO_22_BONUS = 50.00

    allowed_char = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
    allowed_num = set("0123456789")

    while True:
        EmpNum = input("Enter the employee number: ")
        if EmpNum == "":
            EmpNum = print("The employee number cannot be blank. Please re-enter.")
            continue
        elif len(EmpNum) != 5:
            EmpNum = print("The employee number must be 5 numbers. Please re-enter.")
            continue

            # Skips over this validation.
        elif EmpNum.isdigit() == False:
            print("The employee number must be numbers only. Please re-eneter.")
            continue
        else:
            break

    while True:

        EmpFName = input("Enter the employee first name: ").title()

        if EmpFName == "":
            print("Employee first name cannot be blank. Please re-enter.:")
        else:
            break

    while True:

        EmpLName = input("Enter the employee last name: ").title()

        if EmpLName == "":
            print("Employee last name cannot be blank. Please re-enter.")
        else:
            break

    while True:

        LocTrip = input("Enter the location of the trip: ")

        if LocTrip == "":
            print("Location of the trip cannot be blank. Please re-enter.")
        else:
            break

    StartEndDates()

    while True:

        EndDateStr = input("Enter the end date of the trip (YYYY-MM-DD): ")

        if EndDateStr == "":
            print("End date cannot be blank. Please re-enter.")
            continue

        try:
            EndDate = datetime.datetime.strptime(EndDateStr, "%Y-%m-%d")
        except:
            print("Date must be in YYYY-MM-DD format. Please re-enter.")
            continue
        break

        # End date validation needs to be no longer than 7 days after start date

    while True:
        NumDays = 0

        NumDays = input("Enter the number of days: ")

        if NumDays == "":
            print("The number of days cannot be blank. Please re-enter.")
        else:
            break
        if NumDays >= "4":
            NumDays = 100

            # If getting the bonus here, NumDays doesn't need to be an input.

    while True:

        OwnOrRented = input("Enter whether the car was the employee's or rented (O/R): ").upper()

        if OwnOrRented == "":
            print("The field cannot be blank. Please re-enter.")
        elif OwnOrRented != "O" and OwnOrRented != "R":
            print("The option must be O or R only. Please re-enter.")
        else:
            break

    while True:
        TotKiloTrav = 0
        KM_BONUS = 0

        if OwnOrRented == "O":
            TotKiloTrav = int(input("Enter the total kilometers travelled: "))
        elif OwnOrRented == "R":
            break

        if TotKiloTrav == "":
            print("Total kilometers travelled cannot be blank. Please re-enter.")
        elif TotKiloTrav > 2000:
            print("Total kilometers travelled cannot exceed 2000. Please re-enter.")
        else:
            break
        if OwnOrRented == "O" and TotKiloTrav >= 1000:
            KM_BONUS = .04



    while True:

        ClaimType = input("Enter the claim type (S/E): ").upper()

        if ClaimType == "":
            print("Claim type must not be blank. Please re-enter.")
        elif ClaimType != "S" and ClaimType != "E":
            print("Claim type must be S or E only. Please re-enter.")
        else:
            break
        if ClaimType != "E":
            EXEC_BONUS = 45.00
        elif ClaimType != "S":
            EXEC_BONUS = 0


    PerDiemAmt = NumDays * DAILY_RATE
    Mileage = MIL_RATE * TotKiloTrav
    Bonus = ((TotKiloTrav * KM_BONUS) + DayBonus + (NumDays * EXEC_BONUS))
    ClaimAmt = PerDiemAmt + Mileage + Bonus
    ClaimTotal = (ClaimAmt * HST_Rate) + ClaimAmt

    print("    NL Chocolate Company")
    print("Travel Claims Print Out Report")
    print(f"Employee Numeber: {EmpNum}")
    print(f"Employee Name: {EmpFName}, {EmpLName}")
    print(f"Trip Location: {LocTrip}")
    print(f"Start Date: {StartDate}  End Date: {EndDate}")
    print(f"Total Day Of Trip: {NumDays}" )
    print(f"Total KM Travelled: {TotKiloTrav} ")
    print(f"Claim Type: {ClaimType}")
    print(f"Per Diem Amount: {PerDiemAmt} ")
    print(f"Total Mileage Amount: {Mileage}")
    print(f"Total Bonus Amount: {Bonus} ")
    print(f"Total Claim Amount: {ClaimTotal} ")
    input("Press any key to continue: ")



# Bonus, claim amount, etc. need to be calculated

# Display/formatting


def FunIntQ():
    for n in range(1, 101):
        if n % 5 == 0 and n % 8 == 0:
            print("FizzBuzz")
        elif n % 5 == 0:
            print("Fizz")
        elif n % 8 == 0:
            a = print("Buzz")
        else:
            print(str(n))
    input('Press any key to continue:')


def Cool_Dates():
    import datetime
    CurDate = datetime.datetime.now()
    # Employee will enter First Name, Last Name and Phone Number to get there new company email and password
    while True:
        FirstNa = input("Enter First Name: ").title()
        if FirstNa == "":
            print("First Name cannot be blank.")
        else:
            break
    while True:
        LastNa = input("Enter Last Name: ").title()
        if LastNa == "":
            print("First Name cannot be blank.")
        else:
            break
    allowed_char = set("0123456789")
    while True:
        PhoneNum = input("Enter Phone Number(#########): ")  # 10 digits/must enter
        if len(PhoneNum) != 10:
            print("Phone number must be 10 digits - Please re-enter.")
        elif set(PhoneNum).issubset(allowed_char) == False:  # elif CCNum.isdigit() == False
            print("Phone number contains invalid characters.Please re - enter.")
        else:
            break
    NewUser = (FirstNa + "." + LastNa + "@NLChoc.com")
    NewPass = (FirstNa[0] + LastNa[0] + PhoneNum[6:10] + "!")
    # Employee will Enter their start date and be told how many days they have been with the company
    StartDate = input("Enter Start Date(YYYY-MM-DD): ")
    StartDate = datetime.datetime.strptime(StartDate, "%Y-%m-%d")
    DaysWith = (CurDate - StartDate).days
    # Employee with enter their Birth Month and Day and get their Zodiac sign
    month = input("Input month of birth (e.g. march, july etc): ")
    day = int(input("Input birth day: "))
    if month == 'december':
        astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
    elif month == 'january':
        astro_sign = 'Capricorn' if (day < 20) else 'Aquarius'
    elif month == 'february':
        astro_sign = 'Aquarius' if (day < 19) else 'Pisces'
    elif month == 'march':
        astro_sign = 'Pisces' if (day < 21) else 'Aries'
    elif month == 'april':
        astro_sign = 'Aries' if (day < 20) else 'Taurus'
    elif month == 'may':
        astro_sign = 'Taurus' if (day < 21) else 'Gemini'
    elif month == 'june':
        astro_sign = 'Gemini' if (day < 21) else 'Cancer'
    elif month == 'july':
        astro_sign = 'Cancer' if (day < 23) else 'Leo'
    elif month == 'august':
        astro_sign = 'Leo' if (day < 23) else 'Virgo'
    elif month == 'september':
        astro_sign = 'Virgo' if (day < 23) else 'Libra'
    elif month == 'october':
        astro_sign = 'Libra' if (day < 23) else 'Scorpio'
    elif month == 'november':
        astro_sign = 'Scorpio' if (day < 22) else 'Sagittarius'
    print(f"You're A {astro_sign}!")
    print(f"You've been with the company for {DaysWith} days!")
    print(f"New Company Email: {NewUser}")
    print(f"New Company Password: {NewPass}")
    input('Press any key to continue:')


def OldNew():
    # Random number generator
    # using the random module to create a guessing game
    # Firstly need to import random module that's included in the standard library.
    import random
    # Random.choice(Intros) grabs a random intro from the list and plugs it into UserIntro
    while True:
        UserName = input("Enter name: ").title()
        if UserName == "":
            print("Name cant be blank")
        else:
            break
    Intros = ["Bonjour", "Hi", "Hey", "Greetings", "How are you today"]
    UserIntro = random.choice(Intros)
    print(UserIntro, UserName, "wanna play a game?")
    while True:
        PickColour = ["Black", "Red", "Blue"]
        UserColour = input("Pick a colour: Black, Red, or Blue: ").title()
        ColourRNG = random.choices(PickColour, weights=[49, 49, 2])
        AllowedCharR = set("BRbrluedack")
        if UserColour == "":
            print("Your guess can't be blank. Please re-enter.")
        elif set(UserColour).issubset(AllowedCharR) == False:
            print("Please only type one of the colours (Black, Red, or Blue): ")
        elif UserColour == "Black":
            break
        elif UserColour == "Red":
            break
        elif UserColour == "Blue":
            break
        else:
            break
    while True:
        # RandomNum = random.randint(0,10) - randint make a random value that's a int
        RandomNum = random.randint(1, 10)
        UserGuess = int(input("Guess a number from 1-10: "))
        if UserGuess == "":
            print("Your guess can't be blank. Please re-enter: ")

        if RandomNum != UserGuess:
            print("Sorry, you guessed wrong. The number was: ", RandomNum)
            KeepGuess = input("Would you like to continue guessing? (Y/N): ").upper()
            if KeepGuess == "Y":
                continue
            else:
                break

        if RandomNum != UserGuess:
            print("Sorry, you guessed wrong. The number was: ", RandomNum)
            KeepGuess = input("Would you like to continue guessing? (Y/N): ").upper()
            if KeepGuess == "Y":
                continue
            else:
                break
    input("Press any key to continue: ")


# Define 2 more functions - a calculation, and another purpose. No adding to menu.

# Function for the Main Menu.
def MainMenu():
    while True:
        print()
        print("     NL Chocolate Company")
        print("Travel Claims Processing System")
        print()
        print("1. Enter an Employee Travel Claim.")
        print("2. Fun Interview Question.")
        print("3. Cool Stuff with Strings and Dates.")
        print("4. Something Old, Something New.")
        print("5. Quit Program")
        print()

        Choice = int(input("Enter choice (1-5): "))

        if Choice == 1:
            print()
            print("Enter an Employee Travel Claim")
            print()
            EmpClaimProc()

        elif Choice == 2:
            print()
            print("Fun Interview Question")
            print()
            FunIntQ()

        elif Choice == 3:
            print()
            print("Cool Stuff With Strings and Dates")
            print()
            Cool_Dates()

        elif Choice == 4:
            print()
            print("Something Old, Something New")
            print()
            OldNew()

        elif Choice == 5:
            print()
            print("Quit Program")
            input("Press any key to quit: ")
            break

        # Output


print(MainMenu())
