############
##tuxtimer##
############

import time
import datetime
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify
import csv
import os

def countdown(t) :
    print("Der Timer " + name + " wurde um " + time.strftime("%H:%M") + " Uhr gestartet.")    
    while t > 0:
        print (t)
        t = t - 1
        time.sleep(60)
    if t ==0 :
        print(time.strftime("%H:%M") + " Ende!")


#########
##input##
#########
t = int(input("Dauer in Minuten: "))
name = str(input ("Name des Timers: "))

#############
##countdown##
#############
countdown(t)

##########
##notify##
##########
Notify.init("Timer-Ende")
TimerEnde = Notify.Notification.new("Der Timer " + name + " ist um " + time.strftime("%H:%M") + " Uhr abgelaufen.", "Es sind " + str(t) + " Minuten vergangen.", "dialog-information")
TimerEnde.set_timeout(120000)
TimerEnde.show()

print("\n" + "\n" + "bis: " + time.strftime("%H:%M") + " Timer: " + name + " Minuten: " + str(t))

#######
##log##
#######
with open (os.environ['HOME']+'/Documents/Studium/zeitlog', "a") as log:
    log.write("bis: " + time.strftime("%Y-%m-%d %H:%M") + " Timer: " + name + " Minuten: " + str(t) + "\n")

#############
##machs gut##
#############
