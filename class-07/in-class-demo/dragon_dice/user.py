import random
from collections import Counter


class User:
    def __init__(self, username):
        self.username = username
        self.hp = random.randint(80, 100)

    @staticmethod
    def sword_attack(dice_roll: tuple) -> int:  # (1, 2, 3, 4, 5, 6)
        """
        Consistent damage, but less than fireball. Deals 2 times the sum
        of the roll
        :param: dice_roll: A tuple of integers representing a dice roll.
        :return: An Integer, representing damage dealt to the enemy.
        """
        return 2 * sum(dice_roll)

    @staticmethod
    def fireball_attack(dice_roll: tuple) -> int:
        """
        More damage than sword_attack
        :param: dice_roll: A tuple of integers representing a dice roll.
        :return: An Integer, representing damage dealt to the enemy.
        """
        dice_counter = Counter(dice_roll)
        damage = 0

        for dice_value, count in dice_counter.items():
            if count == 2:
                damage += dice_value * 10
        return damage

    def heal(self, dice_roll: tuple) -> None:
        """
        Heals user, by the sum of the dice_roll
        :param dice_roll: A tuple of integers representing a dice roll.
        :return: None.
        """
        # TODO: Add in some kind of cost to use heal. Maybe a limited supply of dice?
        self.hp += sum(dice_roll)

    def receive_damage(self, damage: int) -> None:
        """
        Method for user to receive damage from the enemy
        :param damage:
        :return: None.
        """
        self.hp -= damage
