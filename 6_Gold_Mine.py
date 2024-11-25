# приема броя на локациите и
# очакван среден добив на злато за ден за една локация

number_locations = int(input())

total_gold_digg_days = 0
average_gold_taken = 0
total_days_of_mining = 0

for each_location in range(number_locations):
    average_gold_a_day_expected = float(input())
    days_of_mining = int(input())

    total_days_of_mining += days_of_mining

    for each_day in range(days_of_mining):
        gold_digg_a_day = int(input())

        total_gold_digg_days += gold_digg_a_day
        average_gold_taken = total_gold_digg_days / total_days_of_mining

    if average_gold_taken >= average_gold_a_day_expected:
        print(f"Good job! Average gold per day: {average_gold_taken:.2f}.")
    else:
        gold_not_enough = average_gold_a_day_expected - average_gold_taken
        print(f"You need {gold_not_enough:.2f} gold.")