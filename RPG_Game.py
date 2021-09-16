import random
import time


def random_num():
    return random.randrange(1, 20)


class Warrior:
    def __init__(self, name="", hp=0):
        self.name = name
        self.hp = hp


class Battle:
    def turn(self, attacker, defender):
        attack = random_num()
        block = random_num()
        defender.hp -= max(attack - block, 0)

        print(f"{attacker.name} attacked {defender.name} and dealt {attack} demage. {defender.name} blocked {block} demage.")
        print(f"{attacker.name} left with {attacker.hp} Health Points || {defender.name} left with {defender.hp} Health Points\n")
        time.sleep(0.5)

    def start_fight(self, warrior_One, warrior_Two):
        while(True):
            Battle().turn(warrior_One, warrior_Two)
            if(warrior_Two.hp <= 0):
                print(f"{warrior_Two.name} won!")
                break

            Battle().turn(warrior_Two, warrior_One)
            if(warrior_One.hp <= 0):
                print(f"{warrior_One.name} won!")
                break


def main():
    while(True):
        print("Press enter to start the game!")
        input()

        print("Name of the first warrior: ")
        first_warrior = input()
        print("Name of the second warrior: ")
        second_warrior = input()
        print()

        player_one = Warrior(f"{first_warrior}", 20)
        player_two = Warrior(f"{second_warrior}", 20)

        Battle().start_fight(player_one, player_two)

        print("Wish to play again? y/n")
        answer = input()
        if(answer.lower() == "n"):
            print("End Game")
            input()
            quit()


main()
