class InputReader:

    def __init__(self, fileName):
        self.__file = None
        self.__lines = None
        self.__commands = None
        self.__fileName = fileName

    def StoreInputData(self):
        self.__file = open("./InputFiles/"+self.__fileName, "r")  # opens file with fileName
        self.__lines = self.__file.readlines()
        self.__file.close()
        return

    def InputFileToCommands(self):
        iterator = 0
        self.__commands = []
        while iterator != len(self.__lines):
            if self.__lines[iterator][0] != '#' and self.__lines[iterator] != "\n":
                if iterator != len(self.__lines)-1:
                    self.__commands.append(self.__lines[iterator][: -1])
                else:
                    self.__commands.append(self.__lines[iterator])
            iterator += 1
        for i in range(len(self.__commands)):
            self.__commands[i] = self.__commands[i].split()
        self.__commands = [item for sublist in self.__commands for item in sublist]
        return

    def getLines(self):
        return self.__lines

    def getCommands(self):
        return self.__commands

    def getFile(self):
        return self.__file

    def getFileName(self):
        return self.__fileName
