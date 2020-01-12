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
&lt;!DOCTYPE html&gt;
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8" />
<pre><code>&lt;script&gt;
        L_NO_TOUCH = false;
        L_DISABLE_3D = false;
    &lt;/script&gt;

&lt;script src=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.js&quot;&gt;&lt;/script&gt;
&lt;script src=&quot;https://code.jquery.com/jquery-1.12.4.min.js&quot;&gt;&lt;/script&gt;
&lt;script src=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js&quot;&gt;&lt;/script&gt;
&lt;script src=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js&quot;&gt;&lt;/script&gt;
&lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.css&quot;/&gt;
&lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css&quot;/&gt;
&lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css&quot;/&gt;
&lt;link rel=&quot;stylesheet&quot; href=&quot;https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css&quot;/&gt;
&lt;link rel=&quot;stylesheet&quot; href=&quot;https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css&quot;/&gt;
&lt;link rel=&quot;stylesheet&quot; href=&quot;https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css&quot;/&gt;
&lt;style&gt;html, body {width: 100%;height: 100%;margin: 0;padding: 0;}&lt;/style&gt;
&lt;style&gt;#map {position:absolute;top:0;bottom:0;right:0;left:0;}&lt;/style&gt;

        &lt;meta name=&quot;viewport&quot; content=&quot;width=device-width,
            initial-scale=1.0, maximum-scale=1.0, user-scalable=no&quot; /&gt;
        &lt;style&gt;
            #map_3f1e88876c28404ebe016265acb234f0 {
                position: relative;
                width: 100.0%;
                height: 100.0%;
                left: 0.0%;
                top: 0.0%;
            }
        &lt;/style&gt;
    
&lt;script src=&quot;https://rawcdn.githack.com/ardhi/Leaflet.MousePosition/c32f1c84/src/L.Control.MousePosition.js&quot;&gt;&lt;/script&gt;
&lt;link rel=&quot;stylesheet&quot; href=&quot;https://rawcdn.githack.com/ardhi/Leaflet.MousePosition/c32f1c84/src/L.Control.MousePosition.css&quot;/&gt;</code></pre>
</head>
<body>
<pre><code>    &lt;div class=&quot;folium-map&quot; id=&quot;map_3f1e88876c28404ebe016265acb234f0&quot; &gt;&lt;/div&gt;
    </code></pre>
</body>
<script>
<pre><code>    var map_3f1e88876c28404ebe016265acb234f0 = L.map(
            &quot;map_3f1e88876c28404ebe016265acb234f0&quot;,
            {
                center: [45.372, -121.6972],
                crs: L.CRS.EPSG3857,
                maxBounds: [[-190, -50], [190, 75]],
                zoom: 3,
                zoomControl: true,
                preferCanvas: false,
            }
        );





        var tile_layer_761d9851b2964eb5a81c990cfc24f15e = L.tileLayer(
            &quot;https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png&quot;,
            {&quot;attribution&quot;: &quot;Data by \u0026copy; \u003ca href=\&quot;http://openstreetmap.org\&quot;\u003eOpenStreetMap</code></pre>

## Libraries
* [**Folium**](https://python-visualization.github.io/folium/) to create the map, markers, and interactivity.
* [**PyOWM**](https://pyowm.readthedocs.io/en/latest/) for interacting with the OpenWeatherMap API
* [**PyTz**](http://pytz.sourceforge.net/) for querying TimeZone database
