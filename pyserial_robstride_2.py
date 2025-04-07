import serial
import time

# Adjust this to your COM port and baud rate
ser = serial.Serial(port='/dev/ttyUSB0', baudrate=9600, timeout=1)

def send_at_command(command):
    full_command = (command + '\r\n').encode()
    ser.write(full_command)
    time.sleep(0.1)
    response = ser.read_all().decode(errors='ignore')
    print(f"> {command}\n< {response}")
    return response

# Example AT command sequence
if ser.is_open:
    send_at_command("AT")            # Test communication
    send_at_command("AT+INFO")       # Device information
    send_at_command("AT+CANOPEN")    # Initialize CAN
    send_at_command("AT+CANSEND=0300FD01#0000000000000000")  # Send standard CAN frame
    send_at_command("AT+CANCLOSE")   # Close CAN communication

    ser.close()
else:
    print("Failed to open serial port.")
