"""
Write a program to input three numbers and swap them as this :
1st number becomes the 2nd number, 2nd number becomes the 3rd number
and 3rd number becomes the first number.
"""
n1=int(input("Enter number 1 : "))
n2=int(input("Enter number 2 : "))
n3=int(input("Enter number 3 : "))
print("Original Number : ",n1,n2,n3)
n1,n2,n3=n2,n3,n1
print("After Swapping : ",n1,n2,n3)
