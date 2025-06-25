from datetime import datetime
from read import read_file



def write_file(name, phone_number, purchase_d, total,vat,totalaftervat,ask):
    """
    Summary:
        Writes billing details to a uniquely named text file using date and time.

    Parameters:
        name (str): Customer's name.
        phone_number (str): Customer's phone number.
        purchase_d (list): List of purchased products and their details.
        total (float): Total price before VAT and shipping.
        vat (float): VAT amount (13% of total).
        totalaftervat (float): Final total after VAT and shipping.
        ask (str): 'y' or 'n' indicating if shipping was chosen.

    Returns:
        None

    Raises:
        No error
    """
    #CREATING UNIQUE FILE USING DATE AND TIME
    
    unique_num = str(datetime.now().year)+str(datetime.now().month)+str(datetime.now().day)+str(datetime.now().hour)+str(datetime.now().minute)+str(datetime.now().second)
    file_name=unique_num + ".txt"
    file = open(file_name,"w")
    dash = "-" * 113
    file.write("Name: "+name)
    file.write("\t\t\t\t\t\t\t\t\t Date:"+str(datetime.now().year)+"/"+str(datetime.now().month)+"/"+str(datetime.now().day)+"\n") 
    file.write("Contact: "+phone_number+"\n\n")
    file.write(dash+"\n")
    file.write("Product name\t\tBrand name\t\tPrice\tQuantity\tFree items\tTotal price\n")
    file.write(dash+"\n")
    for item in purchase_d:
        line = str(item[0]) + "\t\t" + str(item[1]) + "\t\t" + str(item[2]) + "\t   " + str(item[3]) + "\t\t   " + str(item[4]) + "\t\t   " + str(item[5])
        file.write(line + "\n")
    file.write(dash+"\n")
    file.write(" Total \t\t\t\t\t\t\t\t\t\t\t  "+str(total)+"\n")
    file.write(" Vat(13%)\t\t\t\t\t\t\t\t\t\t  " +str(vat)+"\n")
    if ask.lower()=='y':
        file.write(" Shipping cost\t\t\t\t\t\t\t\t\t\t " +str(130)+"\n")
    file.write(" Grand Total \t\t\t\t\t\t\t\t\t\t  "+str(totalaftervat)+"\n")
    file.close()
    
