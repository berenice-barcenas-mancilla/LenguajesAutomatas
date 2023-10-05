# Función para imprimir el itinerario a partir de una fuente dada src
def print_itinerary(diccionario, src):
    # Obtenemos el destino correspondiente a la fuente
    dest = diccionario.get(src)
    # Si no hay destino, terminamos
    if not dest:
        return

    # Imprimimos la fuente y el destino
    print(src + ' —> ' + dest)
    # Llamamos a la función recursivamente con el destino como nueva fuente
    print_itinerary(diccionario, dest)

# Función para encontrar el itinerario a partir de una lista dada de aeropuertos de salida y llegada
def findItinerary(tickets):

    # Construimos un conjunto de aeropuertos de destino
    destinos = {*tickets.values()}

    # Consideramos cada aeropuerto de salida para encontrar el aeropuerto de origen
    for k, v in tickets.items():
        # El aeropuerto de origen no estará presente en la lista de aeropuertos de destino
        if k not in destinos:
            # Cuando encontramos el aeropuerto de origen, imprimimos el itinerario
            print_itinerary(tickets, k)
            return

if __name__ == '__main__':

    # Entrada: lista de boletos
    tickets = {
        'Constitucion':'Isabel la Catolica',
        'Chabacano':'Neza',
        '4 caminos': 'Puerto Aereo',
        'Puerto Aereo':'Terminal de Autobuses',
        'Pino Suarez':'Zocalo',
        'Terminal de Autobuses':'Pino Suarez',
        'Zocalo':'Chabacano',
        'Neza':'Constitucion'
    }

    # Llamamos a la función para encontrar el itinerario
    findItinerary(tickets)
