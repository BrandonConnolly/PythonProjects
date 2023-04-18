#Car Rent Project
#Author Brandon Connolly
#Due Date Sept 23 2022

#Current Costs & Rate
Hst_Rate = .15
KM_Rate = .10
DayRate = 35

#Car Rental Input Information
CustName =  input("Enter Customers Name: ")
CustPhone = input("Enter Customer Phone Number: ")
Days_Rent = input("Enter Total Number of Day Vehicle was Rented: ")
Days_Rent = float(Days_Rent)
KM_Rent = input("Enter KM Total at Time of Rental: ")
KM_Rent = float(KM_Rent)
KM_Return = input("Enter KM Total at Return of Rental: ")
KM_Return = float(KM_Return)

#Calculations
Day_Cost = DayRate * Days_Rent

KM_Travel = KM_Return - KM_Rent

KM_Cost = KM_Travel * KM_Rate

TotalCost = Day_Cost + KM_Cost

#Printed Information
print(f"   Customer Name: {CustName:<8s}")
print(f"   Customer Phone Number: {CustPhone:<12s}")
KM_Travel = "{:,.2f}".format(KM_Travel)
print(f"   Total KM Travelled: {KM_Travel:<6s}")
KM_Cost = "${:,.2f}".format(KM_Cost)
print(f"   Total Cost of KM Travelled: {KM_Cost:<6s}")
Day_Cost = "${:,.2f}" .format(Day_Cost)
print(f"   Total Day Rental Cost: {Day_Cost:<6s}")
TotalCost = "${:,.2f}" .format(TotalCost)
print(f"   Total Cost: {TotalCost:<8s}")




