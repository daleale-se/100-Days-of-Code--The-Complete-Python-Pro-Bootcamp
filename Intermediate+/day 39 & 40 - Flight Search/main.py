from data_manager import DataManager
from flight_search import FlightSearch
from utils import get_new_token

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
# classes to achieve the program requirements.


def main():

    data_manager = DataManager()
    flight_search = FlightSearch()
    data_manager.do_search(flight_search)


main()
