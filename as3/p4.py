#-------------------------------------------------------------
# Adam Hussain
# given number n return true if prime and false if composite 
#------------------------------------------------------------
def isPrime(n) : 
    x = 2; 
    while x < n: 
        if n%x==0:              
            x = x + 1; 
            return False;
        else: 
            x = x+1; 
    return True; 

 

#- main program 

num = input("Enter number: "); 
counter = 2; 

while counter <= num: 
    if isPrime(counter): 
        print counter, "is a prime number."; 
    else: 
        print counter, "is a composite number."; 
        counter = counter + 1;
