import requests

n_richeste = 5  # Number of requests per site

# Dictionary with None as initial values
sito = {
    "https://example.com": None,
    "https://google.com": None,
    "https://github.com": None,
}

for url in sito:
    tempi = []
    for _ in range(n_richeste):
        r = requests.get(url)
        tempo = r.elapsed.microseconds / 1000  # Convert microseconds to milliseconds
        tempi.append(tempo)

    medio = sum(tempi) / len(tempi)  # Calculate average response time
    print(f"Tempo medio per {url}: {medio:.2f} ms")
    sito[url] = medio  # Store the average response time

# Find the URL with the best response time
min_tempo = min(sito.values())  # Find the minimum response time
best_url = min(sito, key=sito.get)  # Find the corresponding URL

print(f"Tempo medio migliore: {min_tempo:.2f} ms ({best_url})")
