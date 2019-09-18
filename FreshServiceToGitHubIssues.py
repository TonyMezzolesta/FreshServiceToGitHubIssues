# importing the requests library 
import requests
import json

# Create classes
class GitIssue:
  title = ""
  body = ""

class freshTicket:
  status = 3

# specific for searching fresh service tickets, this one grabs by a specific group and the status is open
query = r'"group_id:4000271714%20AND%20(status:2)"'

# Create URL for FreshService, had to add query parameter to url instead of parameter due to encoding issues
urlSearch = "https://<yourcompany>.freshservice.com/api/v2/search/tickets?query=" + query

# querystring = {"query":r"%22group_id:4000271714%20AND%20%28status:3%20OR%20status:4%29%22"}

headers = {
    'Content-Type': "application/json",
    'Authorization': "Basic <yourtoken>",
    'cache-control': "no-cache"
    }

# response = requests.request("GET", url, headers=headers, params=querystring)
response = requests.request("GET", urlSearch, headers=headers)

data = response.json()

# print("data:%s"%(data))

# loop through tickets
for ticket in data['results']:
    # create github issue object
    issue = GitIssue()
    issue.title = str(ticket['subject']) + ' | ticket: ' + str(ticket['id'])
    issue.body = str(ticket['description'])

    urlGit = "https://api.github.com/repos/<yourcompany>/<yourrepo>/issues"

    # payloadGit = "{\r\n  \"title\": \"" + str(issue.title) + "\",\r\n  \"body\": \"" + str(issue.body) + "\",\r\n  \"labels\": [\r\n    \"bug\"\r\n  ]\r\n}"
    headersGit = {
        'Content-Type': "application/json",
        'Authorization': "Bearer <yourtoken>",
        'User-Agent': "PostmanRuntime/7.16.3",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Host': "api.github.com",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "148",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    responseGit = requests.request("POST", urlGit, data=json.dumps(issue.__dict__).encode("utf-8"), headers=headersGit)

    # print(responseGit.text)

    # put response into json format into object
    dataGit = responseGit.json()

    # create fresh service ticket object
    fticket = freshTicket()
    fticket.status = 8

    urlUpdate = "https://<yourcompany>.freshservice.com/api/v2/tickets/" + str(ticket['id'])

    responseSucces = requests.request("PUT", urlUpdate, data=json.dumps(fticket.__dict__).encode("utf-8"), headers=headers)
