a = int(input("Enter the first number : "))
b = int(input("Enter the Second number : "))

ch = int(input("Enter the choice you want :" \
" 1 - ADD ," \
" 2 - SUBTRACT," \
" 3 - MULTIPLY," \
" 4 - DIVIDE "
" :: "))

if ch == 1:
    print("Addition is : ", a+b)
elif ch == 2:
    print("Subtraction is :", a-b)
elif ch == 3:
    print("Multiplication is : ", a*b)
elif ch == 4:
    print("Division is : ", a/b)
else :
    print("Invalid choice")

    