class Incident:
    __max_id = 0

    def __init__(self, description, priority, time, reporting ):
        Incident.__max_id += 1  
        self.id = Incident.__max_id  
        self.description = description
        self.priority = priority
        self.time = time
        self.reporting = reporting

    def __repr__(self):
        return f"Incident(id={self.id!r}, description={self.description!r})"

    def __str__(self):
        return f"Incident {self.id}: {self.description} \nPriority: {self.priority}, Time of report: {self.time}, Reported by: {self.reporting} "