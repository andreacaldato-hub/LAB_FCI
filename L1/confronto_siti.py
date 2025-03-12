from numpy._core.fromnumeric import size
import requests
from matplotlib import pyplot as plt

# Effetto richista GEjjjT
n_richeste = 10
sito = [
    "http://google.com",
    "http://www.amazon.com",
    "http://www.pornhub.com",
    "http://www.youtube.com",
    "http://www.snai.com",
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
