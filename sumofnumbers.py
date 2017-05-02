#Write a program that asks the user for a number n and prints
# the sum of the numbers 1 to n

#Since we have Gauss's formula which says that the sum of all natural numbers from 1 to n is n(n+1)/2 then we can make this algorithm
#linear so it is a lot more efficient.

n = int(input("Enter a number"))

print(" The sum is", n*(n+1)/2)
