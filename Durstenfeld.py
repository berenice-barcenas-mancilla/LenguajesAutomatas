from random import randrange

#funcion de utlidad para intercambiar elementos A[i] y A[j] en una lista

def print_itinerary(dictionary,src):
    dest=dictionary.get(src)
    if not dest:
        return
    print(src+'->'+dest)
    print_itinerary(dictionary,dest)
    
    
    #funcion para encontrar el itinerario de la lista dada de aeropuertos de salida y llegada

def findItinerary(tickets):
    #construir un conjunto de aeropuertos de destino
    destinations = {*tickets.values()}
    #considere cada aeropuerto de salida para encontrar el aeropuerto de origen
    for k, v in tickets.items():
        if not destinations:
            #cuando se encuentre en el aeropuerto de origen imprima el itinerario
            print_itinerary(tickets,k)
            return
if __name__=='__main__':
    #entrada # de lista de tickets
    tickets={
        'LAX':'DXB',
        'DFW':'JFK',
        'LHR':'DFW',
        'JFK':'LAX',
    }
    findItinerary(tickets)
