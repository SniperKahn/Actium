import serial
import time

# High-level planning

class AdeeptController:
    def __init__(self, port, baud=115200):
        self.conn = serial.Serial(port, baud, timeout=2)
        time.sleep(2) # Wait for Arduino reboot

    def move_to_angles(self, angles):
        """
        angles: list of 5 floats (degrees)
        """
        # 1. Safety Check: Clip to 0-180
        clipped = [max(0, min(180, int(a))) for a in angles]
        
        # 2. Format and Send
        cmd = f"{clipped[0]},{clipped[1]},{clipped[2]},{clipped[3]},{clipped[4]}\n"
        self.conn.write(cmd.encode())
        
        # 3. Wait for Hardware Acknowledgment
        response = self.conn.readline().decode().strip()
        return response == "ACK"

# Usage in the exercise:
arm = AdeeptController('/dev/cu.usbserial-11320')
arm.move_to_angles([90, 90, 90, 90, 180])
