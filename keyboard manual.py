# Import the necessary module from CoDrone EDU
from codrone_edu.drone import *

# Initialize and create a Drone instance
drone = Drone()

# Establish a connection to the drone and the controller
drone.pair()
from codrone_edu.drone import *

import time

drone = Drone()
drone.pair()



print("Command Options: ")

print("w: throttle up")
print("s: throttle down")
print("a: yaw left")
print( "d: yaw right")
print( "i: pitch forward")
print( "k: pitch backward")
print( "j: roll left")
print( "l: roll right" )
print( "q: quit")

# Welcome to Python for Robolink! Write your Python code below.
drone.takeoff()

drone.set_trim(0,0) # Adjust for your drone

power = 40

while True:

    drone.set_throttle(0)

    drone.set_roll(0)

    drone.set_yaw(0)

    drone.set_pitch(0)


    direction = input("Input a command: ")

    if direction == "w":
        time.sleep(0.05)
        drone.set_throttle(power)
        drone.move(1)
        drone.set_throttle(0)

    elif direction == "s":
        time.sleep(0.05)
        drone.set_throttle(-power)
        drone.move(1)
        drone.set_throttle(0)
      
    elif direction == "a":
        time.sleep(0.05)
        drone.set_yaw(-power)
        drone.move(1)
        drone.set_yaw(0)

    elif direction == "d":
        time.sleep(0.05)
        drone.set_yaw(power)
        drone.move(1)
        drone.set_yaw(0)

    elif direction == "i":
        time.sleep(0.05)
        drone.set_pitch(power)
        drone.move(1)
        drone.set_pitch(0)

    elif direction == "k":
        time.sleep(0.05)
        drone.set_pitch(-power)
        drone.move(1)
        drone.set_pitch(0)

    elif direction == "j":
        time.sleep(0.05)
        drone.set_roll(-power)
        drone.move(1)
        drone.set_roll(0)

    elif direction == "l":
        time.sleep(0.05)
        drone.set_roll(power)
        drone.move(1)
        drone.set_roll(0)

    elif direction == "q":

        time.sleep(0.05)
        drone.land()
        break

    else:

        print("Not a command")
        time.sleep(0.05)



drone.close()
drone.close()