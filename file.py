from colorama import Fore
import time
import secrets
from random import randint

continuing = True

btcval = 82.393 # Update die Nummer wenn der Kurs hoch oder runter geht. 

while True:
  if continuing == True:
    time.sleep(.01)
    ranInt = randint(0, 2500)
    if ranInt <= 1:
      randomBTC = randint(1,100)/100
      print(Fore.GREEN + "> 0x" + secrets.token_hex(20) + Fore.GREEN + " > " + str(randomBTC) + " BTC ($" + str("{:,}".format(round(btcval*randomBTC,2))) + ")")
      print(Fore.GREEN + "> SUCCESS! " + str(randomBTC) + " BTC has been imported to your crypto account!")
      answer = input("> Would you like to continue? (Y/N) -> ")
      if answer.lower() == "y":
        continuing = True
      else:
        continuing = False
    else:
      print(Fore.LIGHTMAGENTA_EX + "> 0x" + secrets.token_hex(20) + Fore.RED + " > 0.00 BTC ($0.00)")
  else:
    break
