from Delivery import Delivery

class Express_delivery(Delivery):
  def __init__(self):
    super().__init__()

  def deliver(self):
    return super().deliver() + 300
  
  def addProduct(self, product):
    if len(self._productList) + 1 > 5: raise IndexError("Products count cant be more than 5")
    return super().addProduct(product)