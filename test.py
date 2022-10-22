import danawa as dw

product = dw.get_product_codes("rtx 3060ti")[0]
product_code = product["code"]

variance = dw.get_price_variance(product_code, 3)
print(variance)