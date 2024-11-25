#while loop
dog_food_bought_kg = int(input())

dog_food_bought_grams = 0
dog_food_grams = 0
command = input()

dog_food_bought_grams = dog_food_bought_kg * 1000
current_grams = 0
while command != "Adopted":
    dog_food_grams = int(command)

    current_grams += dog_food_grams
    command = input()

if dog_food_bought_grams >= current_grams :
    left_food = dog_food_bought_grams - current_grams
    print(f"Food is enough! Leftovers: {left_food} grams.")
else:
    needed_food = current_grams - dog_food_bought_grams
    print(f"Food is not enough. You need {needed_food} grams more.")