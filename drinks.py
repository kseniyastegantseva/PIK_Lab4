class Tea:
    def prepare(self):
        return "Чай готов"


class Coffee:
    def prepare(self):
        return "Кофе готов"


class DrinkMaker:
    def create_drink(self):
        raise NotImplementedError

    def make_drink(self):
        drink = self.create_drink()
        return drink.prepare()


class TeaMaker(DrinkMaker):
    def create_drink(self):
        return Tea()


class CoffeeMaker(DrinkMaker):
    def create_drink(self):
        return Coffee()
