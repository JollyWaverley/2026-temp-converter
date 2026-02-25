
from tkinter import*
from functools import  partial

class Converter:

    """temperature conservation tool (c° to f° and f° to c°)"""
    def __init__(self):

        """temperature converter gui"""

        self.all_calculations_list = []

        self.temp_frame = Frame (padx=10, pady=10)
        self.temp_frame.grid()

        self.to_help_button = Button(self.temp_frame,
                                    text="Help / Info",
                                    bg="#CC6600",
                                    fg="#FFFFFF",
                                    font=("Arial", 14, "bold"), width=12,
                                    command=self.to_help)
        self.to_help_button.grid(row=1, padx=5, pady=5)


    def to_help(self):
        """
        Opens help text and disables help buttons so multiple boxes are
         not created
        """
        DisplayHelp(self)


class DisplayHelp:
    """
    displays help box
    """

    def __init__(self, partner):

        # setup dialogue box and background
        background = "#ffe6cc"
        self.help_box = Toplevel()

        # disable help button
        partner.to_help_button.config(state=DISABLED)

        # If users press cross at the top, closes help and releases help button
        self.help_box.protocol('WM_DELETE_WINDOW',
                               partial(self.close_help,partner))

        self.help_frame = Frame(self.help_box, width=300,
                                height=200)
        self.help_frame.grid()

        self.help_heading_label = Label(self.help_frame,
                                        text="Help / info",
                                        font=("Arial", 14, "bold"))
        self.help_heading_label.grid(row=0)


        help_text = ("To use the program, simply enter the temperature "
                     "you wish to convert to either degrees Celsius "
                     "(centigrade) or Fahrenehit \n"
                     "Here is more...\n"
                     "and this is a final paragraph.")


        self.help_text_label = Label(self.help_frame,
                                     text=help_text, wraplength=350,
                                     justify="left")
        self.help_text_label.grid(row=1, padx=10)

        self.dismiss_button = Button(self.help_frame,
                                    font=("Arial", 12, "bold"),
                                    text="dismiss", bg="#CC6600",
                                    fg="#FFFFFF",
                                    command=partial(self.close_help, partner))
        self.dismiss_button.grid(row=2, padx=10, pady=10)


        # List and loop to set background colour on
        # everything except the button

        recolour_list = [self.help_frame, self.help_heading_label,
                         self.help_text_label]



        for item in recolour_list:
            item.config(bg=background)

    def close_help(self, partner):
        """
        Closes help dialogue (and enables help button)
        """

        # put help button back to normal
        partner.to_help_button.config(state=NORMAL)
        self.help_box.destroy()

# Main Routine / Testing starts here
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()
