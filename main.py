#QAP 4 Graph
#Author Brandon Connolly



import matplotlib.pyplot as pit
import matplotlib.pyplot as plt

JanCl = input("Please Enter Claim Amount For Jan: ")
FedCl = input("Please Enter Claim Amount For Feb: ")
MarCl = input("Please Enter Claim Amount For Mar: ")
AprCl = input("Please Enter Claim Amount For Apr: ")
MayCl = input("Please Enter Claim Amount For May: ")
JunCl = input("Please Enter Claim Amount For Jun: ")
JulCl = input("Please Enter Claim Amount For Jul: ")
AugCl = input("Please Enter Claim Amount For Aug: ")
SepCl = input("Please Enter Claim Amount For Sep: ")
OctCl = input("Please Enter Claim Amount For Oct: ")
NovCl = input("Please Enter Claim Amount For Nov: ")
DecCl = input("Please Enter Claim Amount For Dec: ")


x_axis = ["Jan", "Fed", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
y_axis = [JanCl, FedCl, MarCl, AprCl, MayCl, JunCl, JulCl,  AugCl, SepCl, OctCl, NovCl, DecCl]

plt.plot(x_axis , y_axis)
plt.xlabel("Month of Year")
plt.ylabel("Amount of Claims($)")
plt.title("Yearly Claim Amounts($)")
plt.grid(True)

plt.show()