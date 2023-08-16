"""
A timer I did during a train ride and got bored.
Uses for loop as its main function
and of course tkinter :)

Doesnt take into account the overflow
or what happens after hours/list ends.

"""

from tkinter import *
from tkinter.ttk import *

INTERVAL = 1000


class Timer:
    def __init__(self):
        self.__main_window = Tk()
        self.__main_window.title("Timer")

        #Numberss
        #1st 2: hr  #2nd 2:min  #3rd 2:sec
        self.__time_in_bytes = [0,0,0,0,0,0]

        #Numbers
        self.__the_hour = Label(self.__main_window,
                                text=str(self.__time_in_bytes[0])+str(self.__time_in_bytes[1]))
        self.__the_minutes = Label(self.__main_window,
                                text=str(self.__time_in_bytes[2]) + str(self.__time_in_bytes[3]))
        self.__the_seconds = Label(self.__main_window,
                                   text=str(self.__time_in_bytes[4]) + str(self.__time_in_bytes[5]))

        self.__the_hour.place(x=10, y=10)
        self.__the_minutes.place(x=50, y=10)
        self.__the_seconds.place(x=90, y=10)

        #Timer
        self.__main_window.after(INTERVAL,self._time)

        #Buttons
        self.__quit_button = Button(self.__main_window, text="Quit",command=self._quit)
        self.__quit_button.place(x=80, y=70, width=35)
        self.__continue_ticking = True
        self.__stop_button = Button(self.__main_window, text="Stop", command=self._stop)
        self.__stop_button.place(x=45, y=70, width=35)

        self.__main_window.mainloop()

    def _quit(self):
        self.__main_window.destroy()

    def _stop(self):
        if(self.__continue_ticking):
            self.__continue_ticking = False
        else:
            self.__continue_ticking = True

    def _time(self):

        #Stops counting if STOP button pushed
        if self.__continue_ticking:
            # Changes the timer's math
            self.change_time()

            #Changes the GUI, could also be done so
            # that if it needs updating it only updates then
            # by creating a return value for 'change_time'
            self.__the_hour.configure(text=str(self.__time_in_bytes[0])+str(self.__time_in_bytes[1]))
            self.__the_minutes.configure(text=str(self.__time_in_bytes[2]) + str(self.__time_in_bytes[3]))
            self.__the_seconds.configure(text=str(self.__time_in_bytes[4]) + str(self.__time_in_bytes[5]))

        #Repeats the process
        self.__main_window.after(INTERVAL, self._time)

    def change_time(self):
        """
        Updates the math behind the timer.
        Takes into account minutes' and seconds' 60 interval
        """
        list_length = len(self.__time_in_bytes) - 1

        for x in range(0,list_length):
            #For loop helps to reduce repetition

            #Iteration index helps us start from the last list item
            #Though this could have been done by negative numbers as well
            # list[-1] etc.
            iteration_index = int(list_length - x)

            if(x == 0):
                #Adds a second
                self.__time_in_bytes[iteration_index] = self.__time_in_bytes[iteration_index] + 1

            if((iteration_index % 2) == 0 and self.__time_in_bytes[iteration_index] >= 6):
                #When minutes and seconds hit full interval:

                self.__time_in_bytes[iteration_index] = 0

                #Checks so that it's not the last iteration.
                if (x != len(self.__time_in_bytes) - 1):
                    self.__time_in_bytes[iteration_index - 1] = self.__time_in_bytes[iteration_index - 1] + 1

            elif(self.__time_in_bytes[iteration_index] >= 10):
                self.__time_in_bytes[iteration_index] = 0

                if(x != len(self.__time_in_bytes)-1):
                    self.__time_in_bytes[iteration_index-1] = self.__time_in_bytes[iteration_index-1] + 1


def main():
    timer = Timer()


if __name__ == "__main__":
    main()