import tkinter, random

names=list()
colors=list()

names=['Бэмби',"Пэнни","Алекс","Бил"]
colors=['Black','Blue','Orange','Red']




class animal():
   def __init__(self):
      self.age=random.randint(1,10)
      self.mass=random.randint(10,100)
      self.name=random.choice(names)

 
   def info(self):
      return(f"Имя:{self.name}\nМасса: {self.mass}\nВозраст: {self.age}")   


class bird(animal):
   
   skill='Fly'
   colors=random.choice(colors)
   
   def info(self):
      return(f"Имя:{self.name}\nМасса: {self.mass}\nВозраст: {self.age}\nНавыки: {self.skill}\nЦвет: {self.colors}")



skill='Nothing'

OBJ=animal()
BadD=bird(skill)

print(f"{BadD.info()}")
print(f"{OBJ.info()}")