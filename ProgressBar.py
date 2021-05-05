#!/usr/bin/env python3
# .........................
# .. Progress Bar Class  ..
# .. Auth: Damian Costales.
# .........................
# .. Updated 9/12/18     ..
# .........................

class ProgressBar(object):
       
    # SETTINGS VARIABLES =====================================================================================
    # ========================================================================================================
    bar_visual_length = 100
    bar_max = 100
    display_string = ""
    current_status = ""
    percent = 0.0
    
    # settings
    show_percentage = True    
    filled_char = '█'
    empty_char = '░'
    left_end_char = '('
    right_end_char = ')'    
    
    # CONSTRUCTOR ============================================================================================
    # ========================================================================================================
    
    def __init__(self,bar_visual_length,bar_max):
        if(bar_visual_length <= 0):
            self.bar_visual_length = 1
        else:
            self.bar_visual_length = bar_visual_length
        if(bar_max <= 0):
            self.bar_max = 1
        else:
            self.bar_max = bar_max       
        
    # SETTINGS FUNCTIONS =====================================================================================
    # ========================================================================================================
    # changes the char for the default filled and empty chars, the bar max length, and the visual length of the bar
    def ChangeFilledChar(self, new_char):
        if(not new_char): 
            return
        new_char = new_char[0]
        self.filled_char = new_char
        return
    def ChangeEmptyChar(self, new_char):
        if(not new_char): 
            return
        new_char = new_char[0]
        self.empty_char = new_char
        return
    def ChangeLRChar(self, new_char_l,new_char_r):
        if(not new_char_l or not new_char_r): 
            return
        self.left_end_char = new_char_l[0]
        self.right_end_char = new_char_r[0]
        return
    def ChangeBarMax(self, new_max):
        if(new_max <= 0):
            bar_max=1            
        else:
            self.bar_max = new_max
        return
    def ChangeVisualLength(self, new_length):
        if(new_length <= 0):
            self.bar_visual_length = 1
        else:
            self.bar_visual_length = round(new_length)
        return
    
    # OPERATION FUNCTIONS ====================================================================================
    # ========================================================================================================
    
    def Update(self, current_value):
        # calculates the length of the shaded amount of the bar
        shaded_length = int(round(self.bar_visual_length * current_value / float(self.bar_max)))
        # calculates the percentage of completion 
        self.percent = round(100.0 * current_value / float(self.bar_max), 1)
        # creates a text bar representation using the filled and empty chars
        bar_string = self.filled_char * shaded_length + self.empty_char * (self.bar_visual_length - shaded_length) 
        if(self.show_percentage):
            self.display_string = ('%s%s%s %s%s' % (self.left_end_char, bar_string, self.right_end_char, self.percent, '%'))
        else:
            self.display_string = ('%s%s%s' % (self.left_end_char, bar_string, self.right_end_char))
        return 
    
    def UpdateWithStatus(self, current_value, status_text):
        # calculates the length of the shaded amount of the bar
        shaded_length = int(round(self.bar_visual_length * current_value / float(self.bar_max)))
        # calculates the percentage of completion 
        self.percent = round(100.0 * current_value / float(self.bar_max), 1)
        # creates a text bar representation using the filled and empty chars
        bar_string = self.filled_char * shaded_length + self.empty_char * (self.bar_visual_length - shaded_length) 
        #sets the status to be displayed at the end of the bar
        self.current_status = status_text
        if(self.show_percentage):
            self.display_string = ('%s%s%s %s%s %s' % (self.left_end_char, bar_string, self.right_end_char, self.percent, '%', self.current_status))
        else:
            self.display_string = ('%s%s%s %s' % (self.left_end_char, bar_string, self.right_end_char, self.current_status))
        return