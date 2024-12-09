from Delivery import Delivery

class International_delivery(Delivery):
  def __init__(self):
    super().__init__()

  def deliver(self):
    return super().deliver() + 500
  
  def addProduct(self, product):
    if product.name == "батарейки": raise TypeError("The product type cant be \"батарейки\"")
    return super().addProduct(product)