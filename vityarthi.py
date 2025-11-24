#gift shop
Inventory = {101:{"Name":"dresses", "price":2500,"stock":35},102:{"name":"toys","price":1500,"stock":40}, 103:{"name":"novels","price":1200,"stock":65}, 104:{"name":"drwaing sets","price":300,"stock":40}, 105:{"name":"mystery boxes","price":2000, "stock":75}}
#A loop to bring up the menu again after the operation is performed till the user decides to end the program.
end=False
while(end==False):
    #The choice to select the operation to be performed
    print("Press 1 to Add a new gift.")
    print("Press 2 to Check gift Availablity.")
    print("Press 3 to Retrieve a gift Price.")
    print("Press 4 to Update the stock of a gift.")
    print("Press 5 to Remove a gift.")
    print("Press 6 to List all gift with details")
    print("Press 7 to Clear the inventory.")
    print("Press 0 to Exit")
    choice=int(input("Select the operation to be performed:"))
    print("\n")
    if(choice==0):
        end=True
        print("The program will now terminate.")
    elif(choice==1):
        gift_id=int(input("Enter new gift ID:"))
        name=input("Enter gift_items:")
        price=float(input("Enter gift_items Price:"))
        stock = int(input("Enter stock quantity:"))
        Inventory[gift_id]={"name":name,"price":price,"stock":stock}
        print("\nUpdated Inventory:")
        print(Inventory)
        print("\n")
    elif(choice==2):
        gift_id=int(input("Enter gift ID to check:"))
        if gift_id in Inventory:
            print("gift_items:",Inventory[gift_id]["name"])
        else:
            print("gift_items not found.")
        print("\n")
    elif(choice==3):
        gift_id=int(input("Enter gift ID:"))
        if gift_id in Inventory:
            print("Price:",Inventory[gift_id]["price"])
        else:
            print("gift ID not found.")
        print("\n")
    elif(choice==4):
        gift_id=int(input("Enter gift ID:"))
        if gift_id in Inventory:
            print("1. Increase Stock.")
            print("2. Decrease Stock.")
            opt = int(input("Enter choice"))
            qty = int(input("Enter Quantity:"))
            if(opt==1):
                Inventory[gift_id]["stock"]+=qty
                print("Updated Stock:",Inventory[gift_id]["stock"])
            elif(opt==2):
                Inventory[gift_id]["stock"]-=qty
                print("Updated Stock:",Inventory[gift_id]["stock"])
        else:
            print("gift_item not found.")
        print("\n")
    elif(choice==5):
        gift_id=int(input("Enter gift ID to remove:"))
        if Inventory.pop(gift_id,None):
            print("gift_items removed successfully.")
        else:
            print("gift ID not found.")
        print("\nUpdated Inventory:")
        print(Inventory)
        print("\n")
    elif(choice==6):
        print("\nAll gift_items in inventory:")
        for g_id,details in Inventory.items():
            print(g_id,":",details)
        print("\n")
    elif(choice==7):
        Inventory.clear()
        print("Inventory Cleared.")
        print(Inventory)
        print("\n")