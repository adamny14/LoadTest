#------------------------------
# Adam Hussain
# print a triangle of stars for n
#------------------------------
n = input("Enter number n: ");
counter = 1;

while counter <= n:
    print " "*(n-counter) +"*"*counter ;
    counter = counter +1;
