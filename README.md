# Objectively Funny

This project was made by 4 Le Wagon Data Science students as our final project.
We have sourced and processed a wide range of stand-up scripts to analyse comedians and make our own comedy.

## Description

* Constructed a scraper to source and clean 3.6 million words of stand-up comedy from a variety of online sources using BeautifulSoup, Requests, and Pandas.
* Carried out a machine learning analysis using a Latent Dirichlet Allocation (LDA) on the processed dataset and used wordclouds to visualise results.
* Finetuned a bot using GPT2 ([gpt-2-simple](https://github.com/minimaxir/gpt-2-simple), credit: Max Woolf) & generted entirely original stand-up comedy material from only a few words of text input. Created an API for the bot using FastAPI, Docker and Google Cloud Run.
* Integrated and published the completed project on a public site using Heroku and Streamlit.

## Link to Application

[Heroku/Streamlit App](https://objectively-funny.herokuapp.com/)

## Data

### Sources
* [Scraps From the Loft](http://scrapsfromtheloft.com/stand-up-comedy-scripts/) - Scripts and Year
* [Subsaga](https://subsaga.com/bbc/browse/genre/comedy/standup/?page=0) - Scripts
* [TMDB - The Movie Database](https://www.themoviedb.org/?language=en-GB) - Artist Age and Gender

### Data At a Glance
* 555 individual transcripts
* 268 comedians
* 19 million characters
* 3.6 million words

## Tech Stack

* Python
* Jupyter Notebook
* Requests + BeatuifulSoup
* Pandas
* NLTK
* Gensim
* GPT-2
* Docker
* Google Cloud AI Platform
* Google Cloud Run
* Heroku
* Streamlit

Full list of python packages can be found in the requirements.txt file.


## Authors

* Reinis Melbardis [@rmelbardis](https://github.com/rmelbardis)
* Yuqing Wang [@yuqingwang98](https://github.com/yuqingwang98)
* James Farrell [@jfazz9](https://github.com/jfazz9)
* Catriona Beamish [@beamishc](https://github.com/beamishc)

## Version History

* 0.1
    * Initial Release

## Acknowledgments

* [Le Wagon Data Science Course, London](https://www.lewagon.com/london/data-science-course/full-time)
