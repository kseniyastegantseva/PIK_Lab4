from unittest.mock import Mock

from drinks import Coffee, CoffeeMaker, Tea, TeaMaker


def test_tea_maker_creates_tea():
    assert isinstance(TeaMaker().create_drink(), Tea)
    assert TeaMaker().make_drink() == "Чай готов"


def test_coffee_maker_creates_coffee():
    assert isinstance(CoffeeMaker().create_drink(), Coffee)
    assert CoffeeMaker().make_drink() == "Кофе готов"


def test_make_drink_calls_prepare():
    drink = Mock()
    drink.prepare.return_value = "Напиток готов"
    maker = TeaMaker()
    maker.create_drink = Mock(return_value=drink)

    assert maker.make_drink() == "Напиток готов"
    maker.create_drink.assert_called_once_with()
    drink.prepare.assert_called_once_with()
