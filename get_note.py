from NoteTaking import NoteTaking
# import User

def requestUserInput():
    notePiece = NoteTaking()
    print(str(notePiece.get_date())+"\n\n")
    
    new_note = input("***Welcome, tell us about your day!***\n")
    notePiece.write_note(new_note)