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
