class City():

    def __init__(self, name:str, sld:int):
        self.name = name
        self.SLD = sld
        self.f = 0
        self.h = sld
        self.g = 0
        self.distance = []
        self.numconnections = 0
        self.nextcity = []

    def distance(self, city):
        rv = -1
        for i,c in enumerate(self.nextcity):
            if(c.name == city.name):
                return(self.distance[i])
        return rv

    def addconnection(self, city, dist):
        self.numconnections+=1
        self.distance.append(dist)
        self.nextcity.append(city)

    def getSLD(self):
        return self.SLD

    def getcity(self, index):
        return self.nextcity[index]

    def getdist(self, index):
        return self.distance[index]

    def getname(self):
        return self.name