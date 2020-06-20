import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET

url_handle = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_83061.xml')
the_url_content = url_handle.read().decode().strip()
# all_comments = ET.fromstring(the_url_content).findall('comments/comment')
all_comments = ET.fromstring(the_url_content).findall('.//count')

how_many = 0
sum_of_contents = 0

for item in all_comments :
    # a_new_value = item.find('count').text
    a_new_value = item.text
    sum_of_contents = sum_of_contents + int(a_new_value)
    how_many += 1

print(how_many)
print(sum_of_contents)
