food_items = []

choice = 0
while True:
    print("\n==============================")
    print("Community Food Sharing System")
    print("==============================")
    print("1. Donate Food")
    print("2. View Food")
    print("3. Search Food")
    print("4. Exit")

    choice = int(input('Please enter your choice: '))

    if choice == 1:
        print("Donate Food selected")
        food_name = input("Enter your food_name: ")
        quantity = input("Enter your Quantity: ")
        category = input("Enter your Category: ")
        location = input("Enter your location: ")
        food_items.append({'food_name': food_name, 'quantity': quantity, 'category': category, 'location': location})
        print(food_items)
    elif choice == 2:
        if not food_items:
            print('There is no any item is added')
        else:
            print(f'\n\nHere is all donated food items.')
            for index, food_item in enumerate(food_items):
                print(f'\n{index+1}: \nName: {food_item['food_name']}\nQuantity: {food_item['quantity']}\nCategory: {food_item['category']}\nLocation: {food_item['location']}')
    elif choice == 3:
        found = False
        category_search = input('Please enter category: \n')
        for index, food_item in enumerate(food_items):
            if food_item['category'].lower() == category_search.lower():
                found = True
                print(f'\n{index+1}: \nName: {food_item['food_name']}\nQuantity: {food_item['quantity']}\nCategory: {food_item['category']}\nLocation: {food_item['location']}')
        
        if not found:
            print("No food items found in this category.")

    elif choice == 4:
        print("Thank you for using the Community Food Sharing System!")
    else:
        print('Sorry wrong menu')