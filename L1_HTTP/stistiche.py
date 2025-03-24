import requests

# Effetto richista GEjjjT
n_richeste = 10
sito = "http://www.tiktok.com"
Lista_tempo = []
for i in range(n_richeste):
    r = requests.get(sito)
    tempo = r.elapsed.microseconds / 1000
    Lista_tempo.append(tempo)
# print(r.content[:500])  # Prints only the first 500 bytesrint(r.content)
print(f"Lista_tempo: {Lista_tempo}")
min = min(Lista_tempo)
max = max(Lista_tempo)
medio = sum(Lista_tempo) / len(Lista_tempo)
print(f"Min: {min} ms \nMax: {max} ms\nMedio: {medio} ms")
