# **IoT Smart Fan 🌀**

A simulation project for a Smart Fan system using Python2 and Tkinter.  
The fan speed is automatically controlled based on temperature sensor readings.

---

## **🚀 Setup Steps**
1. Clone the repository:
   `
   git clone https://github.com/YOUR-USERNAME/IoT-Smart-Fan.git
   cd IoT-Smart-Fan
   
Install Python2 and Tkinter:
sudo apt install python2 python-tk

Run the simulation:
python2 iotSmartFanTk.py

## **⚡ Challenges Faced**
Original code depended on Onion Omega libraries (OmegaExpansion) that don’t work on normal Ubuntu PCs.

Needed to rewrite some files for Python2 compatibility.

Fixed issues with f-strings and non-ASCII characters.

Added simulation logic for temperature sensors and PWM fan duty cycle.

##*🔧 **How the Simulation Works**
A fake temperature sensor generates random values between 20C and 45C.

A control function maps the temperature to a fan duty cycle (20–100%).

A Tkinter GUI displays real-time updates of temperature and fan duty.

##🛠️ **Emulated Sensors & Devices**
Temperature Sensor → Simulated with random values.

PWM Fan Motor → Represented by duty cycle calculations.

Tkinter GUI → Acts as the fan controller interface.

##🌱 **Future Improvements**
Add graphs (temperature vs. duty cycle) using matplotlib.

Add manual control buttons in Tkinter (e.g., turn fan ON/OFF).

Expand to use real hardware sensors (DS18B20, DHT22).

Deploy on an actual Onion Omega / Raspberry Pi.


<img width="1266" height="731" alt="Screenshot from 2025-09-08 10-50-56" src="https://github.com/user-attachments/assets/eedb582b-d72c-45d4-8109-e98cf84d85e6" />
