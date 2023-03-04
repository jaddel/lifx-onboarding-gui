# LIFX Bulb Onboarder GUI

This is a Python script `OnboardGUI.py` that provides a GUI for onboarding LIFX smart bulbs. The GUI allows users to enter their home Wi-Fi network name and password, and then sends the necessary packets to the LIFX bulb to onboard it to the network. 

## Instructions
1. Bring the LIFX bulb into pairing mode by following the instructions provided by LIFX. This usually involves turning the bulb on and off a certain number of times until it starts flashing rapidly.
2. Connect your computer or mobile device to the Wi-Fi network created by the bulb. This network name should start with "LIFX".
    * Note: If the bulb has not yet created a Wi-Fi network, you may need to wait up to 15 minutes for it to do so. After this time, the bulb will be creating its own Wi-Fi network that you can connect to.
3. Launch the `OnboardGUI.py` script and enter the Wi-Fi network name and password for your home Wi-Fi network into the "SSID" and "Password" fields in the GUI, respectively.
4. Click the "Onboard Bulb" button to start the onboarding process.
5. Wait until the onboarding process is complete, as indicated by the log messages displayed in the GUI. Once complete, you should be able to connect to the bulb using your home Wi-Fi network.

## Dependencies
This script requires the following packages to be installed:
* `tkinter`
* `socket`
* `ssl`
* `io`

## How to Run
1. Clone this repository to your local machine.
2. Navigate to the directory containing the `OnboardGUI.py` script.
3. Run the script with the command `python OnboardGUI.py`.