#-------------------------------------
#Author Adam Hussain
#Print out the first 100 even numbers
#------------------------------------
counter = 1;
odd = 0;
while odd < 100:
    if counter%2 == 0:
        print counter;
        odd = odd + 1;
        counter = counter + 1;
    else:
        counter = counter + 1;
