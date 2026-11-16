from drinks import CoffeeMaker, TeaMaker


def main():
    print("1 — чай")
    print("2 — кофе")
    choice = input("Выберите напиток: ")

    if choice == "1":
        maker = TeaMaker()
    elif choice == "2":
        maker = CoffeeMaker()
    else:
        print("Такого напитка нет")
        return

    print(maker.make_drink())


if __name__ == "__main__":
    main()
