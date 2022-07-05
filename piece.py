class Piece():
    def __init__(self, hasBomb):
        self.hasBomb = hasBomb
        self.cliicked = False
        self.flagged = False

    def getHasBomb(self):
        return self.hasBomb
    def getClicked(self):
        return self.clicked
    def getFlagged(self):
        return self.flagged