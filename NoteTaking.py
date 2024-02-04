from datetime import datetime

class NoteTaking:
    calendar = datetime.today().date()
    def __init__ (self, note_taking = None):
        self.note_taking = note_taking

    def get_date(self):
        return self.calendar

    def get_note_taking(self):
        return self.note_taking
    
    def write_note(self, new_note):
        self.note_taking = new_note
    