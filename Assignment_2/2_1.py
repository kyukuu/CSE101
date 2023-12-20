menu = {"Samosa   ": 15,
        "Idli     ": 30,
        "Maggie   ": 50,
        "Dosa     ": 70,
        "Tea      ": 10,
        "Coffee   ": 20,
        "Sandwich ": 35,
        "ColdDrink": 25
        }

print("The Menu for the day is:")
print("------------------------")
count = 1
space = '\t'
for i in menu:
    print(f'{count}.{i} {space} {menu[i]}')
    count += 1

price = list(menu.values())
items = list(menu.keys())


item = 100
item_list = []
item_quantity = []
while True:
    order = input().split()

    if order == []:
        break

    order = [int(i) for i in order]
    if order[0] < 0 or order[0] > len(items):
        print(f'Item not in menu for {order[0]}')
        order.clear()

    else:
        item_list.append(order[0])
        item_quantity.append(order[-1])

ans = []
for i in range(len(item_list)):
    ans.append(price[item_list[i]-1]*item_quantity[i])

print("----------------------")
print("\tBill")
for i in range(len(item_list)):
    print(
        f'{item_quantity[i]} {items[item_list[i]-1]} is {ans[i]}')
print()
print("Total Amount:", sum(item_quantity), "items", "Rupees", sum(ans))

print("----------------------")

# for items greater than the length of menu
# negative indices
