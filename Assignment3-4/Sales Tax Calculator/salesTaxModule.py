TAXRATE = 0.06

def salesTax(total):
    return round(total * TAXRATE, 2) #returns the value of the sales tax

def totalWithTax(total):
    return round(total + salesTax(total), 2) #returns the value of the tax plus total