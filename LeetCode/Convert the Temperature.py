class Solution(object):
    def convertTemperature(self, celsius):
       Kelvin = round(celsius + 273.15,5)
       Fahrenheit = round(celsius * 1.80 + 32.00,5)
       return [Kelvin, Fahrenheit]


        