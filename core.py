import requests
import json

def Fetch_Nutritions(food):
    name = food.name
    weight = food.weight
    ingr = f"{food.weight}g {food.name}"
    ingr = ingr.replace(" ","%20")
    url = f"https://api.edamam.com/api/nutrition-data?app_id=d87e3e83&app_key=d47ce3ba1b6049cf82fe9b9d8c2d9f41&ingr={ingr}"
    req = requests.get(url)
    if req.status_code == 200:
        data = req.json()
    else:
        raise TypeError(f"{food.name} cannot be found.")

    return data

class Food:
    def __init__(self,name,weight):
        if not name.replace(" ","").isalpha():
            raise ValueError(f"The name {name} is not valid.\n make sure that the name is in English.")
        if not isinstance(weight,(int,float)):
            raise TypeError(f"Weight needs to be a number.")
        if weight<=0:
            raise ValueError(f"Illegal weight, please re-enter.")
        self.name = name
        self.weight = weight
        data = Fetch_Nutritions(self)
        self.calories = data['ingredients'][0]['parsed'][0]['nutrients']['ENERC_KCAL']['quantity']
        self.sugar = data['ingredients'][0]['parsed'][0]['nutrients']['SUGAR']['quantity']
        self.protein = data['ingredients'][0]['parsed'][0]['nutrients']['PROCNT']['quantity']
        self.fat = data['ingredients'][0]['parsed'][0]['nutrients']['FAT']['quantity']

banana = Food("banana",150)
print(f"There is {banana.protein} protein in 150g of banana")