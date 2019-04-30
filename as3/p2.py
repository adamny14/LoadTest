#----------------------------------------
#Author Adam Hussain
# Print an upside down triangle of size n
#----------------------------------------
n = input("Enter a number n: ");
counter = 0;
while counter < n:
    print " "*counter + "*" * (n - counter);
    counter = counter + 1;
