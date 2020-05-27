import city
import map

map = map.Map()

def Asearch():
    open = []
    closed = []

    open.append(map.Arad)

    while(len(open)>0):
        lowest = -1
        for i, city in enumerate(open):
            if(lowest==-1):
                lowest = city
                lowestIndex = i

            elif(city.f<lowest.f):
                lowest = city
                lowestIndex = i

        open.pop(lowestIndex)
        print("-------------------")
        print(lowest.name)
        print('-------------------')
        for i, city in enumerate(lowest.nextcity):
            print('looking at', city.name)
            if(city.name == "Bucharest"):
                print("DONE")
                return
            else:
                city.g = lowest.g + lowest.distance[i]
                city.f = city.g + city.h
                print('F:', city.f, "G:", city.g, "H:", city.h)
                skip = False
                for c in open:
                    if(city.f > c.f):
                        skip=True
                for c in closed:
                    if(city.f > c.f):
                        skip = True

                if(skip==False):
                    open.append(city)

        closed.append(lowest)


Asearch()
