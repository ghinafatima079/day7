# Write a program that takes a number as input from the user and prints its multiplication table up to 10.
num=int(input("Enter a number:"))
for i in range(1,11):
    print(f"{num}X{i}={num*i}")

# Create a program to calculate the sum of even numbers from 1 to 50 using a while loop.
sum=0
i=2
while i<=51:
    sum+=i
    i+=2
print(f"The sum of even numbers from 1 to 50 is {sum}.")

# Write a program that calculates the factorial of a given number using a for loop.
f=int(input("Enter a number:"))
fact=1
for i in range(1,f+1):
    fact*=i
print(f"The factorial of {f} is {fact}.")

# Write a program that prints the following pattern using nested loops:
rows=int(input("Enter the number of rows:"))
print("The pattern is-")
for i in range(1,rows+1):
    for j in range(1,i+1):
        print("*",end="")
    print()

# Write a program to check if a given number is prime.
# Use a for loop to iterate through possible divisors and break out of the loop if the number is found to be non-prime. 
x=int(input("Enter a number:"))
if x==1:
    print("Not prime")
else:
    for i in range(2,x):
        if x%i==0:
            print(f"{x} is not a prime number.")
            break
    else:
        print(f"{x} is a prime number.")