class InputReader:

    def __init__(self, fileName):
        self.file = None
        self.lines = None
        self.commands = None
        self.fileName = fileName

    def StoreInputData(self):
        self.file = open("./vbn\\"+self.fileName, "r")  # opens file with name of "ADT.txt"
        self.lines = self.file.readlines()
        self.file.close()

    def InputFileToCommands(self):
        iterator = 0
        self.commands = []
        while iterator != len(self.lines):
            if self.lines[iterator][0] != '#' and self.lines[iterator] != "\n":
                if iterator != len(self.lines)-1:
                    self.commands.append(self.lines[iterator][: -1])
                else:
                    self.commands.append(self.lines[iterator])
            iterator += 1
        for i in range(len(self.commands)):
            self.commands[i] = self.commands[i].split()
        self.commands = [item for sublist in self.commands for item in sublist]