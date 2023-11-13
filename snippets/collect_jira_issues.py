import requests


jira_api_base_url = "https://issues.apache.org/jira/"
page_length = 500
project = "hadoop"
proj_jira_id = project.upper()
start_idx = 0
url = (
    jira_api_base_url
    + f"rest/api/2/search?jql=project={proj_jira_id}+order+by+created"
    + f"&issuetypeNames=Bug&maxResults={page_length}&"
    + f"startAt={start_idx}&fields=id,key,priority,labels,versions,"
    + "status,components,creator,reporter,issuetype,description,"
    + "summary,resolutiondate,created,updated"
)
print(f"Getting data from {url}...")
r = requests.get(url)
r_dict = r.json()
