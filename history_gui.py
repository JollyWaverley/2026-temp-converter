from tkinter import*
from functools import partial
import all_constants as c


class Converter:

    """temperature conservation tool (c° to f° and f° to c°)"""
    def __init__(self):

        """temperature converter gui"""

        self.all_calculations_list = ['10.0 °F is -12°C', '20.0 °F is -7°C',
                                     '30.0 °F is -1°C', '40.0 °F is 4°C',
                                     '50.0 °F is 10°C', '60.0 °F is 16°C']


        self.temp_frame = Frame (padx=10, pady=10)
        self.temp_frame.grid()

        self.to_history_button = Button(self.temp_frame,
                                    text="Help / Info",
                                    bg="#CC6600",
                                    fg="#FFFFFF",
                                    font=("Arial", 14, "bold"), width=12,
                                    command=self.to_history)
        self.to_history_button.grid(row=1, padx=5, pady=5)


    def to_history(self):

        HistoryExport(self, self.all_calculations_list)

class HistoryExport:
    """
    Displays history dialogue box
    """


    def __init__(self, partner, calculations):
        # setup dialogue box and background

        self.history_box = Toplevel()

        # disable history button
        partner.to_history_button.config(state=DISABLED)


    # If users press the cross at the top, closes history
    # and 'releases' history button

        self.history_box.protocol('WM_DELETE_WINDOW',
        partial(self.close_history,partner))

        self.history_frame = Frame(self.history_box)
        self.history_frame.grid()

        # background colour and text for calculation area
        if len(calculations) <= c.MAX_CALCS:
            calc_back = "#D5E8D4"
            calc_amount = "all your"
        else:
            calc_back = "#FFE6CC"
            calc_amount = (f"your recent calculations - "
                           f"showing {c.MAX_CALCS} / {len(calculations)}")

        # strings for 'long' labels...
        recent_intro_txt = (f"Below are {calc_amount} calculations "
                            "(to the nearest degree).")


        export_instruction_txt = ("push the export button to save your work"
                                       "in a file.  If the file name already exists it will be over written")

        # Label list (label text | format | bg)
        history_labels_list = [
            ["History / Export", ("Arial", "16", "bold"), None],
            [recent_intro_txt, ("Arial", "11"), None],
            ["calculation list", ("Arial", "14"), calc_back],
            [export_instruction_txt, ("Arial", "11"), None]
        ]

    def close_history(self, partner):
        """
        Closes help dialogue (and enables help button)
        """

        # put help button back to normal
        partner.to_history_button.config(state=NORMAL)
        self.history_box.destroy()



# Main Routine / Testing starts here
if __name__ == "__main__":
    root = Tk()
    root.title("temperature converter")
    Converter()
    root.mainloop()