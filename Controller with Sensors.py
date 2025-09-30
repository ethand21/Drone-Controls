# Import the necessary module from CoDrone EDU
from codrone_edu.drone import *

# Initialize and create a Drone instance
drone = Drone()

# Establish a connection to the drone and the controller
drone.pair()
from codrone_edu.drone import *
from codrone_edu.enums import DataType
import time

# Initialize and pair with the drone and controller
drone = Drone()
drone.pair()

# Welcome tones and LED
drone.set_drone_LED(255, 255, 255, 255)
drone.drone_buzzer(Note.C4, 1000)
drone.drone_buzzer(Note.D4, 1000)
drone.drone_buzzer(Note.E4, 1000)

# Sensor check
print("Pressure is: ", drone.get_pressure())
print("Battery is: ", drone.get_battery())
print("Angle is: ", drone.get_angle_x(), drone.get_angle_y(), drone.get_angle_z())

# Temperature conversion function
def to_fahrenheit(degrees_c):
    return degrees_c * 1.8 + 32

temperature = drone.get_drone_temperature()
print("Celsius: ", temperature)
print("Fahrenheit: ", to_fahrenheit(temperature))

# Prepare for manual control
drone.setEventHandler()
print("Controller ready. Use joysticks to fly the drone.")
print("Press TAKE OFF to lift off, LAND to land, SPACEBAR for emergency stop.")

pressures = []

# Function to collect pressure data for a given duration (non-blocking)
def collect_pressures(duration):
    for i in range(duration):
        pressure = drone.get_pressure()
        pressures.append(pressure)
        print(f"Pressure at t={i}s: {pressure} Pa")
        time.sleep(1)

# Flight loop
is_flying = False

try:
    while True:
        # Emergency Stop (spacebar)
        if keyboard.is_pressed("space"):
            print("⚠️ EMERGENCY STOP TRIGGERED!")
            drone.emergency_stop()
            break

        # Update controller info
        drone.controller.get_info()

        # Check TAKEOFF
        if drone.controller.TAKEOFF:
            if not is_flying:
                drone.take_off()
                print("Taking off...")
                is_flying = True
                collect_pressures(5)  # Start collecting pressure right after takeoff

        # Check LAND
        if drone.controller.LAND:
            if is_flying:
                drone.land()
                print("Landing...")
                is_flying = False
                break

        # If flying, read joystick inputs
        if is_flying:
            pitch = drone.controller.left_y()
            roll = drone.controller.left_x()
            yaw = drone.controller.right_x()
            throttle = drone.controller.right_y()

            drone.set_pitch(pitch)
            drone.set_roll(roll)
            drone.set_yaw(yaw)
            drone.set_throttle(throttle)

        time.sleep(0.05)

except KeyboardInterrupt:
    print("Interrupted. Landing drone.")
    drone.land()

finally:
    print("Final pressures collected:")
    for i, p in enumerate(pressures):
        print(f"t={i}s: {p} Pa")

    drone.close()



drone.close()