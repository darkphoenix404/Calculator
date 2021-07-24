try:
    print("\nChoose any Option: + , - , * , /\n")
    user1 = int(input("Enter the First Number: "))
    user2 = int(input("Enter the Second Number: "))
    symbol = input("What you want to do?  ")
    if(symbol == "+"):
        print(f"The Sum of {user1} and {user2} is " + str(user1+user2))
    elif(symbol == "-"):
        print(f"The Subtraction of {user1} and {user2} is " + str(user1-user2))
    elif(symbol == "*"):
        print(f"The Multiplication of {user1} and {user2} is " + str(user1*user2))
    elif(symbol == "/"):
        print(f"The Division of {user1} and {user2} is " + str(user1/user2))
    else:
        print("Enter a Vaild Number!")
except:
    print("Something Went Wrong, Try Again Later!")