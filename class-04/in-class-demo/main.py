from dog_pack.dogs import Lab


def main():
    rosko = Lab("Rosko")
    rosko_2 = Lab("Rosko 2")
    print(rosko.name)
    print(rosko)
    print(rosko_2)  # different memory address
    print()
    print(repr(rosko))
    print(repr(rosko_2))

    # class variable
    print(Lab.scientific_name)

    # class method
    print(Lab.give_scientific_name())


if __name__ == "__main__":
    main()
