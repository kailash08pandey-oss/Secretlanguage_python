#code language
import random
letters=("QWERTYUIOPLKJHGFDSAMNBVCXZqwertyuiopasdfghjklzxcvbnm")


#asking user for encoding or decoding
E_or_D=input("Type \"E\"for encoding and Type \"D\" for decoding:").lower()
if E_or_D.lower() == "e":
    msg=input("Enter your message for encoding : ")


#code for encoding message <=3
    if len(msg)<=3:
        x= (msg[::-1])
        print("Here is your encoded message:",x )

    
#code for encoding message >3
    else:
        x=""
        y=""
        for i in range(4):
            x+=random.choice(letters) 
            y+=random.choice(letters) 
        z= msg[1:]+msg[0]
    print("Here is your encoded message:  ",x+z+y)


#code for decoding
elif E_or_D.lower()== "d":
    print("WARNING: This program can decode only those message which are encodedby this program!!!!!\n\n")
    msg=input("Enter your message for decoding : ")


# code for decoding messaage<=
    if len(msg)<=3:
        print("Here is decoded message:  ", msg[::-1] )
    else:
        x= msg[4:-4]
        y=x[-1]+x[:-1]
        print("Here is your decoded message: ",y)


else:
    print("Wrong command and run again\n Please give command care fully , the program only takes (\"E\",\"D\")commands ")


         
