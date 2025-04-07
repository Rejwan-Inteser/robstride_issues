import serial
import time

# Replace 'COMx' with the correct port where your device is connected.
# For example, on Windows it might be 'COM3' or on Linux/macOS it could be '/dev/ttyUSB0'.
port = '/dev/ttyUSB0'  # Change this to your COM port (e.g., 'COM3' for Windows, '/dev/ttyUSB0' for Linux)
baud_rate = 9600  # Typically, 115200 is the default baud rate for serial communication

# AT command to send (your AT command in hexadecimal format)
at_command = b'41549007e80c0805700000050000000d0a'  # Example of AT command

# Set up serial connection
ser = serial.Serial(port, baudrate=baud_rate, timeout=1)

def send_at_command(command):
    try:
        # Send the AT command to the motor
        print(f"Sending command: {command}")
        ser.write(command)  # Send the command as bytes
        time.sleep(1)  # Wait for the response

        # Read the response from the serial port
        response = ser.read(ser.in_waiting)  # Read available bytes in the buffer

        # Decode the response (assuming it's a UTF-8 response, adjust if necessary)
        if response:
            print(f"Raw response: {response}")
            decoded_response = response.decode('utf-8', errors='ignore')  # Decode the response
            print(f"Decoded response: {decoded_response}")
        else:
            print("No response received.")
        
    except Exception as e:
        print(f"Error: {e}")

# Main function to communicate
if __name__ == "__main__":
    # Open the serial port
    if ser.is_open:
        print(f"Connected to {port} at {baud_rate} baud.")
        send_at_command(at_command)
    else:
        print(f"Failed to open serial port {port}.")

    # Close the serial port after communication
    ser.close()
    print("Serial connection closed.")
