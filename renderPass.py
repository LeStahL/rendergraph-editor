class renderPass:
    idCounter = 0

    def __init__(self):
        self.id = self.idCounter
        self.idCounter += 1
        self.name = ""
        return
