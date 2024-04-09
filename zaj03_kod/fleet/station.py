class Station:
    __max_id = 0

    def __init__(self, location, ambulance, driver, employee):
        Station.__max_id += 1 
        self.id = Station.__max_id 
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee

    def availability(self):
        if self.location == self.ambulance.location:
            av = True
            print(f"Stacja {self.id} posiada dostepna karetke")
        else:
            av = False
            print(f"Stacja {self.id} nie posiada dostepnej karetki")
        return av
    
    