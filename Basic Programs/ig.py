import requests

user = "iamsrk"
url = 'https://www.instagram.com/' + user
r = requests.get(url).text

start = '"edge_followed_by":{"count":'
end = '},"followed_by_viewer"'
followers=r[r.find(start)+len(start):r.rfind(end)]
print(followers)
