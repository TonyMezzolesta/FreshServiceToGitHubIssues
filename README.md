# Fresh Service To GitHub Issues
Python script that gets tickets from Fresh Service based on query and puts them into GitHub Issues


## Flow
### 1. Grab the tickets from Fresh service.
The current script is using a "query" to grab the open tickets from Fresh Service.  It also looks by a specific group within our organization.
Make sure to change the query string to get desired results.

```
# specific for searching fresh service tickets, this one grabs by a specific group and the status is open
query = r'"group_id:4000271714%20AND%20(status:2)"'
```

Make sure to change the URL based on your company.

```
urlSearch = "https://<yourcompany>.freshservice.com/api/v2/search/tickets?query=" + query
```

Make sure to input your token.

```
'Authorization': "Basic <yourtoken>",
```

**Note: Had to put the query in the URL string instead of the parameters due to unicode issues.

### 2. Loop through tickets and write them into GitHub.
This will grab all of the tickets written into the data object from the results of the Fresh Service API call and perform a POST on your GitHub repo issues board.
Make sure to change URL to point to your personal/organization repo.

```
urlGit = "https://api.github.com/repos/<yourcompany>/<yourrepo>/issues"
```

Make sure to input your token.

```
'Authorization': "Basic <yourtoken>",
```

The data object will be POSTed into the GitHub issues and create a new issue.  You can alter the object and add data as needed based on the GitHub API documentation.  I kept it pretty minimal.

### 3. Update Ticket Status
Update the ticket status to prevent duplicate issues.
A fresh service ticket object is filled in and used to update the ticket.
I am using a status of 8, which is a custom status created in Fresh Service.

Make sure to change the URL

```
urlUpdate = "https://<yourcompany>.freshservice.com/api/v2/tickets/" + str(ticket['id'])
````


## Documentation
[Fresh Service/Service Desk API v2](https://api.freshservice.com/v2/)

[GitHub API v3](https://developer.github.com/v3/)
