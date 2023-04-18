#ABC Payroll
#Author Brandon Connolly
#Due Date Sept 23

#Currant Rates & Taxes
HrRate = 17.50
ItemRate = 35
Union = 15
IncomeTax = .21
CPP = .0495
EI = .016

#Input information
EmployeeName = input("Enter Employee Name: ")
HrsWorked = input("Enter Hours worked: ")
HrsWorked = float(HrsWorked)
ItemsProd = input("Enter Number of Products Produced: ")
ItemsProd = float(ItemsProd)
Bonus = input("Enter Total of Bonus Issued: ")
Bonus = float(Bonus)

#Calculations

CommPay = ItemRate * ItemsProd
HrPay = HrRate * HrsWorked
Grosspay = HrPay + CommPay + Bonus
IncomeDed = Grosspay * IncomeTax
CPPDed = Grosspay * CPP
EIDed = Grosspay * EI
TotalDed = IncomeDed + CPPDed + EIDed + Union
NetPay = Grosspay - TotalDed

#Printed Information
print(f"   Employee Name: {EmployeeName:<8s}")
ItemsProd = "{:,.2f}".format(ItemsProd)
print(f"   Total Products Produced: {ItemsProd:<4s}")
HrPay = "${:,.2f}".format(HrPay)
print(f"   Total Hourly Pay: {HrPay:<9s}")
CommPay = "${:,.2f}".format(CommPay)
print(f"   Total Commission: {CommPay:<9s}")
Grosspay = "${:,.2f}".format(Grosspay)
print(f"   Gross Pay: {Grosspay:<9s}")
IncomeDed = "${:,.2f}".format(IncomeDed)
print(f"   Total Income Tax: {IncomeDed:<9s}")
CPPDed = "${:,.2f}".format(CPPDed)
print(f"   Total CPP Contribution: {CPPDed:<9s}")
EIDed = "${:,.2f}".format(EIDed)
print(f"   Total EI Contribution: {EIDed:<9s}")
Union = "${:,.2f}".format(Union)
print(f"   Union Dues: {Union:<3s}")
TotalDed = "${:,.2f}".format(TotalDed)
print(f"   Total Deductions: {TotalDed:<9s}")
NetPay = "${:,.2f}".format(NetPay)
print(f"   Total Net Pay: {NetPay:<10s}")
