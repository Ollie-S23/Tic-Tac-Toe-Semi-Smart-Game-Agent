import random

class enemy_agent:

    def __init__(self):
        pass

    def check_board_state(self, freeSpots):
        smartChance = random.randint(0,1) #binary options: 0,1
        #dumb result - put random place
        if (smartChance == 0):
            print("check_board_state was 0. No smart")
            while(True):
                choice = random.randint(0,8) #0 - 8 (9 options)
                if (choice in freeSpots):
                    freeSpots.remove(choice)
                    print(freeSpots)
                    break
            print(choice)
        #smart result - check board condition
        else:
            print("check_board_state was 1. Yes smart")







def main():
    
    game_status = "play"
    freeSpots = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    while (game_status == "play"):
        enemy = enemy_agent()
        freeSpots = [0, 3, 5, 7]
        enemy.check_board_state(freeSpots)
        break

if __name__ == "__main__":
    main()