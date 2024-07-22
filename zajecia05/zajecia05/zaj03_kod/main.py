from fleet.ambulance import Ambulance
from operations import *
from personnel import *
from fleet.station import Station
from utils.get_logger import get_logger

logger = get_logger(__name__)


def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance("Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 12000.0)
    employee2 = Employee("Jane", "Smith", 8000.0)

    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])
    
    # sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        logger.warning("To są te same karetki!")
        raise ValueError("To są te same karetki!")

    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # stacje
    station1 = Station((50.095340, 18.920282), ambulance1, driver1, employee1)
    station2 = Station((50.095310, 18.920292), ambulance2, driver2, employee2)
    
    station1.availability()
    station2.availability()
    
    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie 2 zgłoszeń
    incident1 = Incident("Power outage in sector 4", 2, "10:00 20.02.2024", "Anna Green")
    incident2 = Incident("Fire alarm in building 21", 1, "10:30 20.02.2024", "John White")
    queue += incident1
    queue += incident2

    # wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # daj kierowcy podwyżkę za super zasługi
    # print(f"Przed podwyżką: {driver1.display_info()}")
    # driver1.update_salary(5000.12)
    # print(f"Po podwyżce: {driver1.display_info()}")


if __name__ == "__main__":
    run_application()