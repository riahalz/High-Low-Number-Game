import random

NUM_ROUNDS = 5

def main():
    print("Welcome to the High-Low Number Game!")
    print("You will get a random number. You must guess if that number is higher or lower than the computer's randomly generated number. \n")

    # User's score
    your_score = 0

    # 5 Rounds
    for i in range(NUM_ROUNDS):
        print("Round", i + 1)
        
        # Generate the random numbers and print them out
        computer_num = random.randint(1, 100)
        your_num = random.randint(1, 100)
        print("Your number is", your_num)

        # Get user input 'higher' or 'lower'
        choice = input("Do you think your number is higher or lower than the computer's?: ")

        while choice != "higher" and choice != "lower":
            choice = input("Please enter either higher or lower: ")

        # Check if number is higher or lower
        higher_and_correct = choice == "higher" and your_num > computer_num
        lower_and_correct = choice == "lower" and your_num < computer_num

        if higher_and_correct or lower_and_correct:
            print("You are right! The computer's number is", computer_num)
            your_score += 1 
        else: 
            print("That's incorrect. The computer's number is", computer_num)

        # Update score
        print("Your score is now ", your_score)
        print()
    
    # Print messages based on user's performance
    print("Your final score is", your_score, "/5")

    if your_score == NUM_ROUNDS:
        print("Well done! You got a perfect score!")
    elif your_score > NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
