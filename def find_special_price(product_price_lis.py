def find_special_price(product_price_list):
   if len(product_price_list)==2:
        return product_price_list[1]
    else:
        price =find_special_price(product_price_list[1:])
        if price//2 > product_price_list[0] :
            return price
        else:
            return product_price_list[0]