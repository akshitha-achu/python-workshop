storage=[]
num=int(input("enter the number of items:"))
for i in range(num):
    item=input("Enter the items:")
    storage.append(item)
print (storage)
item_buy=input("enter the item u want to buy:")
for i in range(len(storage)):
    if item_buy in storage:
        print("the item is delivered")
        storage.remove(item_buy)
print(storage)
