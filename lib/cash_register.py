#!/usr/bin/env python3

class CashRegister: 
  def __init__(self, discount=0):
    self.discount=discount
    self.total=0
    self.items=[]
    self.last_transaction=0
  
  def add_item(self, title, price, quantity=1):
    self.last_transaction=price*quantity
    self.total+=self.last_transaction
    self.items.extend(title for _ in range(quantity))


  def apply_discount(self):
    if self.discount>0:
      self.total-=((self.discount/100)*self.total)
      print(f"After the discount, the total comes to ${self.total:.0f}.")
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    self.total-=self.last_transaction

