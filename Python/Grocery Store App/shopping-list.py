from class_file import ShoppingList, StoreInfo

grocery_lists = []


def view_grocery_lists():
    for index in range(0, len(grocery_lists)):
        print(f"{index + 1} - {grocery_lists[index].location}")


def view_shopping_list():
    for index in range(0, len(grocery_lists)):
        print(grocery_lists[index].location)
        print(grocery_lists[index].address)
        for item in grocery_lists[index].items:
            print(item.name)


while True:

    main_menu = print("""Enter one of the following options
  
  Press option 1 to add new store
  Press option 2 to add new shopping list
  Press option 3 to view your shopping list
  Press option 4 to delete a store
  Press option 5 to delete a shopping list
  Press q to quit
  """)
    try:

        choice = input("Enter your option: ")

    except:
        print("Incorrect input")

    if choice == "1":
        location = input("Enter store: ")
        address = input("Enter address of store: ")

        grocery_list = StoreInfo(location, address)
        grocery_lists.append(grocery_list)

    elif choice == "2":
        view_grocery_lists()
        try:
            user_choice = int(
                input("Which shopping list do you want to add items to? ")) - 1

            grocery_list = grocery_lists[user_choice]
            item_name = input("Enter grocery item: ")
            price = int(input("How much does that item cost? $ "))
            quantity = int(input("Enter quantity needed: "))

            item = ShoppingList(item_name, price, quantity)
            grocery_list.items.append(item)
        except ValueError:
            print("Please enter a valid input")
        except:
            print("Something went wrong")
    elif choice == "3":
        view_shopping_list()

    elif choice == "4":
        view_grocery_lists()

        try:

            user_choice = int(
                input("Which store number do you want to delete? "))

            del grocery_lists[user_choice - 1]

            view_grocery_lists()

            print("Store has been deleted")

        except ValueError:
            print("Please enter a valid input")
        except:
            print("Something went wrong")

    elif choice == "5":
        view_grocery_lists()

        try:

            user_choice = int(
                input("Which store has the item you want to delete? ")) - 1
            grocery_list = grocery_lists[user_choice]
            print(f"{grocery_list.location} has the following items")

            for index in range(len(grocery_list.items)):
                print(f"{index + 1} - {grocery_list.items[index].name}")

            remove_item = int(
                input("Enter item number you wish to remove: ")) - 1
            del grocery_list.items[remove_item]

            view_grocery_lists()
        except ValueError:
            print("You must enter a valid input")
        except:
            print("Something went wrong")
    elif choice == "q":
        break

    else:
        print("Please enter a valid menu option")
