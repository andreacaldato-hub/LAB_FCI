import requests

# Effetto richista GEjjjT
n_richeste = 20
sito = "http://google.com"
risorse = []
for i in range(n_richeste):
    r = requests.get(sito)
    tempo = r.elapsed.microseconds / 1000
    print(f"Tempo di risposta: {tempo} ms")
# print(r.content[:500])  # Prints only the first 500 bytesrint(r.content)
