import wget

print('Beginning file download with wget module')

url = 'http://i3.ytimg.com/vi/J---aiyznGQ/mqdefault.jpg'
url2 = 'http://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
# wget.download(url, '/Users/enlik/Downloads/cat4.jpg')
wget.download(url2, '/Users/enlik/Downloads/countries.geojson')

