import os
import json
import requests

TOKEN = os.environ.get('access_token')

FILE_PATH = '_data/projects.json'

endpoint = "https://api.github.com/graphql"
headers = {
    "Authorization": f"Bearer {TOKEN}"
}
query = """
  {
    viewer {
      login,
      repositories(
        first: 20,
        orderBy: {
          field: CREATED_AT,
          direction: DESC
        }
      ) {
        nodes {
          name,
          createdAt,
          description,
          url,
          primaryLanguage {
            name,
            color
          },
          owner {
            login
          }
        }
      }
    }
  }
"""

req = requests.post(
    endpoint,
    json={
        'query': query
    },
    headers=headers
)


if req.status_code == 200:
    login = req.json().get('data', {}).get('viewer', {}).get('login')
    repositories = req.json().get('data', {}).get('viewer', {}).get('repositories', {}).get('nodes', [])
    repositories = [repo for repo in repositories if repo.get('owner', {}).get('login') == login]
    for repo in repositories:
        repo.pop('owner', None)

    os.makedirs(os.path.dirname(FILE_PATH), exist_ok=True)
    with open(FILE_PATH, 'w', encoding='utf-8') as projects_file:
        json.dump(repositories, projects_file, ensure_ascii=False, indent=2)
else:
    raise Exception("Exception: Github API Query. status code: {code}, response: {response}".format(
        code=req.status_code,
        response=req.json()
    ))
