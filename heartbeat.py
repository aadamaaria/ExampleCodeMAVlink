from pymavlink import mavutil
import time

# Configuration variables
# Serial port for Pixhawk (GPIO UART on Pi)
SERIAL_PORT = '/dev/ttyAMA0'
# Communication speed (57600 is standard for Pixhawk)
BAUD_RATE = 57600

# Establish MAVLink connection to the flight controller
vehicle = mavutil.mavlink_connection(SERIAL_PORT, baud=BAUD_RATE)

# Wait for heartbeat – confirms Pixhawk is responding
print("Waiting for heartbeat...")
vehicle.wait_heartbeat()

# If we reach here, connection successful
print("Heartbeat received")
