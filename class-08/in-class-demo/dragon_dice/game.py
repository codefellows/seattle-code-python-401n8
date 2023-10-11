from dragon_dice.game_logic import GameLogic as GL
from dragon_dice.user import User
from dragon_dice.monster import Dragon


def start_fight():
    print("Welcome Adventurer!")
    print("Today's quest is to fight the evil dragon Smaug!")
    print("")
    print("Enter your name")
    username = input("> ")
    return username


def sword_fireball_heal_run(user):
    """
    Allows the user to choose an action between sword, fireball, heal or run
    :param user: a reference to a User instance
    :return: A reference to a user method, or ends the fight with `fight_over`
    """
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
def play(roller=GL.roll_dice):
    username = start_fight()
    user = User(username)
    smaug = Dragon("Smaug", 90, 80)
    turn = 1

    # start of the turn
    while True:
        print(f"\n***** Turn {turn} *****")
        print(f"Enemy health is {smaug.hp}hp")
        print(f"{user.username}'s health is {user.hp}hp")

        player_choice = sword_fireball_heal_run(user)  # a method: either sword_attack, fireball_attack, heal or run
        print("Enter number of dice")
        num_dice = int(input("> "))
        rolled_dice = roller(num_dice)
        print(f"You rolled {rolled_dice}")
        damage_done = player_choice(rolled_dice)  # uses the number of dice, and the dice roller method

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
    # test_instance = GL([(1, 1, 2, 2, 3, 3), (1, 2, 3, 4, 5, 6)])
    # play(test_instance.mock_roller)
    play()
