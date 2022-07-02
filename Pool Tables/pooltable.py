from datetime import datetime
import json
from tracemalloc import start
from poolclasses import PoolTables


tables = []
player_stats = []


def view_tables():
    for table in tables:
        if table.is_occupied == False:
            print(f"{table.table_number}: UNOCCUPIED")

        if table.is_occupied == True:
            print(f"{table.table_number}: OCCUPIED")


for item in range(1, 13):
    pool_table = PoolTables(item)
    tables.append(pool_table)


def table_selected():
    for table in tables:
        if table.is_occupied == False:
            print(f"{table.table_number}: UNOCCUPIED")

        if table.is_occupied == True:
            print(f"{table.table_number}: OCCUPIED")

    selected_table = tables[table_choice]
    if selected_table.is_occupied == True:
        print("Game is in session, please select a different table!")
    else:
        selected_table.check_out()
        print("\n")
        print(
            f"Your game has started at: {selected_table.converted_start_time}")


def table_cashed_in():
    selected_table = tables[table_choice]
    selected_table.cash_in()

    print("\n")
    print(
        f"Thanks for checking out Pool Table Arcade. Your check out time was {selected_table.converted_end_time}")
    print("\n")


while True:

    main_menu = print("""Welcome to Pool Tables Arcade
Please choose an option from the list below:

Press 1 to view tables
Press 2 to reserve your table
Press 3 to cash out
Press q to quit""")

    try:
        choice = input("Enter option now: ")
    except:
        print("Valid inputs only, try again.")

    if choice == "1":
        view_tables()

    elif choice == "2":
        view_tables()

        table_choice = int(
            input("Enter unoccupied table number to start your game: ")) - 1

        table_selected()

    elif choice == "3":

        table_choice = int(
            input("Which table number are you checking out of? ")) - 1
        table_cashed_in()

    if choice == "q":
        break

for table in tables:
    start_time = table.start_time
    end_time = table.end_time
    if start_time != None and end_time != None:
        total_time = end_time - start_time
    # print(total_time)

        player = {"Pool Table": table.table_number,
                  "Check out": start_time,
                  "Check In": end_time,
                  "Time Played": total_time}

        print(player)

        player_stats.append(player)


with open("table_times.json", "w") as file:

    json.dump(player_stats, file, default=str)
