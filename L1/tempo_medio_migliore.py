import requests

n_richeste = 5

sito = {
    "https://example.com": None,
    "https://google.com": None,
    "https://github.com": None,
}

for url in sito:
    tempi = []
    for _ in range(n_richeste):
        r = requests.get(url)
        tempo = r.elapsed.microseconds / 1000
        tempi.append(tempo)

    medio = sum(tempi) / len(tempi)
    print(f"Tempo medio per {url}: {medio:.2f} ms")
    sito[url] = medio

min_tempo = min(sito.values())
best_url = min(sito, key=sito.get)

print(f"Tempo medio migliore: {min_tempo:.2f} ms ({best_url})")
