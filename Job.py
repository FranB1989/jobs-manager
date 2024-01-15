from Calendar import Calendar

class Job:
    def __init__(self, name, type, calendar):
        self._name = name
        self._type = type
        self._status = None
        self._calendar = calendar
        self._application = None
    
    @property
    def application(self):
        return self._application
    
    @application.setter
    def application(self, nueva_application):
        self._application = nueva_application
    
    @property
    def name(self):
        return self._name    
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    @property
    def type(self):
        return self._type
    
    @type.setter
    def type(self, new_type):
        self._type = new_type
    
    @property
    def status(self):
        return self._status
    
    @status.setter
    def status(self, new_status):
        self._status = new_status

    @property
    def calendar(self):
        return self._calendar
    
    @calendar.setter
    def calendar(self, new_calendar):
        self._calendar = new_calendar
