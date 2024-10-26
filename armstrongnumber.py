inputfromuser=int(input("enter the value you want to check "))
sum=0
inputincode=inputfromuser
while(inputincode>0):
    digit=inputincode%10
    sum=sum+digit**3
    inputincode=inputincode//10
if (sum==inputfromuser):
    print("it is an armstrong number")
else:
    print("it is not a armstrong number")
    