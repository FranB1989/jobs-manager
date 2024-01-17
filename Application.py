from Job import Job

class Application:
    def __init__(self, name):
        self._name = name
        self._jobs = []
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        self._name = new_name
    
    def add_job(self, job):
        self._jobs.append(job)
        job.application = self
    
    def show_jobs(self):
        return self._jobs
    
    def __str__(self):
        return f"Application: {self._name}"
