print("\n\n")
print("-" * 75)
print("\t\t\t    WELCOME TO WECARE!!")
print("-" * 75)
print("\n\n")



from read import read_file
from write import write_file
from operations import display, sell_products, restock_products

make_sale=True
while make_sale==True:
    try:
        print("Press 1 to sell to customer")
        print("Press 2 to purchase from manufacturer")
        print("Press 3 to exit from the system")

        options=int(input("\nEnter your choice"))
        if options<=0 or options >3:
            print("\nPlease enter a valid option!!")
        if options ==1:
           sell_products()
            
        elif options ==2:
            restock_products()

        elif options ==3:
                print("\nExiting the system. Thank you!!")
                make_sale= False
    except ValueError:
        print("\nInvalid input. Please enter numeric values only.")








