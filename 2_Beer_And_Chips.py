#една бира е 1.20 лв., а цената на един пакет чипс е
# равна на 45% от общата стойност на закупените бири.
# Общата цена на чипса да се закръгли до по-голямо число.
import math

football_fan_name = input()
budget = float(input())
number_beers = int(input())
number_packs_chips = int(input())

total_beers_price = number_beers * 1.20
price_per_chips = total_beers_price * 0.45
total_price_chips = math.ceil(price_per_chips * number_packs_chips)

goods_cost = total_price_chips + total_beers_price


if budget >= goods_cost:
    print(f"{football_fan_name} bought a snack and has {(budget - goods_cost):.2f} leva left.")
else:
    print(f"{football_fan_name} needs {(goods_cost - budget):.2f} more leva!")
