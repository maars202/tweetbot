# tweetbot
Bot that scrapes tweets from twitter and performs sentiment analysis over time. It uses a class built from Selenium. Some of the challenges faced were making the class flexible for users with slower browsers that require longer waiting/ sleep time for the class to work. The tweets fetched are limited since sometimes tweets older than 2 days cannot be retrieved using twitter search engine and require an advanced search. Thus future editions will have scraping features using the advanced search engine for a period of time. 

To install relevant packages with pip:
```bash
pip install -r requirements.txt
```
to run example file, /tweetbot/example.py, 
1. download chrome driver from 
2. edit username, password and path to your downloaded chrome driver in /tweetbot/example.py file
3. 
```bash
python3 ./tweetbot/example.py
```

Relevant files for reference:
1. /tweetbot/example.py includes an example of file to use SeleniumClient for scrapping AI related tweets
2. /tweetbot/AI_100_sentiments.csv is an example of 100 tweets scraped using SeleniumClient class with the query string "AI"




package available on testpypi as well and can be installed directly on your computer using
```bash 
pip install -i https://test.pypi.org/simple/ tweetbot
```
Do remember to install selenium and pandas before running the below code to test it out:

to install selenium and pandas:
```bash
pip install selenium pandas
```
to test out tweetbot package, put this in python file:
```python
from tweetbot import SeleniumCli
username = "twitter_username"
password = "twitter_password"
path ="/path/to/chromedriver" # do remember to edit the path if it's in a different place
sel = SeleniumCli.SeleniumClient(path, 4)

d = sel.login(username, password)

query = "environment"
number_of_posts = 50
df = sel.keep_searching(query, number_of_posts)
print(df)

df.to_csv("example.csv")
```
