import time

class TemperatureSensor:
    def __init__(self, threshold):
        self.threshold = threshold
        self.current_temperature = 0.0

    def read_temperature(self):
        # Simulate reading temperature from a sensor
        return self.current_temperature

    def set_temperature(self, temperature):
        self.current_temperature = temperature

    def control_temperature(self):
        while True:
            temperature = self.read_temperature()
            print(f"Current Temperature: {temperature}°C")
            if temperature > self.threshold:
                print("Temperature exceeds threshold! Activating cooling system...")
                self.activate_cooling_system()
            time.sleep(1)

    def activate_cooling_system(self):
        print("Cooling system activated!")

# Main function to run the temperature control loop
if __name__ == "__main__":
    # Set the temperature threshold to 25 degrees Celsius
    sensor = TemperatureSensor(threshold=25)

    # Simulate temperature changes
    for temp in [22, 26, 24, 27, 23]:
        sensor.set_temperature(temp)
        sensor.control_temperature()
