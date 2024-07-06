num1=int(input("enter the first number="))
num2=int(input("enter the second number="))
ch=int(input("enter the choice from 1 to 4="))

if ch==1:
 print ("sum=",num1+num2)
elif ch==2:
 print ("sub=",num1-num2)
elif ch==3:
 print ("mul=",num1*num2)
elif ch==4:
 print ("div=",num1/num2)
else:
 print ("choice is wrong")
