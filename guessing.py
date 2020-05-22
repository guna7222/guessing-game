# Guessing game
secret_number = 8
count = 0
max_attempts = 3
while count < max_attempts:
    user_input = int(input('Guess:- '))
    count = count+1

    if user_input == secret_number:
        print(f'Hey you won secret_number is {user_input}')
        break

    elif user_input != secret_number:
        if count == 1:
            print("you have 2 chances")
        elif count == 2:
            print("you have last chace")

else:
    print("Good Try Smile!...")


