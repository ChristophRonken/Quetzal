WorkerIdCount = 1


class Worker:

    def __init__(self, firstName, lastName, workLoad):
        global WorkerIdCount
        self.workerId = WorkerIdCount
        self.firstName = firstName
        self.lastName = lastName
        self.workLoad = workLoad
        self.order = None
        self.busyTime = 0
        self.isBusy = False
        self.chocolateMilk = None
        WorkerIdCount += 1

    def actBusy(self, busy):
        self.isBusy = busy
        return
