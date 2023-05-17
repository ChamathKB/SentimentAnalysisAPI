# Sentiment Analysis API

[![Build Status](https://app.travis-ci.com/ChamathKB/SentimentAnalysisAPI.svg?branch=master)](https://app.travis-ci.com/ChamathKB/SentimentAnalysisAPI)

An API for sentiment analysis using machine learning.

Dataset used --> [Kaggle](https://www.kaggle.com/c/sentiment-analysis-on-movie-reviews/data)


## Deploy API

### Local
```
python app.py
```

### Heroku
1. Create heroku app
    ```
    heroku create sentimentanalyzer
    ```
2. Push

    from main branch
    ```
    git push heroku master
    ```
    or if from different branch
    ```
    git push heroku heroku_deploy:master
    ```
## User Requests example
```
curl -X GET http://127.0.0.1:5000/ -d query='that movie was boring'
```
