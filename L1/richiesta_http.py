# importo la libreria richieste http
import requests

# Effetto richista GET
r = requests.get("http://google.com")
print(type(r))
