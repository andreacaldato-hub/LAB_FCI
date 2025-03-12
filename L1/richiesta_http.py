# importo la libreria richieste http
import requests

# Effetto richista GET
for i in range(10):
    r = requests.get("http://google.com")
    print(f"Tempo di risposta: {r.elapsed.microseconds / 1000} ms")
# print(r.content[:500])  # Prints only the first 500 bytesrint(r.content)
