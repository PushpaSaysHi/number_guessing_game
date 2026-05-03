import random

#generates random number
random_int = random.randint(1,100)

input_num = int(input("enter your number(100 limit): "))
#loops the input until the number has been guessed
while True:
    #checking condition 
    if random_int < input_num:
        print("Guess is high")
        input_num = int(input("Try Again!!! : "))
       
    elif random_int > input_num:
        print("Guess is low")
        input_num = int(input("Try Again!!! : "))
    # exits the loop    
    else:
        break
    
print(f"Congralutaions!!!. The winning number was {random_int}")
