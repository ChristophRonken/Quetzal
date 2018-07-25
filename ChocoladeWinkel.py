from InputReader import InputReader
from Wrapper import StackWrapper, BSTWrapper, QueueWrapper, DLCWrapper, HashWrapper, CLCWrapper
from ADT_Christoph.HashTable.HashTable import HashTableType


class Store:

    def __init__(self):
        self.inputReader = InputReader()

        self.inputReader.StoreInputData()
        self.inputReader.InputFileToCommands()
        self.Wrapper = None

    def runADTSimulation(self):
        i = 0
        newItem = False
        searchkey = False
        while i != len(self.inputReader.commands):
            print(self.inputReader.commands[i])

            if self.inputReader.commands[i] == "type=bst":
                self.Wrapper = BSTWrapper()
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=stack":
                self.Wrapper = StackWrapper()
                self.Wrapper.create()
                newItem = True
                searchkey = False
                i += 1

            elif self.inputReader.commands[i] == "type=queue":
                self.Wrapper = QueueWrapper()
                self.Wrapper.create()
                newItem = True
                searchkey = False
                i += 1

            elif self.inputReader.commands[i] == "type=dll":
                self.Wrapper = DLCWrapper()
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=cll":
                self.Wrapper = CLCWrapper()
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=hlin":
                self.Wrapper = HashWrapper()
                self.Wrapper.ADT.type = HashTableType.Type1
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=hquad":
                self.Wrapper = HashWrapper()
                self.Wrapper.ADT.type = HashTableType.Type2
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "type=hsep":
                self.Wrapper = HashWrapper()
                self.Wrapper.ADT.type = HashTableType.Type3
                self.Wrapper.create()
                newItem = False
                searchkey = True
                i += 1

            elif self.inputReader.commands[i] == "insert":
                i += 1
                if not newItem:
                    self.Wrapper.insert(int(self.inputReader.commands[i]), None)
                elif not searchkey:
                    self.Wrapper.insert(None, int(self.inputReader.commands[i]))
                i += 1
            elif self.inputReader.commands[i] == "delete":
                i += 1
                if not searchkey:
                    self.Wrapper.delete(None)
                else:
                    self.Wrapper.delete(int(self.inputReader.commands[i]))
                    i += 1

            elif self.inputReader.commands[i] == "print":
                self.Wrapper.print()
                i += 1

        return

