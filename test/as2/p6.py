#--------------------------------------
# Author Adam Hussain
# Print prime numbers less than n
#--------------------------------------
def isPrime(n):
        x = 2;
        while x < n:
                if (n%x) == 0:
                        return False;
                        x = x + 1;
                else:
                        x = x +1;
	return True;

num = input("Enter number: ");
counter = 2;
while counter <= num:
	if isPrime(counter):
		print counter;
                counter = counter + 1;
        else:
                counter = counter + 1;
