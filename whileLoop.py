
#asks the user the enter the password

print("Hi there! Welcome to Kalekem's Incorpprated!");

paswd = "CLEO@";

print("Enter your name : " );
name = input();

print("Your name is "+ name);

print("Please enter the password: ");
password = input();

#check if the passwords match.
#If not, continue asking the user to enter the password

while (password !=paswd ):
    print("Incorrect password. Please enter password");
    password = input();

print ("Access granted!");
    
    


