from random import randint
from time import sleep
simon_says = ["Hands on head", "Hands on ears",
              "Right hand up", "Left hand up",
              "Hands on shoulders"]
count = 0
while count < 10:
  index = randint(0,4)
  instruction = simon_says[index]

  print(f"Simon says...{instruction}")
  count = count + 1
  sleep(2)