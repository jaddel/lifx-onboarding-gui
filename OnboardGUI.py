# OnboardGUI.py
# INSTRUCTIONS FOR USING LIFX BULB ONBOARDER GUI
#
# 1. Bring the bulb into pairing mode by following the instructions provided by LIFX.
#    This usually involves turning the bulb on and off a certain number of times until it starts flashing rapidly.
#
# 2. Connect your computer or mobile device to the Wi-Fi network created by the bulb.
#    This network name should start with "LIFX".
#
#    NOTE: If the bulb has not yet created a Wi-Fi network, you may need to wait up to 15 minutes
#    for it to do so. After this time, the bulb will be creating its own Wi-Fi network that you can
#    connect to.
#
# 3. Enter the Wi-Fi network name and password for your home Wi-Fi network into the "SSID" and "Password" fields in the GUI, respectively.
#
# 4. Click the "Onboard Bulb" button to start the onboarding process.
#
# 5. Wait until the onboarding process is complete, as indicated by the log messages displayed in the GUI.
#    Once complete, you should be able to connect to the bulb using your home Wi-Fi network.

import tkinter as tk
import socket, ssl
import io

class Onboarding:
    def __init__(self, ssid, password):
        self.ssid = ssid
        self.password = password
        self.log = io.StringIO()

    def write(self, message):
        self.log.write(message)

    def onboard(self):
        onboard_packet = b'\x86\x00\x00\x34\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x31\x01\x00\x00\x02'
        onboard_packet += self.ssid.ljust(32, '\x00').encode('utf-8')
        onboard_packet += self.password.ljust(64, '\x00').encode('utf-8')
        onboard_packet += b'\x05'

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        sock = ctx.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
        try:
            sock.connect(('172.16.0.1', 56700))
            self.write("Sending onboard packet to LIFX bulb...\n")
            sock.write(onboard_packet)
            self.write("Sent onboard packet to LIFX bulb.\n")
            self.write("LIFX bulb probably onboarded. Best of luck ;-)\n")
        except Exception as e:
            self.write("Error: " + str(e) + "\n")

class OnboardGUI(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("LIFX Bulb Onboarder")
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.ssid_label = tk.Label(self, text="SSID:")
        self.ssid_label.pack()
        self.ssid_entry = tk.Entry(self)
        self.ssid_entry.pack()

        self.password_label = tk.Label(self, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self, show="")
        self.password_entry.pack()

        self.onboard_button = tk.Button(self, text="Onboard Bulb", command=self.onboard)
        self.onboard_button.pack()

        self.log_label = tk.Label(self, text="Log:")
        self.log_label.pack()
        self.log_text = tk.Text(self, height=10, state="disabled")
        self.log_text.pack()

    def log(self, message):
        self.log_text.configure(state="normal")
        self.log_text.insert(tk.END, message)
        self.log_text.configure(state="disabled")
        self.log_text.see(tk.END)

    def onboard(self):
        ssid = self.ssid_entry.get()
        password = self.password_entry.get()

        onboard = Onboarding(ssid, password)
        onboard.write("Starting LIFX bulb onboarding...\n")
        onboard.onboard()
        self.log(onboard.log.getvalue())

if __name__ == "__main__":
    root = tk.Tk()
    app = OnboardGUI(master=root)
    app.mainloop()
