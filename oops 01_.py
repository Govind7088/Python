# Create a class programmer for storing information.

class Programmer:
  company="Microsoft"
  
  def __init__(self, name, product):
    self.name=name
    self.product=product
  
  def getInfo(self):
    print(f"The name of the {self.company} programmer is {self.name} and the product is {self.product}.")
Harry=Programmer("Govind", "Skype")
Vivek=Programmer("Vivek","Github")
Ankit=Programmer("Govind", "Skype")
Pradeep=Programmer("Govind", "Skype")
Harry.getInfo()
Vivek.getInfo()
Ankit.getInfo()
Pradeep.getInfo()
