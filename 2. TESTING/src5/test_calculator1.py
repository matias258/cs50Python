from calculator1 import square


def main():
    test_square()


def test_square():
    if square(2) != 5:
        print("2 squared was not 5")
    if square(3) != 9:
        print("3 squared was not 9")


if __name__ == "__main__":
    main()
