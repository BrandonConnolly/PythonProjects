


# Sprint week project 1
# Authors:                Date:

import datetime

def EmpClaimProc():
    # Inputs for Employee Travel Claim

    DAILY_RATE = 85
    MIL_RATE = 0.17
    MIL_RATE_RENT = 65.00
    BONUS_ABOVE_3 = 100.00
    BONUS_ABOVE_1000 = 0.04
    EXEC_BONUS = 45.00
    DEC_15_TO_22_BONUS = 50.00
    HST_RATE = 0.15

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

    while True:
        DateBonus = 0
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

        if StartDate == "%m" != 12 and  "%d" >= 15 and "%d" <= 22:
            DateBonus = DEC_15_TO_22_BONUS
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
        DayBonus = 0
        NumDays = int(input("Enter the number of days: "))

        if NumDays == "":
            print("The number of days cannot be blank. Please re-enter.")
        elif NumDays > 7:
            print("The number of days cannot be 7 days past the start date. Please re-enter.")
        elif NumDays >= 4:
            DayBonus = BONUS_ABOVE_3
            break

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
        else:
            break

        if TotKiloTrav == "":
            print("Total kilometers travelled cannot be blank. Please re-enter.")
        elif TotKiloTrav > 2000:
            print("Total kilometers travelled cannot exceed 2000. Please re-enter.")
        else:
            break

    if OwnOrRented == "O" and TotKiloTrav >= 1000:
        KM_BONUS = BONUS_ABOVE_1000
    else:
        KM_BONUS = 0

    while True:

        ClaimType = input("Enter the claim type (S/E): ").upper()
        ExecBonus = 0
        if ClaimType == "":
            print("Claim type must not be blank. Please re-enter.")
        elif ClaimType != "S" and ClaimType != "E":
            print("Claim type must be S or E only. Please re-enter.")
        else:
            break
        if ClaimType == "E":
            ExecBonus = EXEC_BONUS * NumDays


    # Display/formatting
    while True:

        if ClaimType == "E":
            ClaimType = "Executive"
        elif ClaimType == "S":
            ClaimType = "Standard"
        else:
            break

    PerDiemAmt = NumDays * DAILY_RATE

    if OwnOrRented == "O":
        Mileage = MIL_RATE * TotKiloTrav * KM_BONUS
    elif OwnOrRented == "R":
        Mileage = MIL_RATE_RENT
    Bonus = (TotKiloTrav * KM_BONUS) + DayBonus + ExecBonus + (DEC_15_TO_22_BONUS * NumDays)
    ClaimAmt = PerDiemAmt + Mileage + Bonus
    HST = (ClaimAmt * HST_RATE) + ClaimAmt
    ClaimTotal = ClaimAmt + HST

    ClaimAmountDsp = "${:,.2f}".format(ClaimAmt)
    HSTDsp = "${:,.2f}".format(HST)
    ClaimTotalDsp = "${:,.2f}".format(ClaimTotal)
    MileageDsp = "${:,.2f}".format(Mileage)
    PerDiemAmtDsp = "${:,.2f}".format(PerDiemAmt)
    BonusDsp = "${:,.2f}".format(Bonus)

    print()
    print("         NL Chocolate Company")
    print("     Travel Claims Print Out Report")
    print()
    print(f"Employee Number: {EmpNum:<5s}")
    print(f"Employee Name: {EmpFName:<10s} {EmpLName:<10s}")
    print(f"Trip Location: {LocTrip:<12s}")
    print(f"Start Date: {StartDateStr:<10s}    End Date: {EndDateStr:<10s}")
    print(f"Total Days Of Trip: {NumDays:<2d}")
    print(f"Total KM Travelled: {TotKiloTrav:<5d} ")
    print(f"Claim Type:  {ClaimType:<8s}")
    print()
    print(f"Per Diem Amount:           {PerDiemAmtDsp:>9s} ")

    if OwnOrRented == "O":
        print(f"Total Mileage Amount:     {MileageDsp:>9s}")

    print(f"Total Bonus Amount:        {BonusDsp:>9s} ")
    print(f"Claim amount:              {ClaimAmountDsp:>9s}")
    print(f"HST:                       {HSTDsp:>9s}")
    print(f"Total Claim Amount:        {ClaimTotalDsp:>9s} ")
    print()
    input("Press any key to continue: ")

    while True:

        TravClaimContin = input("Would you like to do another travel claim?(Y/N): ").upper()
        if TravClaimContin == "":
            print("Can't be blank(Enter Y/N)")
        elif TravClaimContin != "Y" and TravClaimContin != "N":
            print("Must enter Y or N")
        elif TravClaimContin == "N":
            break
        elif TravClaimContin == "Y":
            continue




# Define functions


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