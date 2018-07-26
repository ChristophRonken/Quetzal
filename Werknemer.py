WorkerIdCount = 1


class Worker:

    def __init__(self, firstName, lastName, workLoad):
        global WorkerIdCount
        self.workerId = WorkerIdCount
        self.firstName = firstName
        self.lastName = lastName
        self.workLoad = workLoad
        WorkerIdCount += 1

    def beBusy(self):
        return
