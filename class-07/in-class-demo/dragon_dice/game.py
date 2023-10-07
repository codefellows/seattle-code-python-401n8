from dragon_dice.game_logic import GameLogic as GL
from dragon_dice.user import User
from dragon_dice.monster import Dragon


def start_fight():
    print("Welcome Adventurer!")
    print("Today's quest is to fight the evil dragon Smaug!")
    print("")
    username = input("Enter your name: ")
    return username


def sword_fireball_heal_run(user):
    while True:
        print("sword, fireball, heal, or run?")
        choice = input("> ")
        if choice == "sword":
            return user.sword_attack
        if choice == "fireball":
            return user.fireball_attack
        if choice == "heal":
            return user.heal
        if choice == "run":
            fight_over("run")


def fight_over(outcome):
    if outcome == "run":
        print("You ran from the fight.")

    if outcome == "win":
        print("You won! congrats")

    if outcome == "lost":
        print("You have died.")

    exit()


# this is where the gameplay loop is
def play():
    username = start_fight()
    user = User(username)
    smaug = Dragon("Smaug", 90, 80)
    turn = 1

    # start of the turn
    while True:
        print(f"***** Turn {turn} *****")
        print(f"Enemy health is {smaug.hp}hp")
        print(f"{user.username}'s health is {user.hp}hp")

        player_choice = sword_fireball_heal_run(user)  # a method: either sword_attack, fireball_attack, heal or run
        num_dice = int(input("Enter number of dice: "))
        damage_done = player_choice(GL.roll_dice(num_dice))  # uses the number of dice, and the dice roller method

        if damage_done:
            smaug.receive_damage(damage_done)

        if smaug.hp <= 0:
            fight_over("win")

        enemy_damage_done = smaug.attack()
        user.receive_damage(enemy_damage_done)

        if user.hp <= 0:
            fight_over("lost")

        turn += 1


if __name__ == "__main__":
    play()
