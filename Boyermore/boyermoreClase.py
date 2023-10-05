def findMajorityElement(nums):
    # Crea un hash map vacío
    d = {}
    
    # Almacena la frecuencia de datos de cada elemento en un diccionario
    for i in nums:
        d[i] = d.get(i, 0) + 1
    
    # Busca el elemento mayoritario
    for key, value in d.items():
        if value > len(nums) / 2:
            return key
    
    # NINGÚN ELEMENTO MAYORITARIO ESTÁ PRESENTE
    return -1

if __name__ == '__main__':
    # Suposición: lista de entrada válida para encontrar el elemento mayoritario
    nums = [1, 8, 7, 4, 1, 2, 2, 2, 2, 2, 2]
    result = findMajorityElement(nums)
    if result != -1:
        print('El elemento mayoritario es', result)
    else:
        print('El elemento mayoritario no existe')
