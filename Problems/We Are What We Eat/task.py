# the list "meals" is already defined
# your code here
meals = [
        {"title": "Oatmeal pancakes with apple and cinnamon", "kcal": 370},
        {"title": "Italian salad with fusilli and ham", "kcal": 320},
        {"title": "Bulgur with vegetables", "kcal": 350},
        {"title": "Curd souffle with lingonberries and ginger", "kcal": 225},
        {"title": "Oatmeal with honey and peanuts", "kcal": 440}]
calories = 0
for meal in meals:
    for key in meal:
        if key == 'kcal':
            calories += meal['kcal']
        else:
            continue
print(calories)