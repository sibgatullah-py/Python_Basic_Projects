import os

from utils import Calculator

def clear(): # clear screen method
    os.system('cls' if os.name == 'nt' else 'clear')
    
calc = Calculator()

while True:
    print("\n1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choose = input("Select Option: ")
    
    if choose == '5':
        break
    
    n1 = float(input("First number: "))
    n2 = float(input("Second number: "))
    
    if choose == '1':
        print("Result: ",calc.addition(n1,n2))
        
    elif choose == '2':
        print("Result: ", calc.subtraction(n1,n2))
        
    elif choose == '3':
        print("Result: ",calc.multiplication(n1,n2))
        
    elif choose == '4':
        print("Result: ",calc.division(n1,n2))
    
    else:
        print("Invalid Option!")
        
    input("\nPress Enter to continue...")  # Wait before clearing
    clear()  # Clear AFTER result