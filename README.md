# GDD Training Taster Sessions

## Introduction

This repository contains all notebooks and materials for each GDD Training Taster.

## Running a taster session

If you need to use one of these tasters, clone the repository and switch to the correct branch (see below).

If you are creating a new course, please add it as a new branch to this repo and add it to the list below. 

## Session Info

Each taster is run for our public courses. To access the material for the course you can go to the branch corresponding to the taster. Here is a breakdown of the branch names:

|Branch Name|Taster Name|Timing|Description|
|---|---|---|---|
|pfda|Python for Data Analysts|2 hr|Public: Covers Python Essentials and Pandas with some visualisations to demonstrate the power of Python|
|dswp|Data Science with Python| 2hr |Public: An introduction to Machine Learning followed by a demo of using sci-kit learn on the penguins dataset|
|adwsp|Advanced Data Science with Python| 2hr |Public: An introduction to all topics covered in the ADWSP course followed by demo of feature engineering|
|anomaly-detection-in-time-series|Anomaly Detection in Time Series| 2hr | Public data science taster |
|deep-learning| Deep Learning | 1hr | Public deep learning webinar |
|seasonality-modelling|Seasonality Modeling from Scratch|2.5hrs|PyData AMS Code Breakfast - https://youtu.be/omEVdUS14SU|
|neural-network-vulnerabilities|Vulnerabilities of Neural Networks: Find, Defend, & Prevent | 2.5hrs | Vadim Nelidov | PyData AMS Code Breakfast | 

## Contributing

To add a new taster you can use the `taster-template` branch and add all the notebooks/files you need. Feel free to remove folders that aren't necessary.

### Using Binder

Each course can correspond to a Binder link (redirected with rebrandley) to allow participants to use jupyter notebooks during the training.

To create a binder link for a taster, first create a `requirements.txt` file with all the packages needed for the taster. Then visit [Binder](https://mybinder.org/), paste the URL of this repo and include the name of the branch when creating:

![](images/binder.png)

## Contacts

Please reach out to the data science training team - Lucy Sheppard, James Hayward, Marysia Winkels, Hertbert van Leeuwen - if you have any questions.
