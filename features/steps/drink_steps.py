from behave import given, when, then

from drinks import CoffeeMaker, TeaMaker


@given("выбран чай")
def choose_tea(context):
    context.maker = TeaMaker()


@given("выбран кофе")
def choose_coffee(context):
    context.maker = CoffeeMaker()


@when("напиток приготовлен")
def make_drink(context):
    context.result = context.maker.make_drink()


@then('результат должен быть "{expected}"')
def check_result(context, expected):
    assert context.result == expected
