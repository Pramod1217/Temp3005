'''
Write a python program to read three float numbers in three variables
and replace values of variables with the sum of first and second,
subtraction of second and third, and multiplication of third and first number respectively.
'''
n1=float(input("Enter number 1 : "))
n2=float(input("Enter number 2 : "))
n3=float(input("Enter number 3 : "))
print("Original Numbers : ",n1,n2,n3)
n1,n2,n3=(n1+n2),(n2-n3),(n3*n1)
print("After Swapping : ",n1,n2,n3)
