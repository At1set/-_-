from Delivery import Delivery

class Regular_delivery(Delivery):
  def __init__(self):
    super().__init__()

  def deliver(self):
    products_cost = super().deliver()
    return products_cost if products_cost > 500 else products_cost + 100