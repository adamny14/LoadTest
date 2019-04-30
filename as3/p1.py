#----------------------------
#Author Adam Hussain
# Print a triangle of size n
#----------------------------
n = input("Enter a number n: ");
counter = 0;
while counter < n:
    print "*"* (n - counter);
    counter = counter + 1;
