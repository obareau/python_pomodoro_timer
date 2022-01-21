# A simple pomodoro timer
from ast import Pass
import time
import threading
import tkinter as tk
from tkinter import ttk, PhotoImage

class PomodoroTimer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x300")
        self.root.title("Olives & Pomodoro Timer")
        self.root.tk.call('wm', 'iconphoto', self.root._w, PhotoImage(file="pomodoro.png"))
        
        self.s = ttk.Style()
        self.s.configure("TNotebook.Tab", font=("Ubuntu", 16))
        self.s.configure("TButton", font=("Ubuntu", 16))
        
        self.tabs = ttk.Notebook(self.root)
        self.tabs.pack(fill="both", pady=10, expand=True)
        
        self.tab1 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab2 = ttk.Frame(self.tabs, width=600, height=100)
        self.tab3 = ttk.Frame(self.tabs, width=600, height=100)
        
        self.pomodoro_timer_label = ttk.Label(self.tab1, text="25:00", font=("Ubuntu, 64"))
        self.pomodoro_timer_label.pack(pady=20)
        
        self.short_break_timer_label = ttk.Label(self.tab2, text="05:00", font=("Ubuntu, 64"))
        self.short_break_timer_label.pack(pady=20)
        
        self.long_break_timer_label = ttk.Label(self.tab3, text="15:00", font=("Ubuntu, 64"))
        self.long_break_timer_label.pack(pady=20)
        
        self.tabs.add(self.tab1, text="Pomodoro")
        self.tabs.add(self.tab2, text="Short Break")
        self.tabs.add(self.tab3, text="Long Break")
        
        self.grid_layout = ttk.Frame(self.root)
        self.grid_layout.pack(pady=10)
        
        self.start_button = ttk.Button(self.grid_layout, text="Start", command=self.start_timer_thread)
        self.start_button.grid(row=0, column=0)
        
        self.skip_button = ttk.Button(self.grid_layout, text="Skip", command=self.skip_clock)
        self.skip_button.grid(row=0, column=1)
        
        self.reset_button = ttk.Button(self.grid_layout, text="Reset", command=self.reset_clock)
        self.reset_button.grid(row=0, column=2)
        
        self.pomodoro_counter_label = ttk.Label(self.grid_layout, text="Pomodoros : 0", font=("Ubuntu", 16))
        self.pomodoro_counter_label.grid(row=1, column=0, columnspan=3, pady=10)
        
        self.pomodoros = 0
        self.skipped = False
        self.stopped = False
        
        
        
        self.root.mainloop()

    def start_timer_thread(self):
        t = threading.Thread(target=self.start_timer)
        t.start()
        
    def start_timer(self):
        self.skipped = False
        self.stopped = False    
        timer_id = self.tabs.index(self.tabs.select()) + 1

        if timer_id == 1:
            full_seconds = 60 * 25
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.pomodoro_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.pomodoros += 1
                self.pomodoro_counter_label.config(text=f"Pomodoros: {self.pomodoros}")
                if self.pomodoros % 4 == 0:
                    self.tabs.select(2)
                    self.start_timer()
                else:
                    self.tabs.select(1)
                self.start_timer()
                
        elif timer_id == 2:
            full_seconds = 60 +5
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.short_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
        
        elif timer_id == 3:
            full_seconds = 60 * 15
            while full_seconds > 0 and not self.stopped:
                minutes, seconds = divmod(full_seconds, 60)
                self.long_break_timer_label.config(text=f"{minutes:02d}:{seconds:02d}")
                self.root.update()
                time.sleep(1)
                full_seconds -= 1
            if not self.stopped or self.skipped:
                self.tabs.select(0)
                self.start_timer()
            
    def reset_clock(self):
        pass
    
    def skip_clock(self):
        pass
    

PomodoroTimer()
