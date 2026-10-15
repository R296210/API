import requests

url = "https://api.open-meteo.com/v1/forecast"

parametros={
    "latitude": 19.4326,
    "longitude": -99.1332,
    "current": "temperature_2m"
}

respuesta= requests.get(url, params=parametros)

print(respuesta.status_code)
datos = respuesta.json() 
print(datos)


print(datos["current"]["temperature_2m"])