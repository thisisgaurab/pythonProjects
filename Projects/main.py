import requests

API_KEY = open('API_KEY').read()
Search_Engine_ID = open('Search_Engine_ID').read()

search_query = 'Cristiano Ronaldo'

url = 'https://www.googleapis.com/customsearch/v1'
params = {
    'q' : search_query,
    'key': API_KEY,
    'cx' : Search_Engine_ID

    #if we want only pdf
    #'fileType' : 'pdf'

    #for image
    #'searchType': 'image'
}

response = requests.get(url, params = params)
results = response.json()
print(results)

if 'items' in results:
  print(results['items'][0]['link'])
