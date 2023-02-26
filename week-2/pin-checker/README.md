# PIN Number Challenge
Little program using conditionals and checking user input 

Task particulars:
To write a Python program that emulates high-street bank mechanism for checking a PIN. Keep taking input fromm the keyboard (see below) until it is identical to a password number which is hard-coded by you in the program.

To output a prompt and read from the keyboard:
'supplied_pin = input("Enter your PIN: ")'

Restrick the number of attempts to 3 (be sure to use a variable for that, we may wish to change it later), and output a suitable message for success and failure. Be sure to include the number of attempts in the message.



Optional: 
PAsswords and PINs, would not normally be displayed (echoed) to the creen, for security reasons. So now we will add the functionality to hide the characters typed. That could be a lot of work, but one of the advantages of using a language like Python is that "there's a module for it".

You will need to import a module called getpass, which is part of the standard library.

Instead of input use getpass.getpass in the same place in the program, with the same parameters.
