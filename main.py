def game_guide():
     print("Welcome to Adi's Bot game")
def game_logic(goal):
     while True:
        input_number = int(input("Enter the number:"))

        if input_number == 25:
            print("You won the game")
        else:  
            print("You lost the game")
            break

goal = "More than 25"
def main():
    goal = 35
    game_guide()
    game_logic(goal)


if __name__ == "__main__":
    main()
