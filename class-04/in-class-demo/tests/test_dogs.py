import pytest
from dog_pack.dogs import Husky, Lab, Dog, DogPack


def test_breed_and_pack_create():
    assert Husky()
    assert Lab()
    assert DogPack()


def test_dog_names():
    brock = Husky("Brock")
    actual = brock.name
    expected = "Brock"
    assert actual == expected


def test_unknown_name():
    random_dog = Lab()
    actual = random_dog.name
    expected = "unknown"
    assert actual == expected


def test_furry():
    dog_1 = Husky()
    dog_2 = Lab()
    expected_1 = dog_1.furry
    actual_1 = True
    expected_2 = dog_2.furry
    actual_2 = True
    # All dogs are furry! regardless of breed!
    assert expected_1 == actual_1
    assert expected_2 == actual_2


def test_all_the_barks():
    carl = Husky("Carl")
    actual = carl.bark()
    expected = "Growl! I'm Carl!"
    assert actual == expected

    sophie = Lab("Sophie")
    actual = sophie.bark()
    expected = "Arf!"
    assert actual == expected


def test_dog_pack():
    brock = Husky("Brock")
    sophie = Lab("Sophie")
    cool_crew = DogPack([brock, sophie], "Cool Crew")
    actual = len(cool_crew.members)
    expected = 2
    assert actual == expected


def test_empty_dog_pack():
    empty_dog_pack = DogPack()
    actual_length = len(empty_dog_pack.members)
    actual_name = empty_dog_pack.name
    expected_length = 0
    expected_name = "unknown"
    assert actual_length == expected_length
    assert actual_name == expected_name


def test_kai_bark(kai):
    assert kai.bark() == "Arf!"


def test_kai_furry(kai):
    assert kai.furry == True


#######################
# Fixtures
#######################


@pytest.fixture
def kai():
    return Lab("Kai")




