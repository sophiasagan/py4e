# Extracting Data from JSON
#
# - prompt for a URL
# - read the JSON data from that URL using urllib
# - parse and extract the comment counts from the JSON data
# - compute the sum of the numbers in the file
#
# Sample data: http://py4e-data.dr-chuck.net/comments_42.json (Sum=2553)
# Actual data: http://py4e-data.dr-chuck.net/comments_42030.json (Sum ends with 66)
#
# The data consists of a number of names and comment counts in JSON as follows:
# {
#   comments: [
#     {
#       name: "Matthias"
#       count: 97
#     },
#     {
#       name: "Geomer"
#       count: 97
#     }
#     ...
#   ]
# }
#
# Example: json2.py
# Sample Execution
#
# $ python3 solution.py
# Enter location: http://py4e-data.dr-chuck.net/comments_42.json
# Retrieving http://py4e-data.dr-chuck.net/comments_42.json
# Retrieved 2733 characters
# Count: 50
# Sum: 2...

import urllib.request, urllib.parse, urllib.error
import json

url_handle = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_83062e.json')
the_url_content = url_handle.read().decode()
the_content = json.loads(the_url_content)

sum_new_items = 0

for an_item in the_content['comments'] :
    new_item = int(an_item['count'])
    sum_new_items = sum_new_items + new_item
print(sum_new_items)

#
#
# for an_item in the_content['comments'] :
#     # print(an_item['name'], an_item['count'])
#     new_item = int(an_item['count'])
#     sum_new_items = sum_new_items + new_item
# print(sum_new_items)
