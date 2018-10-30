# A class Country holds the information about a single country.
class Country:
    def __init__(self, name, pop, area, continent):  # Constructor including four instance variables.
        self._name = name
        self._population = int(pop)
        self._area = float(area)
        self._continent = continent

# A method to get country's name.
    def getName(self):
        return self._name

# A method to get country's population.
    def getPopulation(self):
        return self._population

# A metohod to get country's area.
    def getArea(self):
        return self._area

# A method to get the continent.
    def getContinent(self):
        return self._continent

# A method to set new population.
    def setPopulation(self, pop):
        self._population = pop

# A method to set new area.
    def setArea(self, area):
        self._area = area

# A method to set new continent.
    def setContinent(self, continent):
        self._continent = continent

# A method to get population density.
    def getPopDensity(self, pop, area):
        self._density = pop/area
        return "%.2f" % self._density

#  Generates a string representation for class objects.
    def __repr__(self):
        return str(self._name) + "(pop: " + str(self._population) + ", size: " + str(self._area) + ") in " + self._continent


