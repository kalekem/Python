
#Error handling

def divideByZeroError(divide):
    try:
        return 45/divide;

    except ZeroDivisionError:
        print("Erro! Invalid Arguments!");

print (divideByZeroError(5));
print (divideByZeroError(0));
print (divideByZeroError(9));
print (divideByZeroError(2));
print (divideByZeroError(0));
        
