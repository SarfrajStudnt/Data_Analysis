def addition(num1, num2):
    return num1+num2
def subtr(num1, num2):
    return num1-num2
def mult(num1, num2):
    return num1*num2
def dev(num1, num2):
    return num1/num2
def mod(num1, num2):
    return num1%num2
def add(num1, num2, num3, num4):
     return num1+num2+num3+num4
def substract(num1,num2,num3,num4):
     return (num1+num2)-(num3+num4)
def multiple(num1,num2,num3,num4):
    return num1*num2*num3*num4
def devide(num1,num2,num3,num4):
    return (num1+num2)/(num3+num4)
def module(num1,num2,num3,num4):
    return (num1+num2)%(num3+num4)
def exit():
    return 0
while(True):
    print('Welcome to the lybrary :')
    choice = input('now you can chose the option. +: for addition, -: for substract, *: for multiply, /: for devide, %: for modules ')
    list = [0,1,2,3,4,5]
    print("how many time of calculation you're going to perform :", list)
    choose = list[int(input())]
    if choose <= 2:
        print('Welcome to the calculation world :')
        num1 = int(input("Enter your first num :"))
        num2 = int(input("Enter your secound number :"))
        if choice == '+':
            print('The sum of two number :', addition(num1, num2))
            next_cal = input("If you want to do next Calculation, type y/n ")
            if next_cal == 'n':
                break
        elif choice == '-':
            print("The substraction of two number is :", subtr(num1, num2))
            next_cal = input("If you want to do next Calculation, type y/n ")
            if next_cal == 'n':
                break
        elif choice == '*':
            print("The multiple of two number is :", mult(num1,num2))
            next_cal = input("If you don't want to do next Calculation, type y/n ")
            if next_cal == 'n':
                break
        elif choice == '/':
            print('The devision between two number is :', dev(num1, num2))
            if next_cal == 'n':
                break
        elif choice == '%':
            print('The modulus of two number is :', mod(num1, num2))
    else:
        print('SORRY YOU HAVE TYPED WRONG : if you want to exit type yes', exit() )

    print("how many time of calculation you're going to perform :", list)
    choose = list[int(input())]
    if choose <= 4:
        num1 = int(input("Enter your first num :"))
        num2 = int(input("Enter your secound number :"))
        choice = input('now you can chose the option. +: for addition, -: for substract, *: for multiply, /: for devide, %: for modules ')
        num3 = int(input("Enter your third number :"))
        num4 = int(input("Enter your fourth number :"))
    else:
        print("Please enter only visible instruction :")
    if choice == '+':
        print('The sum of number :', add(num1, num2, num3, num4))
        next_cal = input("If you  want to do next Calculation, type y/n ")
        if next_cal == 'n':
             break
    elif choice == '-':
        print("The substraction of two number is :", substract(num1, num2, num3, num4))
        next_cal = input("If you want to do next Calculation, type y/n ")
        if next_cal == 'n':
             break
    elif choice == '*':
        print("The multiple of two number is :", multiple(num1, num2, num3, num4))
        next_cal = input("If you want to do next Calculation, type y/n ")
        if next_cal == 'n':
             break
    elif choice == '/':
        print('The devision between two number is :', devide(num1, num2, num3, num4))
    else:
        print('worng typed :')
    chosen = input('if you want to quit this game , type Yes')
    if chosen == 'Yes':
        break
        exit()