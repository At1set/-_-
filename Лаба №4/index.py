from Product import Product
from Delivery import Delivery
from Regular_delivery import Regular_delivery
from Express_delivery import Express_delivery
from International_delivery import International_delivery


def main():
  product_list1 = [
    Product(1, "Игрушка", 130),
    Product(2, "Карандаши", 120),
    Product(3, "Рюкзак", 100),
    Product(4, "Кубик рубика", 50),
    Product(5, "Бумага А4", 100),
  ]

  product_list2 = [
    Product(7, "Arduino Nano", 380),
    Product(7, "Динамик 40мм, 3W, 4Ом.", 240),
    Product(8, "Провода соединительные \"папа-папа\"", 210),
    Product(9, "Комплект светодиодов 5 мм", 50),
    Product(10, "SG90 Сервопривод x2", 350),
    Product(11, "Тактовая кнопка 4 контакта x3", 120),
  ]

  product_list3 = [
    Product(12, "Игрушка-антистресс", 200),
    Product(13, "Печеньки", 150),
    Product(14, "Ананас", 500),
    Product(15, "Игровая приставка", 4500),
    Product(16, "батарейки", 200),
  ]

  def test_delivery(delivery : Delivery, product_list):
    try:
      products_cost = 0
      for product in product_list:
        delivery.addProduct(product)
        products_cost += product.price
      print(f"Товаров на сумму: {products_cost}, стоимость с доставкой: {delivery.deliver()}")
    except Exception as error:
      product_list_type = None
      if product_list == product_list1: product_list_type = "product_list1" 
      if product_list == product_list2: product_list_type = "product_list2" 
      if product_list == product_list3: product_list_type = "product_list3" 
      print(f"Ошибка при попытке добавить товар из списка {product_list_type} в корзину: {error}")
    finally:
      delivery.clearProductList()

  print("====== Обычная доставка ======")
  regular_delivery = Regular_delivery()
  test_delivery(regular_delivery, product_list1)
  test_delivery(regular_delivery, product_list2)

  print("\n====== Экспресс доставка ======")
  express_delivery = Express_delivery()
  test_delivery(express_delivery, product_list1)
  test_delivery(express_delivery, product_list2)

  print("\n====== Международная доставка ======")
  international_delivery = International_delivery()
  test_delivery(international_delivery, product_list1)
  test_delivery(international_delivery, product_list3)


if __name__ == "__main__":
  main()