import requests
from matplotlib import pyplot as plt

# Effetto richista GEjjjT
n_richeste = 10
sito = [
    "http://www.wikipedia.org",
    "http://www.siti.org",
    "http://www.sitinazionale.org",
    "http://www.irs.gov",
]
plt.figure()
for sito in sito:
    tempi = []
    for _ in range(n_richeste):
        r = requests.get(sito)
        tempo = r.elapsed.microseconds / 1000
        tempi.append(tempo)
    Min = min(tempi)
    # print(f"Tempo minimo per {sito}: {Min}")
    plt.plot(tempi, label=sito)  # 🔥 Increase line thickness
plt.xlabel("Id richiesta", size=25)
plt.ylabel("Tempo(ms)", size=25)
plt.grid()
plt.legend(loc=1, fontsize=10)
plt.show()
