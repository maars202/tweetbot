
from SeleniumCli import SeleniumClient

username = "your_twitter_username"
password = "your_twitter_password"
path ="/Users/maarunipandithurai/Desktop/maars202/selen_pro/chromedriver" # do remember to edit the path if it's in a different place
# set to 4 seconds waiting period before username and password inputs:
sel = SeleniumClient(path, 4)

d = sel.login(username, password)

query = "AI blockchain"
number_of_posts = 10
df = sel.keep_searching(query, number_of_posts)
print(df)
