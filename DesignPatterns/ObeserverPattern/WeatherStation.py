from ObeserverPattern.Observer import Observer


class WeatherStation(object):

    temperature = 0
    sunrise = 0
    sunset = 0
    humidity = 0
    precipitation = 0

    obslist = []

    def __init__(self, temp):
        self.temperature = temp


    def notify(self):


            obs = Observer()
            obs.display()


    def addViewers(self, observer):
        self.obslist.append(observer)