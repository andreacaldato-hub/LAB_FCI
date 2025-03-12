import requests
from matplotlib import pyplot as plt

n_richeste = 20
sito = "http://www.polimi.it"
Lista_tempo = []
for i in range(n_richeste):
    r = requests.get(sito)
    tempo = r.elapsed.microseconds / 1000
    Lista_tempo.append(tempo)
# print(r.content[:500])  # Prints only the first 500 bytesrint(r.content)
min = min(Lista_tempo)
max = max(Lista_tempo)
medio = sum(Lista_tempo) / len(Lista_tempo)
print(f"Min: {min} ms \nMax: {max} ms\nMedio: {medio} ms")

plt.figure()
plt.title("Tempi di risposta", size=30)
plt.xlabel("Id Richiesta", size=25)
plt.ylabel("Tempo(ms)", size=25)
plt.axhline(min, color="#C45A5A", label="min")
plt.axhline(max, color="#E3A01F", label="max")
plt.axhline(medio, color="#219D8C", label="medio")
plt.grid()
plt.plot(Lista_tempo)
plt.ylim([min, max])
plt.show()
plt.legend(loc=1, fontsize=25)
