from abc import ABC, abstractmethod
import time


class Monster(ABC):
    def __init__(self, name: str, hp: int, attack_power: int) -> None:
        self.name = name
        self.hp = hp
        self.attack_power = attack_power
        self.last_attack = None

    @abstractmethod
    def attack(self):
        pass

    def receive_damage(self, damage: int) -> None:
        """
        Method for monster to receive damage from user.
        :param damage: Integer, representing damage taken
        :return: None
        """
        self.hp -= damage


class Dragon(Monster):
    def attack(self) -> int:
        """
        The dragon's attack method, dealing damage to user.
        Takes 20 seconds before full recharge.
        100% of damage on first attack.
        :return: Integer, representing damage done.
        """
        # first attack
        if self.last_attack is None:
            return self.attack_power

        delta = int(time.time()) - self.last_attack  # how many seconds have passed between attacks
        self.last_attack = int(time.time())  # update self.last_attack with current time

        if delta > 20:
            return self.attack_power
        else:
            return (delta / 20) * self.attack_power


# TODO: add a dictionary of monsters




