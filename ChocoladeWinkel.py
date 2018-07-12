from InputReader import InputReader
from ADT_Christoph.Stack.Stack import Stack
from Wrapper import StackWrapper


class Store:

    def __init__(self):
        self.inputReader = InputReader()
        self.inputReader.StoreInputData()
        self.inputReader.InputFileToCommands()
        self.Wrapper = None

    def runSimulation(self):
        i = 21
        while i != len(self.inputReader.commands):
            print(self.inputReader.commands[i])
            if self.inputReader.commands[i] == "type=stack":
                self.Wrapper = StackWrapper()
                i += 1
            elif self.inputReader.commands[i] == "insert":
                i += 1
                self.Wrapper.insert(self.inputReader.commands[i])
                i += 1
            elif self.inputReader.commands[i] == "delete":
                self.Wrapper.delete()
                i += 1
            else:
                i += 1
                pass
        return


Quetzal = Store()
Quetzal.runSimulation()

