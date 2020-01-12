# CorpMap
An interactive global map to display different locations of a corporation and relevant information about each. 

## Introduction
This program is designed to provide internal monitoring and compliance checking across dozens of corporate locations at a company.
It uses Python's Folium library to create interactive maps with embedded JavaScript. Each location is denoted by a marker on the map,
and locations are grouped by region, which can be toggled on/off to focus on a region. 
Each location can be selected by clicking a marker, which then pops up a small window on the map, which includes
date/time, weather, compliance and contact informaiton corresponding the branch.

This project was a great introduction to HTML and organizing and manipulating information using Python at a larger scale.

## Walkthrough
![alt text](https://github.com/coreystone/CorpMap/blob/master/map.png "")

![alt text](https://github.com/coreystone/CorpMap/blob/master/marker.png "")

![alt text](https://github.com/coreystone/CorpMap/blob/master/regions.png "")

## Libraries
* [**Folium**](https://python-visualization.github.io/folium/) to create the map, markers, and interactivity.
* [**PyOWM**](https://pyowm.readthedocs.io/en/latest/) for interacting with the OpenWeatherMap API
* [**PyTz**](http://pytz.sourceforge.net/) for querying TimeZone database
