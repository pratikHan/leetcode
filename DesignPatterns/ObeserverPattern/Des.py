from ObeserverPattern.WeatherStation import WeatherStation
from ObeserverPattern.PhoneDisplay import PhoneDisplay, LCD

ws = WeatherStation(20)
ps = PhoneDisplay(ws)
lcd = LCD(ws)
ws.addViewers(ps)
ws.addViewers(lcd)
ws.notify()