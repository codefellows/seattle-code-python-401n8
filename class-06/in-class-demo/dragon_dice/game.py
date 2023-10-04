from dragon_dice.game_logic import GameLogic as GL


# this is where the gameplay loop is
def play():
    dragon_health = 100

    # add welcome message

    while True:
        if dragon_health <= 0:
            print("The Dragon has been defeated! You win!")
            break

        num_dice = input("Enter number of dice:")

        dice_roll = GL.roll_dice(int(num_dice))
        print(f"You rolled: {dice_roll}")

        damage_dealt = GL.calculate_damage(dice_roll)
        print(f"You dealt {damage_dealt} damage!")

        dragon_health -= damage_dealt


if __name__ == "__main__":
    play()
