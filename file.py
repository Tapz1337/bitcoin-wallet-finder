
from colorama import Fore
import time
import secrets
from random import randint

continuing = True

btcval = 14404.41 # Update die Nummer wenn der Kurs hoch oder runter geht. 

while True:
  if continuing == True:
    time.sleep(.01)
    ranInt = randint(0, 2500)
    if ranInt <= 1:
      randomBTC = randint(1,100)/100
      print(Fore.WHITE + "> " + secrets.token_hex(64) + Fore.GREEN + " > " + str(randomBTC) + " BTC ($" + str("{:,}".format(round(btcval*randomBTC,2))) + ")")
      answer = input("> Would you like to continue? (Y/N) -> ")
      if answer.lower() == "y":
        continuing = True
      else:
       continuing = False
    else:
      print(Fore.WHITE + "> " + secrets.token_hex(20) + Fore.RED + " > 0.00 BTC ($0.00")
  else:
    break
      
  
      
