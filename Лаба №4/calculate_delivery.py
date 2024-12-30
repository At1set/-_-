calculate_products_cost = lambda product_list: sum(map(lambda x: x.price, product_list))

def Calculate_regular_delivery(product_list : list):
  products_cost = calculate_products_cost(product_list)
  return products_cost if products_cost > 500 else products_cost + 100

def Calculate_express_delivery(product_list : list):
  if len(product_list) > 5: raise IndexError("Products count cant be more than 5")
  return calculate_products_cost(product_list) + 300

def Calculate_international_delivery(product_list : list):
  if any([product.name == "батарейки" for product in product_list]): raise TypeError("The product type cant be \"батарейки\"")
  products_cost = calculate_products_cost(product_list)
  return products_cost + 500