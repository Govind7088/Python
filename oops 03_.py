# Ticket book of train and find the Seats and train Name.

class Train:
  def __init__(self, name, fare, seats):
    self.name=name
    self.fare=fare
    self.seats=seats

  def getStatus(self):
    print("**************************************")
    print(f"The name of the Train is {self.name}")
    print(f"The seats available in the Train is {self.seats}")
    print("**************************************")

  def fareInfo(self):
    print(f"The price of tickets is {self.fare}")

  def bookTicket(self):
    if (self.seats>0):
      print(f"Your ticket has been booked! Your seat number is {self.seats}")
      self.seats=self.seats-1  
    else:
      print("Sorry! This train has been fulled.")

intercity=Train("Intercity Express: 14509",90,300)
intercity.getStatus()
intercity.fareInfo()
intercity.bookTicket()
intercity.getStatus()