import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# delay = 1.000
# button = Button.right
start_stop_key = KeyCode(char="=")
exit_key = KeyCode(char="`")

delay = input("Do you want to click Fast or Faster? Type fast or faster: ")
if delay == "faster":
    delay = 0.01
else:
    delay = 0.1

button = input("Which key? Type exactly left or right: ")
if button == "right":
    button = Button.right
else:
    button = Button.left

print("Please wait...")
print("Program is ready! Press '=' to start and pause. Press '~' for emergency stop.")


class ClickMouse(threading.Thread):
    def __init__(self, delay, button):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.button = button
        self.running = False
        self.program_running = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def exit(self):
        self.stop_clicking()
        self.program_running = False

    def run(self):
        while self.program_running:
            while self.running:
                mouse.click(self.button)
                time.sleep(self.delay)


mouse = Controller()
click_thread = ClickMouse(delay, button)
click_thread.start()


def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()


with Listener(on_press=on_press) as listener:
    listener.join()
