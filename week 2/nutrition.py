item = input("Item: ").lower()

fruit = {"apple": 130,
         "avocado": 50,
         "grapefruit": 60,
         "sweet cherries": 100,
         "kiwifruit": 90,
         "pear": 100} # add fruits in list if needed

for i in fruit:
    if item == i:
        print("Calories:", fruit[i])
# check50 cs50/problems/2022/python/nutrition
# submit50 cs50/problems/2022/python/nutrition