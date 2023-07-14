class inc():
    def __init__(self,date,who,ammount):
        self.date = date
        self.kwota=ammount
        if who == "AMS":
            self.who="N"
        if who == "STT":
            self.who="P"

    