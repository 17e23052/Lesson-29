counter = [1, 2, 3, 4, 5, 6, 7, 8, 9]
from random import randint
from time import sleep
simon_says = ["Hands on head", "Hands on ears",
              "Right hand up", "Left hand up",
              "Hands on shoulders"]

for counter in range(10):
  index = randint(0,4)
  instruction = simon_says[index]
  print(f"Simon says... {instruction}")
  sleep(2)