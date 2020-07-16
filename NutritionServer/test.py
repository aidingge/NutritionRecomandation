import csv
import os
from mainApp.models import Occupation, FoodMaterial, Menu, CookQuantity, MenuClassification, Physique
base_dir = 'D:/program/pycharm/workspace/NutritionMasterSpider/data/心食谱/'

csv_list = os.listdir(base_dir)
for file in csv_list:
    file_path = base_dir + '/' + file
    import pandas as pd

    table = pd.read_csv(file_path, encoding='utf-8')
    for i in range(len(table)):
        menu = table.loc[i]['name']
        materials = str(table.loc[i]['materials'])
        dic = {}
        materials = materials.strip()
        materials_list = materials.split(',')
        for s in materials_list:
            if not s.__eq__(''):
                ma = s.split(':')
                if len(ma) != 2:
                    continue
                quantity = ma[0]
                name = ma[1]
                dic[name] = quantity
        for material_name, quantity_str in dic.items():
            food_material = FoodMaterial(material_name=material_name)
            food_material.save()
            cook_quantity = CookQuantity(quantity=quantity_str, material_id=food_material, menu_id=menu)
            try:
                cook_quantity.save()
            except Exception as e:
                pass