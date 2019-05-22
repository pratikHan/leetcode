from ObeserverPattern.Observer import Observer
from ObeserverPattern.WeatherStation import WeatherStation



class PhoneDisplay(Observer):

    ws: WeatherStation

    def __init__(self, ws):
        print("Phone constructor :")
        self.ws = ws
        self.display()

    def display(self):
        print(self.ws.temperature)

class LCD(Observer):
    ws: WeatherStation
    def __init__(self, ws):
        print("LCD constructor")
        self.ws = ws
        self.display()

    def display(self):
        print(self.ws.temperature)