# CorpMap
An interactive global map to display different locations of a corporation and relevant information about each. 

## Introduction
This program is designed to provide internal monitoring and compliance checking across dozens of corporate locations at a company.
It uses Python's Folium library to create interactive maps with embedded JavaScript. Each location is denoted by a marker on the map,
and locations are grouped by region, which can be toggled on/off to focus on a region. 
Each location can be selected by clicking a marker, which then pops up a small window on the map, which includes
date/time, weather, compliance and contact informaiton corresponding the branch.

This project was a great introduction to HTML and organizing and manipulating information using Python at a larger scale.

## Demo
var map_3f1e88876c28404ebe016265acb234f0 = L.map( "map_3f1e88876c28404ebe016265acb234f0", { center: [45.372, -121.6972], crs: L.CRS.EPSG3857, maxBounds: [[-190, -50], [190, 75]], zoom: 3, zoomControl: true, preferCanvas: false, } ); var tile_layer_761d9851b2964eb5a81c990cfc24f15e = L.tileLayer( "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap

## Libraries
* [**Folium**](https://python-visualization.github.io/folium/) to create the map, markers, and interactivity.
* [**PyOWM**](https://pyowm.readthedocs.io/en/latest/) for interacting with the OpenWeatherMap API
* [**PyTz**](http://pytz.sourceforge.net/) for querying TimeZone database
