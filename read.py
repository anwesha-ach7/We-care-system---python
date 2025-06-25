def read_file():
    """
    Summary:
        Reads product data from a text file and stores it in a dictionary.

    Parameters:
        None

    Returns:
         A dictionary with product IDs as keys and product details as values.

    Raises:
        No error

    """
    d={}
    file = open("products.txt", "r")
    data = file.readlines() #Reading all lines from the text file and storing it in data
    id1 = 1#uniquely identifying each product
    for line in data:  
        line = line.replace("\n", "").split(", ")
        """Removing the newline character at the end
        of the line and spliting the line by commas"""
        d[id1] = line #Adding product to the dictionary
        id1 = id1 + 1


    file.close()
    return d
    print()
