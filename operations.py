from write import write_file
from read import read_file # Importing function from read file
from datetime import datetime 
d= read_file() #Calling the function and stroing the returned dictionary
def display(show_selling_price=True):
    """
    Summary:
        Displays the current inventory of products with calculated selling prices.

    Parameters:
        None

    Returns:
        None

    Raises:
        None

    """
    print("ID \t Product \t Brand \t\t Stock \t Price\t Country")
    print("-" * 75)

    for key, value in d.items():
        product_name = value[0] #Getting product name
        brand_name=value[1] #Getting Brand name
        stock=value[2] #Getting stock value
        cost_price = int(value[3])  # Getting cost price of the product from file
        price = cost_price * 2 if show_selling_price else cost_price # Calculating markup i.e converting cost price to selling price
        country = value[4] #Getting country name
        print(key ,"\t", product_name,"\t", brand_name ,"\t", stock,"\t",price,"\t",country)
        print("-" * 75)

display()

def sell_products():
    """
    Summary:
        Handles the customer purchase process, applies promotions, calculates totals, 
        updates stock, and generates a bill.

    Parameters:
        None

    Returns:
        None

    Raises:
        ValueError: If the user inputs invalid (non-numeric or negative) values.
        KeyError: If a non-existent product ID is entered.

    """
    purchase_d=[] #List to hold items purchased by customer
    total=0 #Total bill without shipping
    grand_total=0 #Final total
    shipping_cost = 0 
    sell_loop=True
    tot=0
    total=0
    display()
    while sell_loop == True:
        #Taking valid productID from the customer
        while True:
            try:
                product_id = int(input("Enter the ID of the product you want to buy: "))
                    
                if product_id <= 0 or product_id > len(d):
                    print("\nPlease provide a valid product ID!")
                    continue  # takes us back to the top of the loop
                    
                print("\nTotal in stock:", d[product_id][2]) 
                break  # Exits the loop if everything is valid

            except ValueError:
                print("\nInvalid input. Please enter numeric values only.")

        while True:
            try:
                product_quantity = int(input("\nPlease provide the number of quantity of the product you want to buy: "))
                quantity_of_selected_products = int(d[product_id][2])  # Get available stock as integer

                free_items = product_quantity // 3
                total_for_stock = product_quantity + free_items

                if product_quantity <= 0 or total_for_stock > quantity_of_selected_products:
                    print("\nDear Admin, the quantity you are looking for is not available in our shop.")
                    print("Can you please look again in the table and enter a valid quantity.")
                    continue  # Ask for input again

                break  # Exit loop if input and stock are valid

            except ValueError:
                print("\nInvalid input. Please enter numeric values only.")


        product_name = d[product_id][0]
        brand_name = d[product_id][1]
        cost_price = int(d[product_id][3])
        price = cost_price * 2

            
        free_items = product_quantity //3
        total_for_stock = product_quantity + free_items

        if free_items>0:
            print( "\nwe are having buy 3 get one free offer, hence you have recieved",free_items,"free item")
        d[product_id][2] = str(int(d[product_id][2])-total_for_stock) #Updating the stock after the user buys items
        print("\nTotal in stock after buying:",d[product_id][2])
        tot = price*product_quantity
        print("\nFor this product and quantity is ",tot)

        #Adding the item and details to an empty list
        purchase_d.append([product_name, brand_name,price, product_quantity, free_items,tot])
        total = total + tot
        a=input("\n\nDo you want to by more items? (y/n)")
        if a.lower()=="y":
            continue
        elif a.lower()=="n":
            sell_loop=False
        else:
            print("NOT A VALID OPTION!")
            continue
                
            
            
        print("Total to be paid is ",total)
        #Writing the updated dictionary back to products.txt
        file = open("products.txt","w")
        for key in d.keys():
            line=d[key][0] +", " + d[key][1] + ", " + d[key][2] + ", " + d[key][3] + ", " + d[key][4] + "\n"
            file.write(line)
        file.close()
    print("\n")
    print("\n")
    print("For bill gneration you will have to enter the details first: ")
    print("\n")
    name = input("Enter your name")
    phone_number=input("Enter your phone number")
    print("\n")
    print("-" *75)
    print("\n")
    vat=(13/100)*total
    while True:
        ask = input("Do you want your order to be shipped? (y/n): ")
        
        if ask.lower() == 'n':
            totalaftervat = total + vat
            address = "Not Provided"
            break  # valid input, exit loop
        elif ask.lower() == 'y':
            address = input("Please enter your address: ")
            print("\nThe shipping cost is 130\n")
            totalaftervat = total + vat + 130
            break  # valid input, exit loop
        else:
            print("NOT A VALID OPTION! Please enter 'y' or 'n'.")
             
    

    write_file(name, phone_number, purchase_d, total,vat,totalaftervat,address)
    print("\n" + "-" * 113)
    print("Name: " + name + "\t\t\t\t\t\t\t\t\tDate: " + str(datetime.now().year) + "/" + str(datetime.now().month) + "/" + str(datetime.now().day))
    print("Contact: " + phone_number)
    print("\n" + "-" * 113)
    print("Product name\t\tBrand name\t\tPrice\tQuantity\tFree items\tTotal price")
    print("-" * 113)

    for item in purchase_d:
        line = item[0] + "\t\t" + item[1] + "\t\t" + str(item[2]) + "\t" + str(item[3]) + "\t\t" + str(item[4]) + "\t\t" + str(item[5])
        print(line)

    print("-" * 113)
    print(" Total\t\t\t\t\t\t\t\t\t\t\t  " + str(total))
    print(" Vat(13%)\t\t\t\t\t\t\t\t\t\t  " + str(vat))
    if address.lower() != "not provided":
        print(" Shipping cost\t\t\t\t\t\t\t\t\t\t  130")
    print(" Grand Total\t\t\t\t\t\t\t\t\t\t  " + str(totalaftervat))
    print("-" * 113)

def restock_products():
    """
    Summary:
        Allows admin to restock existing products and updates the inventory file.

    Parameters:
        None

    Returns:
        None

    Raises:
        ValueError: If the input is not numeric or a valid quantity.
        KeyError: If a non-existent product ID is entered.

    """
    restock_loop = True
    while restock_loop ==True:
        print("Here's the list of current products:\n")
        display(show_selling_price=False)

        restock_id = int(input("\nEnter the ID of the product to restock"))
        if restock_id in d:
            restock_quantity = int(input("\nEnter the quantity of the product that you want to restock"))
            if restock_quantity>0:
                d[restock_id][2] = str(int(d[restock_id][2])+restock_quantity) #Adding the quantity in the stock
                display(show_selling_price=False)
                print("\nStock updated successfully!")
                print("\nUpdated stock for", d[restock_id][0],":", d[restock_id][2])

                #Writing the updated dictionary back to products.txt
                file = open("products.txt","w")
                for key in d.keys():
                    line=d[key][0] +", " + d[key][1] + ", " + d[key][2] + ", " + d[key][3] + ", " + d[key][4] + "\n"
                    file.write(line)
                file.close()
        
                
            else:
                print("\nPlease enter a number greater than 0")
        else:
            print("\nInvalid product ID.")
            
        b=input("\n\nDo you want to restock more items? (y/n)")
        if b.lower()=="y":
            continue
        elif b.lower()=="n":
            restock_loop=False
        else:
            print("NOT A VALID OPTION!")
            continue

