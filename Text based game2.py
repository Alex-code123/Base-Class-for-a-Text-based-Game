import time

class Text_Game:

    def __init__(self, writing_speed):
        # Typing speed
        self.writing_speed = writing_speed
        # For cool typing effects
        self.fancy_typing = False
        self.current_inventory = {
            # Enter items of inventory
        }
        self.last_saved_inventory = {}

    def inventory_update(self,current,save=False,get=False):
        if save:
            # Saves the inventory
            self.last_saved_inventory = self.current_inventory
        if get:
            # Returns the current inventory
            return self.current_inventory
        if current is not None:
            # Updates the current inventory to the one given
            self.current_inventory = current

    def print(self, text,title=True,fancy_typing=False):
        # Function that makes text printed out with a cool effect
        for letter in text:
            print(letter, end='')
            if fancy_typing:
                # If fancy_typing is True this effect will happen
                time.sleep(self.writing_speed)
        if title:
            #if the text is a title an extra line will be printed at the end of it
            print()
        print()

    def make_options(self,choice_titles):
        # Function that makes the different options get printed out
        for choice in choice_titles:
            self.print(choice,False,self.fancy_typing)

    def make_par(self,title_text,choices):
        # Function that prints out the title and options
        self.print(title_text,fancy_typing=self.fancy_typing)
        self.make_options(choices)

    def run(self):
        # Determines if it should do the cool typing effect or not
        if input("Would you like fancy typing(Yes,No): ") == "Yes":
            self.fancy_typing = True
        else:
            self.fancy_typing = False
        # Call a function here to start the main game


Text_Game(0.075).run()
