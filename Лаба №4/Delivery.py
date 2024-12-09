from Product import Product

class Delivery():
  def __init__(self):
    self._productList = []

  def deliver(self):
    """
    Получение суммы доставки
    """
    return sum(map(lambda x: x.price, self._productList))

  def addProduct(self, product : Product):
    """
    Добавление продукта в доставку
    """
    if not isinstance(product, Product): raise TypeError("product argument must be instance of Product class")
    return self._productList.append(product)
  
  def removeProduct(self, product : Product):
    """
    Удаление продукта из доставки
    """
    if not isinstance(product, Product): raise TypeError("product argument must be instance of Product class")
    if (self._productList.count(product) == 0): return False
    self._productList.remove(product)
    return True
  
  def clearProductList(self):
    """
    Очистка списка продуктов доставки
    """
    self._productList = []