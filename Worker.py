class Worker:

    def __init__(self, firstName, lastName, workLoad, workerIdCount):
        self.__workerId = workerIdCount
        self.__firstName = firstName
        self.__lastName = lastName
        self.__workLoad = workLoad
        self.__order = None
        self.__busyTime = 0
        self.__isBusy = False
        self.__chocolateMilk = None

    @property
    def searchkey(self):
        return None

    def getWorkerId(self):
        return self.__workerId

    def getFirstName(self):
        return self.__firstName

    def getLastName(self):
        return self.__lastName

    def getWorkLoad(self):
        return self.__workLoad

    def getOrder(self):
        return self.__order

    def getBusyTime(self):
        return self.__busyTime

    def getIsBusy(self):
        return self.__isBusy

    def getChocolateMilk(self):
        return self.__chocolateMilk

    def setOrder(self, order):
        self.__order = order
        return True

    def setBusyTime(self, busyTime):
        self.__busyTime = busyTime
        return True

    def setIsBusy(self, isBusy):
        self.__isBusy = isBusy
        return True

    def setChocolateMilk(self, chocolateMilk):
        self.__chocolateMilk = chocolateMilk
        return True

