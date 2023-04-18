import offer
from resources import resources
from prices import prices
from emoji import emoji_dict
from info import info
import datetime
import random
import os

line = "-" * 40
footer_line = "*" * 40

def main():
    header()
    basket = []

    while True:
        total = round(sum(basket), 2)
        # print("Current resources: ", resources)
        # print("Basket prices: ", basket)
        # print("In total: ", total)

        item = input("Item number --> ")

        if item == "q":
            print("I am processing the purchase..\n")
            print(line)
            break

        elif not item.isdigit():
            print("Invalid input. Please enter a valid\nitem number.")

        elif int(item) > 0 and int(item) < 20:
            if resources[int(item)] > 0:
                item_emoji = emoji_dict[int(item)]
                print(f"{item_emoji} added to basket 🛒")
                basket.append(prices[int(item)])
                resources[int(item)] -= 1
            elif resources[int(item)] == 0:
                print("❌ The selected product is no longer\nin stock ❌")

        else:
            print("Invalid input. Please enter a valid\nitem number.")

    os.system("cls")
    footer(basket, total)

def header():
    print(f"\n{offer.greet}\n{line}")
    print(f"{offer.offer}\n{line}")
    print("Choose an item according to the item\nnumber and press enter.")
    print("Press 'q' to end the purchase.")
    print(line)


def footer(basket, total):
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M:%S")
    rand_num = random.randint(1000119, 1299990)

    print(info)
    print(footer_line)
    print("Total items purchased: ", len(basket))
    print(f"Purchase price: {total} €")
    print(footer_line)
    print(f"Transaction number: {rand_num}")
    print(datetime.date.today(), current_time)
    print(line)
    print("Thanks for ordering.")
    print("Have a nice day.\n")
    print("🥩   🧀   🍎   🍌   🥕   🥐   🥦   🍭 ")
    print(line)


main()