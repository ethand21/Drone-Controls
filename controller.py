# Import the necessary module from CoDrone EDU
from codrone_edu.drone import *

# Initialize and create a Drone instance
drone = Drone()

# Establish a connection to the drone and the controller
drone.pair()
from codrone_edu.drone import *

print("Command Options: ")

print("left joystick: pitch, roll")
print("right joystick: yaw, altitude")
print("l1: takeoff")
print("l2: land")
print("r1: flip")
print("r1: readings")

def check_buttons():

    if drone.l1_pressed():
        drone.takeoff()
        print("takeoff")
    elif drone.l2_pressed():
        drone.land()
        print("land")
    elif drone.r1_pressed():
        drone.flip()
        print("flip")
    elif drone.r2_pressed():
        print("Temperature is: ", drone.get_temperature())
        print("Battery is: ", drone.get_battery())
        print("Pressure is: ", drone.get_pressure())
        print("Angle is: ", drone.get_angle_x(), drone.get_angle_y(), drone.get_angle_z())
        drone.drone_buzzer(Note.A4, 500)
        drone.drone_buzzer(Note.D4, 500)
        drone.drone_buzzer(Note.A4, 500)
        drone.drone_buzzer(Note.D4, 500)
        drone.set_drone_LED(255, 0, 0, 255)
        time.sleep(0.5)
        drone.set_drone_LED(0, 0, 255, 255)
        time.sleep(0.5)
        drone.set_drone_LED(255, 0, 0, 255)
        time.sleep(0.5)
        drone.set_drone_LED(0, 0, 255, 255)
        drone.drone_buzzer(Note.A4, 500)
        drone.drone_buzzer(Note.E4, 500)
        drone.drone_buzzer(Note.A4, 500)
        drone.drone_buzzer(Note.E4, 500)

drone = Drone()
drone.pair()

while True:
    check_buttons()
    pitch = drone.get_left_joystick_y()
    roll = drone.get_left_joystick_x()
    throttle = drone.get_right_joystick_y()
    yaw = drone.get_right_joystick_x()

    if pitch > 60:
        pitch = 60
    if pitch < -60:
        pitch = -60
    if roll > 60:
        roll = 60
    if roll < -60:
        roll = -60
    if throttle > 60:
        throttle = 60
    if throttle < -60:
        throttle = -60
    if yaw > 60:
        yaw = 60
    if yaw < -60:
        yaw = -60

    drone.set_pitch(pitch)
    drone.set_roll(roll)
    drone.set_throttle(throttle)
    drone.set_yaw(yaw)
    drone.move()

drone.close()
drone.close()