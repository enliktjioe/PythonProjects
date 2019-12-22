import wget

# print('Beginning file download with wget module')
#
# url = 'http://raw.githubusercontent.com/datasets/geo-countries/master/data/countries.geojson'
# wget.download(url, 'countries.geojson')



import geojson
with open('countries.geojson') as f:
    gj = geojson.load(f)
features = gj['features'][0]

