#Call Center: Imagine you have a call center with three levels of employees: respondent,
# manager, and director. An incoming telephone call must be first allocated to a respondent who is free.
#If the respondent can't handle the call, he or she must escalate the call to a manager.
#If the manager is not free or not able to handle it, then the call should be escalated to a director.
#Design the classes and data structures for this problem. Implement a method dispatchCall( } which assigns a call to the first available employee.
class employee():

    def __init__(self):
        self.call = None
        self.rank = None

    def take_call(self,call):
        self.call = call

    def end_call(self):
        self.call = None

    def is_available(self):
        return self.call is None

    def scale_up(self):
        self.call.rank += 1
        # send call to queue
        self.end_call()

class respondent(employee):
    def __init__(self):
        self.rank = 0

class manager(employee):
    def __init__(self):
        self.rank = 1

class director(employee):
    def __init__(self):
        self.rank = 2


class Call():
    def __init__(self,caller):
        self.start_time = datetime.now()
        self.caller = caller
        self.rank = 0
        self.employee = None
        self.end_time = None

    def employee_on_line(self, employee):
        self.employee = employee

    def end_call(self):
        self.end_time = datetime.now()

    def duration(self):

        if self.end_time is None:
            return (datetime.now() - self.start_time).total_seconds() # in seconds
        else:
            return (self.end_time - self.start_time).total_seconds() # in seconds

class callcenter():
    def __init__(self):
        self.respondents= []
        self.managers = []
        self.directors = []
        self.calls = [] #queue
        for i in range(10):
            respondent = respondent()
            self.respondents.append(respondent)
        for i in range(4):
            manager = manager()
            self.managers.append(manager)
        for i in range(2):
            director = director()
            self.directors.append(director)

    def add_call(self,call):
        self.calls.append(call)
    def remove_call(self):
        self.calls.pop(0)

    def dispatchCall(self):
        responded = False
        employees=[]
        employees[0] = self.respondents
        employees[1] = self.managers
        employees[2] = self.directors
        a = 0
        while(responded == False and i<3):
            for i in range(len(employees[a])):
                if employees[a][i].is_available():
                    employees[a][i].take_call(self.calls[0])
                    responded = True
            i+=1
        self.remove_call()


def main():
    my_call_center = callcenter()
