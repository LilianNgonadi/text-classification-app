# Twitter Sentiment Project
<!-- About The Project -->

<a name="readme-top"></a>

<!-- TABLE OF CONTENTS -->


<summary>Table of Contents</summary>
<ol>
  <li><a href="#introduction">Introduction</a></li>
  <li><a href="#dataset">Dataset</a></li>
     <li><a href="#usage">Usage</a></li>
  </li>
</ol>


# Introduction

- In the age of social media, platforms like Twitter have become a significant source of real-time information and public opinion. Understanding the sentiment behind tweets can provide valuable insights into public mood, opinions on various topics, and reactions to events. 

- This project  aims to leverage machine learning techniques to classify the sentiment of tweets into categories such as positive, negative, neutral, or irrelevant. By utilizing two datasets—one for training and one for validation—we aim to build a robust sentiment analysis model capable of accurately interpreting the sentiment expressed in tweets.


# Dataset

The [Twitter dataset](https://www.kaggle.com/datasets/markmedhat/twitter) used in this project contain tweets related to specific keywords, along with their corresponding sentiment labels. The training dataset includes over 74,000 entries, while the validation dataset contains nearly 1,000 entries. Each entry comprises an identifier, a keyword, a sentiment label, and the tweet text. These datasets provide a comprehensive basis for training and evaluating sentiment analysis models

## Training Dataset (twitter_training.csv)
The training dataset contains 74,681 entries and 4 columns:
* ID (2401): Identifier for the tweets.
* Keyword (Borderlands): Keyword or category for the tweets.
* Sentiment (Positive): Sentiment label of the tweets.
* Tweet Text: The actual text of the tweets.
  
## Validation Dataset (twitter_validation.csv)
The validation dataset contains 999 entries and 4 columns:
* ID (3364): Identifier for the tweets.
* Keyword (Facebook): Keyword or category for the tweets.
* Sentiment (Irrelevant): Sentiment label of the tweets.
* Tweet Text: The actual text of the tweets.

# Usage
These [Twitter dataset](https://www.kaggle.com/datasets/markmedhat/twitter) is gotten from Kaggle and can be used for training and evaluating sentiment analysis models. Each entry includes a tweet and its associated sentiment label, which can be used to classify the sentiment of new tweets.
