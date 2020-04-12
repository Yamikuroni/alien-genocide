class Settings():
    #Class that will store all of the game settings

    def __init__(self):
        """Initializing game settings"""

        # Display setings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (81, 86, 89)

        # Ship settings
        self.ship_speed_factor = 6.5
