import requests
from time import sleep
nom="salut ca va"
response = requests.get("http://193.48.125.177/etrs403/projet_td/sql/test_pico.php?test="+nom) # Remplacer URL 193.48.125.177*/
response_code = response.status_code
response_content = response.content
print('Response code: ', response_code)
print('Response content:', response_content)
sleep(2)
