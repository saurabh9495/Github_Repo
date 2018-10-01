import requests, json
 
github_url = "https://api.github.com/user/repos"
data = json.dumps({'name':'name_of_your_github_repository', 'description':'about_yout_repository'})
r = requests.post(github_url, data, auth=('your_username_github', 'your_password_github'))

print (r.text)
