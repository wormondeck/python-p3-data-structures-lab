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
    
def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food['heat_level'] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        spicy_formatted = f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"] * "🌶"}'      
        print(spicy_formatted)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    # using single inline for readability
    return next((food for food in spicy_foods if food['cuisine'] == cuisine))
    #  for loop with if statement works as well:
    #  for food in spicy_foods:
    #      if food['cuisine'] == cuisine:
    #         return food 

def print_spiciest_foods(spicy_foods):
    for food in spicy_foods:
        if food['heat_level'] > 5:
            print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {food["heat_level"] * "🌶"}')

def get_average_heat_level(spicy_foods):
    return int(sum(food['heat_level'] for food in spicy_foods) / len(spicy_foods))

    # value = 'heat_level'
    # total_sum = sum(key[value] for key in spicy_foods)
    # average_heat = int(total_sum / len(spicy_foods))
    # return average_heat

def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods.append(spicy_food)
    return spicy_foods    