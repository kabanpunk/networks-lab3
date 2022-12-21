import os

conf = {
    'GRAPHHOPPER_API_KEY':  os.environ['GRAPHHOPPER_API_KEY'],
    'GRAPHHOPPER_API_URL': 'https://graphhopper.com/api/1/geocode',
    'OPENWEATHERMAP_API_KEY': os.environ['OPENWEATHERMAP_API_KEY'],
    'OPENWEATHERMAP_API_URL': 'https://api.openweathermap.org/data/2.5/',
}