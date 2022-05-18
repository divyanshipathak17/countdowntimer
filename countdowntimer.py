


# *************IMPOTING MODULES************

import threading
import time
import tkinter as tk
# winsound module works only for windows software, so if your device does not have windows, comment out the winspund part i.e line 7 and line 139 and 149
# also mac os software doesn't support background colour for buttons, so i'd suggest you to use windows software as this application looks more interactive on windows
import winsound as ws


# ************CREATING A CLASS************

class CountdownTimer:

    def __init__(self):

        # creating tkinter window
        self.root = tk.Tk()
        self.root.geometry('800x550')
        self.root.title("Timer")
        self.root.configure(background="#1d1f1f")
        self.root.resizable(False, False)

        # creating attributes
        self.seconds_remaining = None
        self.stop_loop = False

        # label asking to enter time
        self.enter_time_label = tk.Label(self.root,
                                         font=("Courier new", 65),
                                         text="hh:mm:ss",
                                         bg="#1d1f1f",
                                         fg="white")

        self.enter_time_label.pack(pady=10)

        # entry box to enter time
        self.text = tk.StringVar()
        self.text.set("00:00:00")
        self.enter_time = tk.Entry(self.root,
                                   textvariable=self.text,
                                   font=("Courier new", 70),
                                   width=8,
                                   bg="#3c4242",
                                   fg="white",
                                   highlightbackground="black")

        self.enter_time.pack(pady=10)

        # label to display time left
        self.time_label = tk.Label(self.root,
                                   font=("Courier new", 45),
                                   text="Time left: 00:00:00",
                                   bg="#1d1f1f",
                                   fg="white")

        self.time_label.pack(pady=10)

        # creating start, pause, and reset buttons
        self.start_button = tk.Button(self.root,
                                      font=("Courier new", 30),
                                      text="Start/\nResume",
                                      height=3,
                                      width=8,
                                      bg="#529c5c",
                                      fg="#3c4242",
                                      activebackground="#42ed78",
                                      highlightbackground="black",
                                      command=self.start_thread)

        self.start_button.pack(side=tk.LEFT, padx=50)

        self.pause_button = tk.Button(self.root,
                                      font=("Courier new", 30),
                                      text="Pause",
                                      height=3,
                                      width=8,
                                      bg="#b84844",
                                      fg="#3c4242",
                                      activebackground="#f23c35",
                                      highlightbackground="black",
                                      command=self.pause)

        self.pause_button.pack(side=tk.LEFT)

        self.reset_button = tk.Button(self.root,
                                      font=("Courier new", 30),
                                      text="Reset",
                                      height=3,
                                      width=8,
                                      bg="#3c85c9",
                                      fg="#3c4242",
                                      activebackground="#22b0e3",
                                      highlightbackground="black",
                                      command=self.reset)

        self.reset_button.pack(side=tk.LEFT, padx=50)

        # running of the window
        self.root.mainloop()

    # creating thread for multitasking for eg, running timer and moving the window or typing another time in entry box
    def start_thread(self):

        t = threading.Thread(target=self.start)
        t.start()

    # creating start function
    def start(self):

        self.stop_loop = False
        hours, minutes, seconds = 0, 0, 0
        string_split = self.enter_time.get().split(":")

        if len(string_split) == 3:
            hours = int(string_split[0])
            minutes = int(string_split[1])
            seconds = int(string_split[2])

        elif len(string_split) == 2:
            minutes = int(string_split[0])
            seconds = int(string_split[1])

        elif len(string_split) == 1:
            seconds = int(string_split[0])

        else:
            print("Invalid input")

        self.enter_time.delete(0, "end")
        self.enter_time.insert(0, "00:00:00")
        self.seconds_remaining = hours * 3600 + minutes * 60 + seconds
        self.countdown()

        # if your os is not windows comment out this block, as this is the part of winsound library
        if not self.stop_loop:
            ws.Beep(800, 2000)

    # countdown function for updating time(decrementing time every second)
    def countdown(self):

        while self.seconds_remaining > 0 and not self.stop_loop:
            self.seconds_remaining -= 1
            minutes, seconds = divmod(self.seconds_remaining, 60)
            hours, minutes = divmod(minutes, 60)
            self.time_label.config(text=f"Time left : {hours:02d}:{minutes:02d}:{seconds:02d}")
            self.root.update()
            time.sleep(1)

    # creating pause function
    def pause(self):

        if self.stop_loop:
            self.stop_loop = False
            self.countdown()

        else:
            self.stop_loop = True

        string_split = self.time_label.cget("text").split(":")
        if len(string_split) == 4:
            hours = int(string_split[1])
            minutes = int(string_split[2])
            seconds = int(string_split[3])
            self.enter_time.delete(0, "end")
            self.enter_time.insert(0, f"{hours:02d}:{minutes:02d}:{seconds:02d}")

    # creating reset function
    def reset(self):

        self.stop_loop = True
        self.time_label.config(text="Time left: 00:00:00")
        self.enter_time.delete(0, "end")
        self.enter_time.insert(0, "00:00:00")


# calling the class
CountdownTimer()
