#Книгата се състои от 899 страници и 2 корици
#намаление (в проценти)
#трябва да се заплати на дизайнер

price_per_page = float(input())
price_per_cover = float(input())
discount_for_printing = int(input())
price_for_designer = float(input())
percent_from_total_price_paid_by_team = int(input())

start_price_for_printing = (price_per_page * 899) + (price_per_cover * 2)
discounted_price_for_printing = start_price_for_printing * (1 - (discount_for_printing / 100))
costs_with_designer = discounted_price_for_printing + price_for_designer

total_price = costs_with_designer * (1 - (percent_from_total_price_paid_by_team / 100))

print(f"Avtonom should pay {total_price :.2f} BGN.")