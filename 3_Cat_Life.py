# 6 човешки месеца се равняват на 1 котешки месец
import math

cat_breed = input() #"British Shorthair", "Siamese"
gender_cat = input() #f or m

result = 0

if cat_breed == "British Shorthair":
    if gender_cat == "m":
        result = math.floor(13 * 12) / 6
    elif gender_cat == "f":
        result = math.floor(14 * 12) / 6
    print(f"{math.floor(result)} cat months")
elif cat_breed == "Siamese":
    if gender_cat == "m":
        result = math.floor(15 * 12) / 6
    elif gender_cat == "f":
        result = math.floor(16 * 12) / 6
    print(f"{math.floor(result)} cat months")
elif cat_breed == "Persian":
    if gender_cat == "m":
        result = math.floor(14 * 12) / 6
    elif gender_cat == "f":
        result = math.floor(15 * 12) / 6
    print(f"{math.floor(result)} cat months")
elif cat_breed == "Ragdoll":
    if gender_cat == "m":
        result = math.floor(16 * 12) / 6
    elif gender_cat == "f":
        result = math.floor(17 * 12) / 6
    print(f"{math.floor(result)} cat months")
elif cat_breed == "American Shorthair":
    if gender_cat == "m":
        result = math.floor(12 * 12) / 6
    elif gender_cat == "f":
        result = math.floor(13 * 12) / 6
    print(f"{math.floor(result)} cat months")
elif cat_breed == "Siberian":
    if gender_cat == "m":
        result = math.floor(11 * 12) / 6
    elif gender_cat == "f":
        result = math.floor(12 * 12) / 6
    print(f"{math.floor(result)} cat months")

else:
    result = "invalid"
    print(f"{cat_breed} is invalid cat!")

