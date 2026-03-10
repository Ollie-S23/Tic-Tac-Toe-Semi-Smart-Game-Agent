import random

class enemy_agent:

    def __init__(self):
        pass

    def check_board_state(self):
        smartChance = random.randint(0,1) #binary options: 0,1
        #dumb result - put random place
        if (smartChance == 0):
            print("check_board_state was 0. No smart")
            choice = random.randint(0,8) #0 - 8 (9 options)
            print(choice)
        #smart result - check board condition
        else:
            print("check_board_state was 1. Yes smart")







def main():
    
    game_status = "play"

    while (game_status == "play"):
        enemy = enemy_agent()
        enemy.check_board_state()
        break

if __name__ == "__main__":
    main()