from random import randint
from random import choice
from time import sleep
intros = ["Simon says... ", ""]
simon_says = ["Hands on head", "Hands on ears",
              "Right hand up", "Left hand up",
              "Hands on shoulders"]
counter = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for counter in range(10):
  intro = choice(intros)
  index = randint(0,4)
  instruction = simon_says[index]
  print(f"{intro}{instruction}")
  sleep(2)