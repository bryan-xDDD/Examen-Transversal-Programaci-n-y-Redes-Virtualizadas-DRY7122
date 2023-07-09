import requests

def obtener_distancia(ciudad_origen, ciudad_destino):
    api_key = '64yybEcLkNn3k3P4mMtZgqz6Z72J2f7w'  # Reemplaza con tu propia API key de MapQuest
    url = f'http://www.mapquestapi.com/directions/v2/route?key={api_key}&from={ciudad_origen}&to={ciudad_destino}'
    response = requests.get(url)
    data = response.json()
    if data['info']['statuscode'] != 0:
        print('No se pudo obtener la distancia entre las ciudades.')
        return None
    distancia_kms = data['route']['distance'] * 1.60934  # Convertir millas a kilómetros
    return distancia_kms

def calcular_duracion(distancia_kms, velocidad_promedio=80):
    tiempo_horas = distancia_kms / velocidad_promedio
    tiempo_minutos = tiempo_horas * 60
    tiempo_segundos = tiempo_minutos * 60
    return tiempo_horas, tiempo_minutos, tiempo_segundos

def calcular_combustible(distancia_kms, consumo_litros_km=0.12):
    combustible_litros = distancia_kms * consumo_litros_km
    return combustible_litros

# Solicitar ciudades de origen y destino al usuario
ciudad_origen = input("Ciudad de Origen: ")
ciudad_destino = input("Ciudad de Destino: ")

# Obtener la distancia entre las ciudades
distancia_kms = obtener_distancia(ciudad_origen, ciudad_destino)
if distancia_kms is None:
    exit()

# Calcular la duración del viaje
tiempo_horas, tiempo_minutos, tiempo_segundos = calcular_duracion(distancia_kms)

# Calcular el combustible requerido
combustible_litros = calcular_combustible(distancia_kms)

# Imprimir los resultados
print("Distancia:", round(distancia_kms, 1), "kms")
print("Duración:", round(tiempo_horas, 1), "horas,", round(tiempo_minutos, 1), "minutos,", round(tiempo_segundos, 1), "segundos")
print("Combustible requerido:", round(combustible_litros, 1), "litros")
