today_date = input("Qual a data de hoje? ")
breakfast_calories = int(input("\nCalorias do seu Café da manhã: "))
lunch_calories = int(input("\nCalorias do seu almoço: "))
dinner_calories = int(input("\nCalorias da sua janta: "))
snack_calories = int(input("\nCalorias do seu lanche: "))

content_calories = breakfast_calories + lunch_calories + dinner_calories + snack_calories

print("\n\nTeor de calorias em " + today_date + ": " + str(content_calories) + " calorias.")
