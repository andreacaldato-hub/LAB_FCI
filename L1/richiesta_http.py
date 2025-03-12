# importo la libreria richieste http
import requests

# Effetto richista GEjjjT
n_richeste = 10
sito = "http://wikipedia.org"
for i in range(n_richeste):
    r = requests.get(sito)
    tempo = r.elapsed.microseconds / 1000
    print(f"Tempo di risposta: {tempo} ms")
# print(r.content[:500])  # Prints only the first 500 bytesrint(r.content)
