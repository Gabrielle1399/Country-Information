# This class will use two files to build the data structures to hold the information about countries and continents.
# 12 methods are included in the CountryCatalogue class.
# import country class from country file.
from country import Country


class CountryCatalogue:
    def __init__(self, continent, data):  # pass two txt files as parameters in constructor.
        continentfile = open(continent, "r")
        datafile = open(data, "r")
        self._countryCat = []
        self._cDictionary = {}

        continentfile.readline()  # read first line of the countryfile, exclude that from self._cDictionary.
        for line in continentfile:
            line = line.strip()
            parts = line.split(",")  # split by comma.
            self._countryName = parts[0]
            self._countryContinent = parts[1]
            self._cDictionary[parts[0]] = parts[1]  # append country name as key and corresponding continent as value.

        datafile.readline()  # read first line of the countryfile, exclude that from self._countryCat.
        for line in datafile:
            line = line.strip()
            line = line.replace(",", "")  # eliminate commas between numbers.
            parts = line.split("|")  # split by "|".
            self._countryData = Country(parts[0], parts[1], parts[2], self._cDictionary[parts[0]])
            self._countryCat.append(self._countryData)  # add country object to the list.

    def findCountry(self, name):
        for i in range(len(self._countryCat)):
            if name == self._countryCat[i].getName():  # to fine if the name exists in the list.
                return self._countryCat[i]
        else:
            return

    def setPopulationOfCountry(self, name, newpop):
        for i in range(len(self._countryCat)):
            if name == self._countryCat[i].getName():
                self._countryCat[i].setPopulation(newpop)  # call the "setPopulation" method in country class.
                return True
        else:
            return False

    def setAreaOfCountry(self, name, newarea):
        for i in range(len(self._countryCat)):
            if name == self._countryCat[i].getName():
                self._countryCat[i].setArea(newarea)  # # call the "setArea" method in country class.
                return True
        else:
            return False

    def addCountry(self, name, pop, area, continent):
        if name not in self._cDictionary:
            self._newCountry = Country(name, pop, area, continent)
            self._countryCat.append(self._newCountry)  # add new country to the self._countryCat list.
            self._cDictionary[name] = continent  # add new country to the self._cDictionary.
            return True
        else:
            return False

    def deleteCountry(self, name):
        if name in self._cDictionary:
            self._cDictionary.pop(name)
        self._newlist = []  # create a new list to store country that won't be deleted.
        for i in range(len(self._countryCat)):
            if name != self._countryCat[i].getName():
                self._newlist.append(self._countryCat[i])  # append countries to the newlist except the one that is deleted.
        self._countryCat = self._newlist
        return self._countryCat

    def printCountryCatalogue(self):
        print(self._countryCat.__repr__())

    def getCountriesByContinent(self, continent):
        self._countrylist = []
        for i in range(len(self._countryCat)):
            if continent == self._countryCat[i].getContinent():  # to check if continent exists in the country catalogue.
                self._countrylist.append(self._countryCat[i])  # add that country into the list.
        return self._countrylist

    def getCountriesByPopulation(self, continent = ""):  # parameter with default value -- "".
        self._listP = []
        for i in range (len(self._countryCat)):
            self._tup = self._countryCat[i].getName(), self._countryCat[i].getPopulation()  # create a tuple with name and population.
            if continent == self._countryCat[i].getContinent():
                self._listP.append(self._tup)
            elif continent == "":  # if continent is default value, add each the country to the list.
                self._listP.append(self._tup)
        self._listP.sort(key = lambda tup: tup[1], reverse = True)  # sort the list with descending order.
        return self._listP

    def getCountriesByArea(self, continent = ""):
        self._listA = []
        for i in range(len(self._countryCat)):
            self._tup = self._countryCat[i].getName(), self._countryCat[i].getArea()  # create a tuple with name and population.
            if continent == self._countryCat[i].getContinent():
                self._listA.append(self._tup)
            elif continent == "":  # if continent is default value, add each the country to the list.
                self._listA.append(self._tup)
        self._listA.sort(key = lambda tup: tup[1], reverse = True)  # sort the list with descending order.
        return self._listA

    def findMostPopulousContinent(self):
        self._popcontinent = {}
        for i in range(len(self._countryCat)):
            if self._countryCat[i].getContinent() not in self._popcontinent.keys():  # to check if continent is already in the key of the dictionary.
                self._popcontinent[self._countryCat[i].getContinent()] = self._countryCat[i].getPopulation()  # if not, add it in the dictionary.
            else:
                for key in self._popcontinent:
                    if self._countryCat[i].getContinent() == key:
                        self._popcontinent[key] += self._countryCat[i].getPopulation()  # add values to the existing key that is same as the given key.
        self._maxcont = max(self._popcontinent, key=self._popcontinent.get)  # find the key possesses the largest population.
        self._maxpop = max(self._popcontinent.values())  # find the larget population.
        self._tup = self._maxcont, self._maxpop
        return self._tup  # return a tuple

    def filterCountriesByPopDensity(self, lower, upper):
        self._densitylist = []
        for i in range(len(self._countryCat)):
            self._density = float("%.2f" % (self._countryCat[i].getPopulation()/self._countryCat[i].getArea()))
            self._tup = self._countryCat[i].getName(), self._density
            if lower <= self._density <= upper:  # if density falls in the range, add tuple to the list.
                self._densitylist.append(self._tup)
        self._densitylist.sort(key = lambda tup: tup[1], reverse = True)  # sort with descending order.
        return self._densitylist

    def saveCountryCatalogue(self, catalogue):
        self._catalogue = open(catalogue, "w")
        self._listD = CountryCatalogue.filterCountriesByPopDensity(self, 0, 10000000)  # add all the countries in the list.
        self._catalogue.write("Name|Continent|Population|AreaSize|PopulationDensity")  # write the header.
        for i in range(len(self._countryCat)):
            self._name = str(self._countryCat[i].getName())
            self._cont = str(self._countryCat[i].getContinent())
            self._pop = str(self._countryCat[i].getPopulation())
            self._area = str(self._countryCat[i].getArea())
            self._catalogue.write(self._name + "|" + self._cont + "|" + self._pop + "|" + "%.2f" % (self._area) + "|" + str(self._listD[i]) + "\n")
        self._catalogue.close()
        return self._countryCat.count(self._name) + 1  # retrn the number of items written.
