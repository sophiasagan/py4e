# Calling a JSON API
#
# The program will:
# prompt for a location
# contact a web service
# retrieve JSON for the web service
# parse that data
# retrieve the first place_id from the JSON.
#
# (A place ID is a textual identifier that uniquely
# identifies a place as within Google Maps.)
#
# Use this API endpoint (static subset of the Google Data):
# http://py4e-data.dr-chuck.net/geojson?
#
# This API uses the same parameter (address) as the Google API. This API also
# has no rate limit so you can test as often as you like. If you visit the
# URL with no parameters, you get a list of all of the address values which
# can be used with this API.
#
# To call the API, you need to provide address that you are requesting as
# the address= parameter that is properly URL encoded using the
# urllib.urlencode() fuction as shown in http://www.py4e.com/code3/geojson.py
#
# Test Data / Sample Execution
#
# You can test to see if your program is working with a location
# of "South Federal University" which will have a place_id
# of "ChIJJ8oO7_B_bIcR2AlhC8nKlok".
#
# $ python3 solution.py
# Enter location: South Federal University
# Retrieving http://...
# Retrieved 2101 characters
# Place id ChIJJ8oO7_B_bIcR2AlhC8nKlok
#
# Please run your program to find the place_id for this location:
# University of Evora
#
# The first seven characters of the place_id should be: "ChIJw3_ ..."

# PLAN:
# import libraries (urllib and json)
# define the api endpoint
# capture user input
# parse the user input into something urllib can read and combine with endpoint
# request the content, decode it, read it
# parse it with json into a list
# extract the place id from the list - it's in: results/place_id

import urllib.request, urllib.parse, urllib.error
import json

api_endpoint = 'http://py4e-data.dr-chuck.net/geojson?'
requested_location = input('Requested Location? ')
the_full_url = api_endpoint + urllib.parse.urlencode( {'address': requested_location} )
the_url_content = urllib.request.urlopen(the_full_url).read().decode()
the_content = json.loads(the_url_content)

for a_node in the_content['results'] :
    print(a_node['place_id'])


#
#
