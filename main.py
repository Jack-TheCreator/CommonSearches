print('hello')

class City:
    def __init__(self, name):
        self.name = name
        self.numConnections = 0
        self.childCities = []

    def addconnection(self, City, distance):
        self.childCities.append(City)

class Map:
    def __init__(self):
        self.initCities()
        self.addConnections()

    def initCities(self):
        self.Oradea = City("Oradea")
        self.Zerind = City("Zerind")
        self.Arad = City("Arad")
        self.Timisoara = City("Timisoara")
        self.Lugoj = City("Lugoj")
        self.Mehadia = City("Mehadia")
        self.Drobeta = City("Drobeta")
        self.Craiova = City("Craiova")
        self.Rimnicu = City("Rimnicu")
        self.Sibiu = City("Sibiu")
        self.Pitesi = City("Pitesi")
        self.Fagaras = City("Fagaras")
        self.Bucharest = City("Bucharest")
        self.Giurgiu = City("Giurgiu")
        self.Hirsova = City("Hirsova")
        self.Eforie = City("Eforie")
        self.Urziceni = City("Urziceni")
        self.Vaslui = City("Vaslui")
        self.Iasi = City("Iasi")
        self.Neamt = City("Neamt")

    def addConnections(self):
        self.Oradea.addconnection(self.Zerind, 71)
        self.Oradea.addconnection(self.Sibiu, 151)
        self.Zerind.addconnection(self.Oradea, 71)
        self.Zerind.addconnection(self.Arad, 75)
        self.Arad.addconnection(self.Sibiu, 140)
        self.Arad.addconnection(self.Zerind, 75)
        self.Arad.addconnection(self.Timisoara, 118)
        self.Timisoara.addconnection(self.Arad, 118)
        self.Timisoara.addconnection(self.Lugoj, 111)
        self.Lugoj.addconnection(self.Timisoara, 111)
        self.Lugoj.addconnection(self.Mehadia, 70)
        self.Mehadia.addconnection(self.Drobeta, 75)
        self.Mehadia.addconnection(self.Lugoj, 70)
        self.Drobeta.addconnection(self.Mehadia, 75)
        self.Drobeta.addconnection(self.Craiova, 120)
        self.Craiova.addconnection(self.Drobeta, 120)
        self.Craiova.addconnection(self.Rimnicu, 146)
        self.Craiova.addconnection(self.Pitesi, 120)
        self.Rimnicu.addconnection(self.Craiova, 146)
        self.Rimnicu.addconnection(self.Sibiu, 80)
        self.Rimnicu.addconnection(self.Pitesi, 97)
        self.Sibiu.addconnection(self.Arad, 140)
        self.Sibiu.addconnection(self.Oradea, 151)
        self.Sibiu.addconnection(self.Fagaras, 99)
        self.Sibiu.addconnection(self.Rimnicu, 80)
        self.Pitesi.addconnection(self.Craiova, 120)
        self.Pitesi.addconnection(self.Rimnicu, 97)
        self.Pitesi.addconnection(self.Bucharest, 101)
        self.Fagaras.addconnection(self.Sibiu, 99)
        self.Fagaras.addconnection(self.Bucharest, 211)
        self.Bucharest.addconnection(self.Fagaras, 211)
        self.Bucharest.addconnection(self.Pitesi, 101)
        self.Bucharest.addconnection(self.Giurgiu, 90)
        self.Bucharest.addconnection(self.Urziceni, 85)
        self.Giurgiu.addconnection(self.Bucharest, 90)
        self.Urziceni.addconnection(self.Hirsova, 98)
        self.Urziceni.addconnection(self.Bucharest, 85)
        self.Urziceni.addconnection(self.Vaslui, 142)
        self.Hirsova.addconnection(self.Eforie, 86)
        self.Hirsova.addconnection(self.Urziceni, 98)
        self.Eforie.addconnection(self.Hirsova, 86)
        self.Vaslui.addconnection(self.Urziceni, 142)
        self.Vaslui.addconnection(self.Iasi, 92)
        self.Iasi.addconnection(self.Vaslui, 92)
        self.Iasi.addconnection(self.Neamt, 87)
        self.Neamt.addconnection(self.Iasi, 87)

    def DFS(self) -> list:
        path = []
        self._DFS(self.Arad, path)
        return path

    #DFS recursive helper
    def _DFS(self, currentCity:City, path:list):
        path.append(currentCity)
        if(currentCity == self.Bucharest):
            #stops the recurison
            return True
        for child in currentCity.childCities:
            #Stops path circling
            if(child not in path):
                found = self._DFS(child, path)
                if(found):
                    return True
        #return False because bucharest hasn't been found
        return False

    def BFS(self):
        #toVisit is being used as a queue
        toVisit = []
        toVisit.append(self.Arad)
        path = self._BFS(toVisit)
        return path

    def _BFS(self,toVisit:list):
        path = []
        while(len(toVisit)>0):
            city = toVisit.pop()
            path.append(city)
            if(city == self.Bucharest):
                return path
            for child in city.childCities:
                if((child not in toVisit) and (child not in path)):
                    toVisit.insert(0, child)

        return False

    def IDS(self):
        path = []
        limit = 0
        found = False
        while(not found):
            #subpath used to get tracking of overall path when increment depthlimit
            subpath = []
            found, subpath = self.DLS(self.Arad, limit, subpath)
            path.extend(subpath)
            limit += 1

        return path

    def DLS(self, currentCity, limit, subpath):
        subpath.append(currentCity)
        if(currentCity == self.Bucharest):
            return True, subpath
        if(limit == 0):
            return False, subpath
        for child in currentCity.childCities:
            if(child not in subpath):
                found, subpath = self.DLS(child, limit-1, subpath)
                if(found):
                    return True, subpath


        return False, subpath


    #just used to print city names rather than object mem addresses
    def print(self, path:list):
        for city in path:
            print(city.name)


map = Map()
print("----------DFS PATH------------")
map.print(map.DFS())
print("----------BFS PATH------------")
map.print(map.BFS())
print("----------IDS PATH------------")
map.print(map.IDS())
print("------------------------------")
