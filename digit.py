character=input("Enter the character:")

if ((character >= 'a' and character <= 'z') or (character >= 'A' and character <= 'Z')):
    print("ALPHABET.")
    
elif (character >= '0' and character <= '9'):
   print("DIGITS")
   
else :
   print ("SPECIAL CHARACTER")