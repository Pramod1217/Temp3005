# Assignment -4
item=input("Enter item name :")
sp_cost=float(input("How much is selling price of item: "))
cgst_rate=float(input("What is CGST rate %: "))
sgst_rate=float(input("What is SGST rate %: "))
cgst = sp_cost*(cgst_rate/100)
sgst = sp_cost*(sgst_rate/100)
print("CGST (@",cgst_rate,"%) :",(cgst))
print("SGST(@",sgst_rate,"%) :",(sgst))
amt=sp_cost+cgst+sgst
print("Amount payable: ",(amt))
