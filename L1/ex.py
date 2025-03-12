import requests

n_richeste = 5
sito = [
    "http://google.com",
    "http://youtube.com",
]
medi = []
for sito in sito:
    tempi = []
    for _ in range(n_richeste):
        r = requests.get(sito)
        tempo = r.elapsed.microseconds / 1000
        tempi.append(tempo)
    medio = sum(tempi) / len(tempi)
    print(f"Tempo medio per {sito}: {medio} ms")
    medi.append(medio)
print(f"Tempo medio migliore {min(medi)}")
