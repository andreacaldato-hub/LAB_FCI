import requests
from matplotlib import pyplot as plt

n_richeste = 20
sito = "http://www.polimi.it"
tempi = []
for i in range(n_richeste):
    r = requests.get(sito)
    tempo = r.elapsed.microseconds / 1000
    tempi.append(tempo)
# print(r.content[:500])  # Prints only the first 500 bytesrint(r.content)
min = min(tempi)
max = max(tempi)
medio = sum(tempi) / len(tempi)
print(f"Min: {min} ms \nMax: {max} ms\nMedio: {medio} ms")

plt.figure()
plt.title("Tempi di risposta", size=30)
plt.xlabel("Id Richiesta", size=25)
plt.ylabel("Tempo(ms)", size=25)
plt.axhline(min, color="#C45A5A", label="min")
plt.axhline(max, color="#E3A01F", label="max")
plt.axhline(medio, color="#219D8C", label="medio")
plt.grid()
plt.plot(tempi, label=sito)
plt.plot(tempi, label=medio)
plt.ylim([min, max])
plt.show()
plt.legend(loc=1, fontsize=25)
