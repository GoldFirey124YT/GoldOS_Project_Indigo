import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit
import paho.mqtt.client as mqtt

# Set up the MQTT client
client = mqtt.Client()
client.connect("mqtt.eclipse.org", 1883, 60)

# Define the message handler
def on_message(client, userdata, message):
    print(message.topic, message.payload.decode())

# Set up the message handler
client.on_message = on_message

# Start the MQTT client loop
client.loop_start()

# Define the GUI
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Project Indigo")
        self.setGeometry(100, 100, 400, 300)

        self.input_box = QLineEdit(self)
        self.input_box.move(50, 50)
        self.input_box.resize(200, 30)

        self.send_button = QPushButton("Send", self)
        self.send_button.move(50, 100)
        self.send_button.clicked.connect(self.send_message)

    def send_message(self):
        message = self.input_box.text()
        client.publish("my/topic", message)
        self.input_box.clear()

# Start the GUI
app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
