import sys

#The user must enter "exit" to end the program

while True:
    print("Type 'exit' to exit");

    response = input();

    if(response == "exit"):
        sys.exit();

    print("You typed "+ response + ".");
