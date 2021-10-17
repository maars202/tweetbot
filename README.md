# tweetbot
Bot that scrapes tweets from twitter and performs sentiment analysis over time.

```bash
run: pip install -r requirements.txt in your shell.
```
to run example file, /tweetbot/example.py, 
1. download chrome driver from 
2. edit username, password and path to your downloaded chrome driver in /tweetbot/example.py file
3. 
```bash
run: python3 ./tweetbot/example.py in your shell.
```

Relevant files for reference:
1. /tweetbot/example.py includes an example of file to use SeleniumClient for scrapping AI related tweets
2. /tweetbot/AI_100_sentiments.csv is an example of 100 tweets scraped using SeleniumClient class with the query string "AI"
