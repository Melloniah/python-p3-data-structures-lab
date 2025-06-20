spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]
print(get_names(spicy_foods))   


def get_spiciest_foods(spicy_foods):
   

    spiciest_food=[]
    for food in spicy_foods: 
        if food["heat_level"]>=5:
           
            spiciest_food.append(food)
    return spiciest_food




def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")
        


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    food_cuisine=[]
    for food in spicy_foods:
        if food["cuisine"]==cuisine:

            return food

def print_spiciest_foods(spicy_foods):
    spiciest=[]
    for food in spicy_foods:
        if food["heat_level"]>5:
             print(f"{food['name']} ({food['cuisine']}) | Heat Level: {'🌶' * food['heat_level']}")

def get_average_heat_level(spicy_foods):
    total=sum(food["heat_level"] for food in spicy_foods)
    return total//len(spicy_foods)

def create_spicy_food(spicy_foods, new_spicy_food):
    spicy_foods.append(new_spicy_food)
    return spicy_foods
