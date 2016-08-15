##program to check if an entry is a phone number

def isPhone(text):
    if len(text) != 12:
        return False;
    
    for i in range (0, 3):
        if not text[i].isdecimal():
            return False;

    if text[3] != "-":
            return False;

    for i in range (4, 7):
        if not text[i].isdecimal():
            return False;

    if text[7] != "-":
            return False;
        
    for i in range (8, 12):
        if not text[i].isdecimal():
            return False;

    return True;

print("781-839-0886 is a phone number? ");
print(isPhone("781-839-0886"));

print("123-677-88987 a phone is a phone number");
print(isPhone("123-677-88987"));

print("Cleophas Kalekem is a phone number");
print(isPhone("Cleophas Kalekem"));

print("78-839-0887 is a phone number? ");
print(isPhone("78-839-0887"));
      
print("123-456-7891 is a phone number? ");
print(isPhone("123-456-7891"));

message = "Call me at 781-839-0886 tomorrow. 415-555-1111 is my office."
for i in range(len(message)):
    phoneNumber = message[i:i+12]
    if isPhone(phoneNumber):
        print("Phone number found: " + phoneNumber);

print("Done & finished!");
    
 
















