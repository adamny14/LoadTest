#----------------------------------
#Author Adam Hussain
#Print first 50 prime number
#----------------------------------
def isPrime(n): 
    x = 2; 
    while x < n: 
        if n%x==0:              
            x = x + 1; 
            return False;
        else: 
            x = x+1; 
    return True; 

#main program
counter = 1;
prime = 0;
while prime <= 50:
    if isPrime(counter):
        print counter;
        prime = prime + 1;
        counter = counter + 1;
    else:
        counter = counter + 1;
