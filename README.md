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
<!DOCTYPE html>
<head>    
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    
        <script>
            L_NO_TOUCH = false;
            L_DISABLE_3D = false;
        </script>
    
    <script src="https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.js"></script>
    <script src="https://code.jquery.com/jquery-1.12.4.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/js/bootstrap.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.js"></script>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/leaflet@1.5.1/dist/leaflet.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap-theme.min.css"/>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/font-awesome/4.6.3/css/font-awesome.min.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/Leaflet.awesome-markers/2.0.2/leaflet.awesome-markers.css"/>
    <link rel="stylesheet" href="https://rawcdn.githack.com/python-visualization/folium/master/folium/templates/leaflet.awesome.rotate.css"/>
    <style>html, body {width: 100%;height: 100%;margin: 0;padding: 0;}</style>
    <style>#map {position:absolute;top:0;bottom:0;right:0;left:0;}</style>
    
            <meta name="viewport" content="width=device-width,
                initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />
            <style>
                #map_3f1e88876c28404ebe016265acb234f0 {
                    position: relative;
                    width: 100.0%;
                    height: 100.0%;
                    left: 0.0%;
                    top: 0.0%;
                }
            </style>
        
    <script src="https://rawcdn.githack.com/ardhi/Leaflet.MousePosition/c32f1c84/src/L.Control.MousePosition.js"></script>
    <link rel="stylesheet" href="https://rawcdn.githack.com/ardhi/Leaflet.MousePosition/c32f1c84/src/L.Control.MousePosition.css"/>
</head>
<body>    
    
            <div class="folium-map" id="map_3f1e88876c28404ebe016265acb234f0" ></div>
        
</body>
<script>    
    
            var map_3f1e88876c28404ebe016265acb234f0 = L.map(
                "map_3f1e88876c28404ebe016265acb234f0",
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
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 2, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_3f1e88876c28404ebe016265acb234f0);
        
    
            var mouse_position_ad5559e85c6f453a9a788911863bbc5e = new L.Control.MousePosition(
                {"emptyString": "", "lngFirst": true, "numDigits": 20, "position": "topright", "prefix": "Coordinates:", "separator": " | "}
            );
            mouse_position_ad5559e85c6f453a9a788911863bbc5e.options["latFormatter"] =
                function(num) {return L.Util.formatNum(num, 3) + ' º ';};;
            mouse_position_ad5559e85c6f453a9a788911863bbc5e.options["lngFormatter"] =
                function(num) {return L.Util.formatNum(num, 3) + ' º ';};;
            map_3f1e88876c28404ebe016265acb234f0.addControl(mouse_position_ad5559e85c6f453a9a788911863bbc5e);
        
    
            var feature_group_25ef0eed750248cea3908f2b268793db = L.featureGroup(
                {}
            ).addTo(map_3f1e88876c28404ebe016265acb234f0);
        
    
            var marker_96c26997481f480d884de36cfb9e6207 = L.marker(
                [29.72844, -95.5554],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_22f02f235ea741cdb203415780d740cf = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_96c26997481f480d884de36cfb9e6207.setIcon(icon_22f02f235ea741cdb203415780d740cf);
        
    
        var popup_ec3ace6590a5479ab337572012dfe43c = L.popup({"maxWidth": "100%"});

        
            var html_577a15f044354ec297867b5bfee70004 = $(`<div id="html_577a15f044354ec297867b5bfee70004" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_houston.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Houston, USA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;12:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;11.96°C   /   53.53°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_ec3ace6590a5479ab337572012dfe43c.setContent(html_577a15f044354ec297867b5bfee70004);
        

        marker_96c26997481f480d884de36cfb9e6207.bindPopup(popup_ec3ace6590a5479ab337572012dfe43c)
        ;

        
    
    
            marker_96c26997481f480d884de36cfb9e6207.bindTooltip(
                `<div>
                     Houston
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_190aff144b7f452d993cd055f931e4b8 = L.marker(
                [44.052071, -123.086754],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_268b13a26d9d47778d93b738681a8407 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_190aff144b7f452d993cd055f931e4b8.setIcon(icon_268b13a26d9d47778d93b738681a8407);
        
    
        var popup_fae0fa510d684221a3ed458c3a431841 = L.popup({"maxWidth": "100%"});

        
            var html_ac2f323fbd444e9c97c51d1889d7384f = $(`<div id="html_ac2f323fbd444e9c97c51d1889d7384f" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_eugene.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Eugene, USA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;10:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;6.52°C   /   43.74°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_fae0fa510d684221a3ed458c3a431841.setContent(html_ac2f323fbd444e9c97c51d1889d7384f);
        

        marker_190aff144b7f452d993cd055f931e4b8.bindPopup(popup_fae0fa510d684221a3ed458c3a431841)
        ;

        
    
    
            marker_190aff144b7f452d993cd055f931e4b8.bindTooltip(
                `<div>
                     Eugene
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6acc0a2d28d2402d9c928242a41e99cc = L.marker(
                [51.04869, -114.0732],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_aa1736670bd04e75981463059001aac7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_6acc0a2d28d2402d9c928242a41e99cc.setIcon(icon_aa1736670bd04e75981463059001aac7);
        
    
        var popup_117bc276e6c740f298d2a5b2504e4b06 = L.popup({"maxWidth": "100%"});

        
            var html_c8fb9d0b403c417bbebc33159421566e = $(`<div id="html_c8fb9d0b403c417bbebc33159421566e" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_calgary.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Calgary, CANADA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;11:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;-23.14°C   /   -9.65°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_117bc276e6c740f298d2a5b2504e4b06.setContent(html_c8fb9d0b403c417bbebc33159421566e);
        

        marker_6acc0a2d28d2402d9c928242a41e99cc.bindPopup(popup_117bc276e6c740f298d2a5b2504e4b06)
        ;

        
    
    
            marker_6acc0a2d28d2402d9c928242a41e99cc.bindTooltip(
                `<div>
                     Calgary
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_68526fdd2158430683f7a974f0d568be = L.marker(
                [33.674141, -117.670097],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_23298897116a4b7c9e7eb8fb1e960122 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_68526fdd2158430683f7a974f0d568be.setIcon(icon_23298897116a4b7c9e7eb8fb1e960122);
        
    
        var popup_2ce39a34f9e9419687184d874b1a17d7 = L.popup({"maxWidth": "100%"});

        
            var html_dd0e3420b1cc44d99af4493e4ab9c9c4 = $(`<div id="html_dd0e3420b1cc44d99af4493e4ab9c9c4" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://california.wonderware.com/media/WWNC/images/2018_LakeForest_Event/Wonderware_HQ.png width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Lake Forest, USA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;10:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;13.35°C   /   56.03°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_2ce39a34f9e9419687184d874b1a17d7.setContent(html_dd0e3420b1cc44d99af4493e4ab9c9c4);
        

        marker_68526fdd2158430683f7a974f0d568be.bindPopup(popup_2ce39a34f9e9419687184d874b1a17d7)
        ;

        
    
    
            marker_68526fdd2158430683f7a974f0d568be.bindTooltip(
                `<div>
                     Lake Forest
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1db208ab694a4fb2ab8e7ea5f0493091 = L.marker(
                [39.952583, -75.165222],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_8d579bd5621442f49e8e3554d3bebf8f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_1db208ab694a4fb2ab8e7ea5f0493091.setIcon(icon_8d579bd5621442f49e8e3554d3bebf8f);
        
    
        var popup_9b37fb8c42a04bbf8476ec0074f0e59e = L.popup({"maxWidth": "100%"});

        
            var html_a72b25300bbe4abd805ce3148480c40b = $(`<div id="html_a72b25300bbe4abd805ce3148480c40b" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_philadelphia.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Philadelphia, USA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;13:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;17.94°C   /   64.29°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_9b37fb8c42a04bbf8476ec0074f0e59e.setContent(html_a72b25300bbe4abd805ce3148480c40b);
        

        marker_1db208ab694a4fb2ab8e7ea5f0493091.bindPopup(popup_9b37fb8c42a04bbf8476ec0074f0e59e)
        ;

        
    
    
            marker_1db208ab694a4fb2ab8e7ea5f0493091.bindTooltip(
                `<div>
                     Philadelphia
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7304dc0c9e894e8ea00e3d51eaa63829 = L.marker(
                [19.432608, -99.133209],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_cf71a059b4be4ac5a541851912db6ad6 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_7304dc0c9e894e8ea00e3d51eaa63829.setIcon(icon_cf71a059b4be4ac5a541851912db6ad6);
        
    
        var popup_6a209d0b793d4c5ca363a44d50fe7aba = L.popup({"maxWidth": "100%"});

        
            var html_44dc1fcf016440859a8a67d04c4fda49 = $(`<div id="html_44dc1fcf016440859a8a67d04c4fda49" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_mexico-city.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Mexico City, MEXICO</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;12:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;20.94°C   /   69.69°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_6a209d0b793d4c5ca363a44d50fe7aba.setContent(html_44dc1fcf016440859a8a67d04c4fda49);
        

        marker_7304dc0c9e894e8ea00e3d51eaa63829.bindPopup(popup_6a209d0b793d4c5ca363a44d50fe7aba)
        ;

        
    
    
            marker_7304dc0c9e894e8ea00e3d51eaa63829.bindTooltip(
                `<div>
                     Mexico City
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_60e9a644447d4777bb19de1a46eaf37d = L.marker(
                [-22.906847, -43.172897],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_d2dc93045b2f45c7a853ffad2317022f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_60e9a644447d4777bb19de1a46eaf37d.setIcon(icon_d2dc93045b2f45c7a853ffad2317022f);
        
    
        var popup_593c92437bf6435292e10f428598614f = L.popup({"maxWidth": "100%"});

        
            var html_1adb5ab1fa2a4ccfb254e33b3da9a200 = $(`<div id="html_1adb5ab1fa2a4ccfb254e33b3da9a200" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_rio.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Rio, BRASIL</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;15:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;6.82°C   /   44.28°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_593c92437bf6435292e10f428598614f.setContent(html_1adb5ab1fa2a4ccfb254e33b3da9a200);
        

        marker_60e9a644447d4777bb19de1a46eaf37d.bindPopup(popup_593c92437bf6435292e10f428598614f)
        ;

        
    
    
            marker_60e9a644447d4777bb19de1a46eaf37d.bindTooltip(
                `<div>
                     Rio
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c80a4aa9a11c46d2b1c711e24cefbe0a = L.marker(
                [-33.448891, -70.669266],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_f693eca5fda547c6abf511d18e4fd48d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_c80a4aa9a11c46d2b1c711e24cefbe0a.setIcon(icon_f693eca5fda547c6abf511d18e4fd48d);
        
    
        var popup_59f2e3d493f847aa87ed5cfdd124356f = L.popup({"maxWidth": "100%"});

        
            var html_0aeae1002a534574a0beff359c9e1172 = $(`<div id="html_0aeae1002a534574a0beff359c9e1172" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_santiago.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Santiago, CHILE</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;15:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;32.99°C   /   91.38°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_59f2e3d493f847aa87ed5cfdd124356f.setContent(html_0aeae1002a534574a0beff359c9e1172);
        

        marker_c80a4aa9a11c46d2b1c711e24cefbe0a.bindPopup(popup_59f2e3d493f847aa87ed5cfdd124356f)
        ;

        
    
    
            marker_c80a4aa9a11c46d2b1c711e24cefbe0a.bindTooltip(
                `<div>
                     Santiago
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a52b1ce7f0904c4bbe15367413987a3a = L.marker(
                [4.710989, -74.07209],
                {}
            ).addTo(feature_group_25ef0eed750248cea3908f2b268793db);
        
    
            var icon_f2f1b441303846668d2dce53089a7529 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "green", "prefix": "fa"}
            );
            marker_a52b1ce7f0904c4bbe15367413987a3a.setIcon(icon_f2f1b441303846668d2dce53089a7529);
        
    
        var popup_0fb7d246fdd640af8cb54c480147ec4b = L.popup({"maxWidth": "100%"});

        
            var html_66b1b2bec4e2460c930f7eca8875a707 = $(`<div id="html_66b1b2bec4e2460c930f7eca8875a707" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_bogota.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Bogota, COLOMBIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;13:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;20.0°C   /   68.0°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_0fb7d246fdd640af8cb54c480147ec4b.setContent(html_66b1b2bec4e2460c930f7eca8875a707);
        

        marker_a52b1ce7f0904c4bbe15367413987a3a.bindPopup(popup_0fb7d246fdd640af8cb54c480147ec4b)
        ;

        
    
    
            marker_a52b1ce7f0904c4bbe15367413987a3a.bindTooltip(
                `<div>
                     Bogota
                 </div>`,
                {"sticky": true}
            );
        
    
            var feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d = L.featureGroup(
                {}
            ).addTo(map_3f1e88876c28404ebe016265acb234f0);
        
    
            var marker_47c24cf032574e3b9ccb2494fbe14772 = L.marker(
                [55.60355, 13.0109],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_d771d472182146f09c7af24c549b41a2 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_47c24cf032574e3b9ccb2494fbe14772.setIcon(icon_d771d472182146f09c7af24c549b41a2);
        
    
        var popup_d33ec599f213461e94fc23c1751889f1 = L.popup({"maxWidth": "100%"});

        
            var html_b6439729c5e64058bc7da63d1ec0210c = $(`<div id="html_b6439729c5e64058bc7da63d1ec0210c" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_malmo.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Malmo, SWEDEN</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.91°C   /   40.84°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_d33ec599f213461e94fc23c1751889f1.setContent(html_b6439729c5e64058bc7da63d1ec0210c);
        

        marker_47c24cf032574e3b9ccb2494fbe14772.bindPopup(popup_d33ec599f213461e94fc23c1751889f1)
        ;

        
    
    
            marker_47c24cf032574e3b9ccb2494fbe14772.bindTooltip(
                `<div>
                     Malmo
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_357f659137684c9d892f1af65f720a37 = L.marker(
                [52.21351, 0.08444],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_090cb6d70e0044a4b0374ee8219891e7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_357f659137684c9d892f1af65f720a37.setIcon(icon_090cb6d70e0044a4b0374ee8219891e7);
        
    
        var popup_7c9f8fef81ad474c8b474222de61842e = L.popup({"maxWidth": "100%"});

        
            var html_c643b8e4e92d479e82f793da52a8e1cc = $(`<div id="html_c643b8e4e92d479e82f793da52a8e1cc" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_cambridge.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Cambridge, UK</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;18:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;-3.29°C   /   26.08°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_7c9f8fef81ad474c8b474222de61842e.setContent(html_c643b8e4e92d479e82f793da52a8e1cc);
        

        marker_357f659137684c9d892f1af65f720a37.bindPopup(popup_7c9f8fef81ad474c8b474222de61842e)
        ;

        
    
    
            marker_357f659137684c9d892f1af65f720a37.bindTooltip(
                `<div>
                     Cambridge
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1114efe1e3654ecc94e3f8e6a993d238 = L.marker(
                [53.480759, -2.242631],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_72b87c9d80b149179748f3640c9b8ebb = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_1114efe1e3654ecc94e3f8e6a993d238.setIcon(icon_72b87c9d80b149179748f3640c9b8ebb);
        
    
        var popup_33d7ee00c23840f2aa8e0fe16a407951 = L.popup({"maxWidth": "100%"});

        
            var html_16053c35844446df94d4660929e775e9 = $(`<div id="html_16053c35844446df94d4660929e775e9" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_manchester.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Manchester, UK</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;18:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.83°C   /   40.69°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_33d7ee00c23840f2aa8e0fe16a407951.setContent(html_16053c35844446df94d4660929e775e9);
        

        marker_1114efe1e3654ecc94e3f8e6a993d238.bindPopup(popup_33d7ee00c23840f2aa8e0fe16a407951)
        ;

        
    
    
            marker_1114efe1e3654ecc94e3f8e6a993d238.bindTooltip(
                `<div>
                     Manchester
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_64ae6fee7d1c4c90b066bf9675682ed5 = L.marker(
                [51.507351, -0.127758],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_7abd12f5324442df8f789a7b82e3d5e4 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_64ae6fee7d1c4c90b066bf9675682ed5.setIcon(icon_7abd12f5324442df8f789a7b82e3d5e4);
        
    
        var popup_b9fa2ad6d2014404bb2a04e52fedf9a3 = L.popup({"maxWidth": "100%"});

        
            var html_f609451bbf0545a08701a2096a290978 = $(`<div id="html_f609451bbf0545a08701a2096a290978" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_london.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>London, UK</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;18:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;6.77°C   /   44.19°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_b9fa2ad6d2014404bb2a04e52fedf9a3.setContent(html_f609451bbf0545a08701a2096a290978);
        

        marker_64ae6fee7d1c4c90b066bf9675682ed5.bindPopup(popup_b9fa2ad6d2014404bb2a04e52fedf9a3)
        ;

        
    
    
            marker_64ae6fee7d1c4c90b066bf9675682ed5.bindTooltip(
                `<div>
                     London
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_efa5b4901e474e7b94dfc67a09263473 = L.marker(
                [54.996613, -7.308575],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_f9ce63a233a2482889d78e81c08afa08 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_efa5b4901e474e7b94dfc67a09263473.setIcon(icon_f9ce63a233a2482889d78e81c08afa08);
        
    
        var popup_30508392d14743339dac519647afc1df = L.popup({"maxWidth": "100%"});

        
            var html_a39267d725fd4075a1d4c779190bfb53 = $(`<div id="html_a39267d725fd4075a1d4c779190bfb53" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Internals-Small-Offices-EMEA.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Derry, UK</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;18:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;5.45°C   /   41.81°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_30508392d14743339dac519647afc1df.setContent(html_a39267d725fd4075a1d4c779190bfb53);
        

        marker_efa5b4901e474e7b94dfc67a09263473.bindPopup(popup_30508392d14743339dac519647afc1df)
        ;

        
    
    
            marker_efa5b4901e474e7b94dfc67a09263473.bindTooltip(
                `<div>
                     Derry
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_a549e096d1a24420912e4a14e11ebaf4 = L.marker(
                [53.235359, -1.42415],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_46d2ba0507804e4c887e7b842514a562 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_a549e096d1a24420912e4a14e11ebaf4.setIcon(icon_46d2ba0507804e4c887e7b842514a562);
        
    
        var popup_3bb74253017648dcaf70ff50d1ede7fc = L.popup({"maxWidth": "100%"});

        
            var html_f141fe92eb2542dc920976c2b477f19c = $(`<div id="html_f141fe92eb2542dc920976c2b477f19c" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_chesterfield.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Chesterfield, UK</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;18:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19.9°C   /   67.82°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_3bb74253017648dcaf70ff50d1ede7fc.setContent(html_f141fe92eb2542dc920976c2b477f19c);
        

        marker_a549e096d1a24420912e4a14e11ebaf4.bindPopup(popup_3bb74253017648dcaf70ff50d1ede7fc)
        ;

        
    
    
            marker_a549e096d1a24420912e4a14e11ebaf4.bindTooltip(
                `<div>
                     Chesterfield
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c04e7548582f4da6a4153f4a7c1aaded = L.marker(
                [48.84313, 2.42938],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_7138811de3534814a53717c9276a2862 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c04e7548582f4da6a4153f4a7c1aaded.setIcon(icon_7138811de3534814a53717c9276a2862);
        
    
        var popup_268715b2eea348c0b9a919674f934db5 = L.popup({"maxWidth": "100%"});

        
            var html_0c310ef56d7d48d284717cf3ad5711d7 = $(`<div id="html_0c310ef56d7d48d284717cf3ad5711d7" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_paris.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Paris, FRANCE</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;8.28°C   /   46.9°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_268715b2eea348c0b9a919674f934db5.setContent(html_0c310ef56d7d48d284717cf3ad5711d7);
        

        marker_c04e7548582f4da6a4153f4a7c1aaded.bindPopup(popup_268715b2eea348c0b9a919674f934db5)
        ;

        
    
    
            marker_c04e7548582f4da6a4153f4a7c1aaded.bindTooltip(
                `<div>
                     Paris
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e0fa4e8484b041c28007daf9e5a54ffe = L.marker(
                [55.71998, 37.62822],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_bd668b08f2814aeb8227cd3b9eb0caaf = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_e0fa4e8484b041c28007daf9e5a54ffe.setIcon(icon_bd668b08f2814aeb8227cd3b9eb0caaf);
        
    
        var popup_bb733eb3c46c4b4dbaac8de56baddd57 = L.popup({"maxWidth": "100%"});

        
            var html_92659c60a6b143cdbf5fdd0905262ef2 = $(`<div id="html_92659c60a6b143cdbf5fdd0905262ef2" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_moscow.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Moscow, RUSSIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;21:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;-0.97°C   /   30.25°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_bb733eb3c46c4b4dbaac8de56baddd57.setContent(html_92659c60a6b143cdbf5fdd0905262ef2);
        

        marker_e0fa4e8484b041c28007daf9e5a54ffe.bindPopup(popup_bb733eb3c46c4b4dbaac8de56baddd57)
        ;

        
    
    
            marker_e0fa4e8484b041c28007daf9e5a54ffe.bindTooltip(
                `<div>
                     Moscow
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_c78a21812dca4bed86e0e278ea16f421 = L.marker(
                [59.94185, 30.37332],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_a0794261afae411ea6b88ce95fd68ef9 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_c78a21812dca4bed86e0e278ea16f421.setIcon(icon_a0794261afae411ea6b88ce95fd68ef9);
        
    
        var popup_5ccf43d343484ff589857edfa5aa3e95 = L.popup({"maxWidth": "100%"});

        
            var html_76fbf6aba4a6404bac3dae26aa81d223 = $(`<div id="html_76fbf6aba4a6404bac3dae26aa81d223" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_st-petersburg.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>St. Petersburg, RUSSIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;21:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.8°C   /   40.64°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_5ccf43d343484ff589857edfa5aa3e95.setContent(html_76fbf6aba4a6404bac3dae26aa81d223);
        

        marker_c78a21812dca4bed86e0e278ea16f421.bindPopup(popup_5ccf43d343484ff589857edfa5aa3e95)
        ;

        
    
    
            marker_c78a21812dca4bed86e0e278ea16f421.bindTooltip(
                `<div>
                     St. Petersburg
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_1e030c30788e4545812f6a256b365525 = L.marker(
                [26.282502, 50.213035],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_1d3f5921948a4a8e8686e98fad0cc533 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_1e030c30788e4545812f6a256b365525.setIcon(icon_1d3f5921948a4a8e8686e98fad0cc533);
        
    
        var popup_ebf73ba8d40247b995c91c35f167dd56 = L.popup({"maxWidth": "100%"});

        
            var html_df7d4e6055e54cca9b05cb5aa704af36 = $(`<div id="html_df7d4e6055e54cca9b05cb5aa704af36" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://static.travelweekly.com/i/sized/780/437/www.cfmedia.vfmleonardo.com/imageRepo/4/0/81/783/23/Hotel_Exterior_(1)_S.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Al Khobar, SAUDI ARABIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;21:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;13.9°C   /   57.02°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_ebf73ba8d40247b995c91c35f167dd56.setContent(html_df7d4e6055e54cca9b05cb5aa704af36);
        

        marker_1e030c30788e4545812f6a256b365525.bindPopup(popup_ebf73ba8d40247b995c91c35f167dd56)
        ;

        
    
    
            marker_1e030c30788e4545812f6a256b365525.bindTooltip(
                `<div>
                     Al Khobar
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_485a754467b0483683887a55789315f4 = L.marker(
                [41.042283, 28.97771],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_75d842380d884cd992864eff0d7cba07 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_485a754467b0483683887a55789315f4.setIcon(icon_75d842380d884cd992864eff0d7cba07);
        
    
        var popup_1dafde0cfa4a45cb9629506e9aa749a6 = L.popup({"maxWidth": "100%"});

        
            var html_152c69c08a4f43e9884a6eeec464ed59 = $(`<div id="html_152c69c08a4f43e9884a6eeec464ed59" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_istanbul.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Istanbul, TURKEY</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;21:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;8.21°C   /   46.78°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_1dafde0cfa4a45cb9629506e9aa749a6.setContent(html_152c69c08a4f43e9884a6eeec464ed59);
        

        marker_485a754467b0483683887a55789315f4.bindPopup(popup_1dafde0cfa4a45cb9629506e9aa749a6)
        ;

        
    
    
            marker_485a754467b0483683887a55789315f4.bindTooltip(
                `<div>
                     Istanbul
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6bc403b4d64148d7b42b985129ddf94d = L.marker(
                [25.044362, 55.240822],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_14b19086a4af4a7fbfbed31680c013da = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6bc403b4d64148d7b42b985129ddf94d.setIcon(icon_14b19086a4af4a7fbfbed31680c013da);
        
    
        var popup_809316720360465e8c77d5f63fbbf576 = L.popup({"maxWidth": "100%"});

        
            var html_f745b08119ec41728b470d7806a06a4d = $(`<div id="html_f745b08119ec41728b470d7806a06a4d" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_dubai.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Dubai, UAE</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;22:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;16.61°C   /   61.9°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;</td> </tr>  </tbody> </table> </div>`)[0];
            popup_809316720360465e8c77d5f63fbbf576.setContent(html_f745b08119ec41728b470d7806a06a4d);
        

        marker_6bc403b4d64148d7b42b985129ddf94d.bindPopup(popup_809316720360465e8c77d5f63fbbf576)
        ;

        
    
    
            marker_6bc403b4d64148d7b42b985129ddf94d.bindTooltip(
                `<div>
                     Dubai
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_36094fdb9d4a4da694f5b4c38c22d987 = L.marker(
                [26.820553, 30.802498],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_16f18ac9b45a4d99bebf57bfa648c74d = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_36094fdb9d4a4da694f5b4c38c22d987.setIcon(icon_16f18ac9b45a4d99bebf57bfa648c74d);
        
    
        var popup_8c8554b4781a4805a4fc18b65eccffd5 = L.popup({"maxWidth": "100%"});

        
            var html_2d8b8f8ff99b4cc28f6d076d21386a02 = $(`<div id="html_2d8b8f8ff99b4cc28f6d076d21386a02" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_egypt.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Cairo, EGYPT</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;20:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;15.0°C   /   59.0°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_8c8554b4781a4805a4fc18b65eccffd5.setContent(html_2d8b8f8ff99b4cc28f6d076d21386a02);
        

        marker_36094fdb9d4a4da694f5b4c38c22d987.bindPopup(popup_8c8554b4781a4805a4fc18b65eccffd5)
        ;

        
    
    
            marker_36094fdb9d4a4da694f5b4c38c22d987.bindTooltip(
                `<div>
                     Cairo
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f33e49ab39474b7090e39e56e894386e = L.marker(
                [23.58589, 58.405922],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_08b1ffcc12e34b79ad370b54a7fdd482 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f33e49ab39474b7090e39e56e894386e.setIcon(icon_08b1ffcc12e34b79ad370b54a7fdd482);
        
    
        var popup_adf332146ddd482c877af39376a31571 = L.popup({"maxWidth": "100%"});

        
            var html_b70f7c53a02743a2884e6a8afd05e3fd = $(`<div id="html_b70f7c53a02743a2884e6a8afd05e3fd" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_oman.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Muscat, OMAN</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;20:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;18.0°C   /   64.4°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_adf332146ddd482c877af39376a31571.setContent(html_b70f7c53a02743a2884e6a8afd05e3fd);
        

        marker_f33e49ab39474b7090e39e56e894386e.bindPopup(popup_adf332146ddd482c877af39376a31571)
        ;

        
    
    
            marker_f33e49ab39474b7090e39e56e894386e.bindTooltip(
                `<div>
                     Muscat
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_20d1954db4424ed29a0b328d436881c4 = L.marker(
                [60.29322, 24.96814],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_cea4838f162347a385f6a491669e2576 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_20d1954db4424ed29a0b328d436881c4.setIcon(icon_cea4838f162347a385f6a491669e2576);
        
    
        var popup_f3b6fe78ffab4ef88d6058034d375435 = L.popup({"maxWidth": "100%"});

        
            var html_0d167fb2e3dd4d2fb9df92c2e4898663 = $(`<div id="html_0d167fb2e3dd4d2fb9df92c2e4898663" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_helsinki.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Helsinki, FINLAND</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;21:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.48°C   /   40.06°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_f3b6fe78ffab4ef88d6058034d375435.setContent(html_0d167fb2e3dd4d2fb9df92c2e4898663);
        

        marker_20d1954db4424ed29a0b328d436881c4.bindPopup(popup_f3b6fe78ffab4ef88d6058034d375435)
        ;

        
    
    
            marker_20d1954db4424ed29a0b328d436881c4.bindTooltip(
                `<div>
                     Helsinki
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_8a8565350e1e464ab4c6498ce951423a = L.marker(
                [53.10784, 8.86275],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_7de79346274241f2b7b04123f3ece3bd = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_8a8565350e1e464ab4c6498ce951423a.setIcon(icon_7de79346274241f2b7b04123f3ece3bd);
        
    
        var popup_fa6d7e3a36434b81890684585fae480f = L.popup({"maxWidth": "100%"});

        
            var html_91b977411251456390f3552c7a6898f6 = $(`<div id="html_91b977411251456390f3552c7a6898f6" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_bremen.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Bremen, GERMANY</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;8.07°C   /   46.53°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_fa6d7e3a36434b81890684585fae480f.setContent(html_91b977411251456390f3552c7a6898f6);
        

        marker_8a8565350e1e464ab4c6498ce951423a.bindPopup(popup_fa6d7e3a36434b81890684585fae480f)
        ;

        
    
    
            marker_8a8565350e1e464ab4c6498ce951423a.bindTooltip(
                `<div>
                     Bremen
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_325da23ec29e4efbb469621aac6cf191 = L.marker(
                [51.46688, 7.27593],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_a9756f769ca846a7bdb5e38c2d3b276a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_325da23ec29e4efbb469621aac6cf191.setIcon(icon_a9756f769ca846a7bdb5e38c2d3b276a);
        
    
        var popup_d5a4b23fca0444ceb3a36a4f696b008e = L.popup({"maxWidth": "100%"});

        
            var html_fe8f00697da84e79ae8b64925c5743b5 = $(`<div id="html_fe8f00697da84e79ae8b64925c5743b5" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_bochum.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Bochum, GERMANY</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;7.82°C   /   46.08°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_d5a4b23fca0444ceb3a36a4f696b008e.setContent(html_fe8f00697da84e79ae8b64925c5743b5);
        

        marker_325da23ec29e4efbb469621aac6cf191.bindPopup(popup_d5a4b23fca0444ceb3a36a4f696b008e)
        ;

        
    
    
            marker_325da23ec29e4efbb469621aac6cf191.bindTooltip(
                `<div>
                     Bochum
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_96a3554be1a84afaa1ab9fedaeab039d = L.marker(
                [53.6049, 9.95609],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_16faba5f71ac4d33b068fbba1e20be2b = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_96a3554be1a84afaa1ab9fedaeab039d.setIcon(icon_16faba5f71ac4d33b068fbba1e20be2b);
        
    
        var popup_8c1697a2fc0446268d0f3a090f4326ff = L.popup({"maxWidth": "100%"});

        
            var html_f2d1ca58d40f499a91dc40eef455c8c3 = $(`<div id="html_f2d1ca58d40f499a91dc40eef455c8c3" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_hamburg.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Hamburg, GERMANY</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;7.15°C   /   44.87°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_8c1697a2fc0446268d0f3a090f4326ff.setContent(html_f2d1ca58d40f499a91dc40eef455c8c3);
        

        marker_96a3554be1a84afaa1ab9fedaeab039d.bindPopup(popup_8c1697a2fc0446268d0f3a090f4326ff)
        ;

        
    
    
            marker_96a3554be1a84afaa1ab9fedaeab039d.bindTooltip(
                `<div>
                     Hamburg
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_e0c71b07d66d4db694ff0223ad407381 = L.marker(
                [50.13075, 8.51832],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_822ca19370464d9c95813f6752da9d53 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_e0c71b07d66d4db694ff0223ad407381.setIcon(icon_822ca19370464d9c95813f6752da9d53);
        
    
        var popup_7330e8ab58544c728b65e49885fc675e = L.popup({"maxWidth": "100%"});

        
            var html_2ec8d6e4d6f34e8e8cbdb16e4d6f0a41 = $(`<div id="html_2ec8d6e4d6f34e8e8cbdb16e4d6f0a41" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_frankfurt.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Frankfurt, GERMANY</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.24°C   /   39.63°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_7330e8ab58544c728b65e49885fc675e.setContent(html_2ec8d6e4d6f34e8e8cbdb16e4d6f0a41);
        

        marker_e0c71b07d66d4db694ff0223ad407381.bindPopup(popup_7330e8ab58544c728b65e49885fc675e)
        ;

        
    
    
            marker_e0c71b07d66d4db694ff0223ad407381.bindTooltip(
                `<div>
                     Frankfurt
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_50750eccdbea4bb6aee7e78b3239690a = L.marker(
                [53.13042, -6.74563],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_dfebcb6ed9bc4e088b11a3bf59ed13e3 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_50750eccdbea4bb6aee7e78b3239690a.setIcon(icon_dfebcb6ed9bc4e088b11a3bf59ed13e3);
        
    
        var popup_9530461f8be344b7a6b4cd8853dac17f = L.popup({"maxWidth": "100%"});

        
            var html_021db9f61b7b427184791b474ea1e560 = $(`<div id="html_021db9f61b7b427184791b474ea1e560" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_kilcullen.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Kilcullen, IRELAND</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;18:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.39°C   /   39.9°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_9530461f8be344b7a6b4cd8853dac17f.setContent(html_021db9f61b7b427184791b474ea1e560);
        

        marker_50750eccdbea4bb6aee7e78b3239690a.bindPopup(popup_9530461f8be344b7a6b4cd8853dac17f)
        ;

        
    
    
            marker_50750eccdbea4bb6aee7e78b3239690a.bindTooltip(
                `<div>
                     Kilcullen
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_64a1493108594ad38faf320aca894895 = L.marker(
                [44.407059, 8.93399],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_c45261f6b4154811aae85dc7d6d77999 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_64a1493108594ad38faf320aca894895.setIcon(icon_c45261f6b4154811aae85dc7d6d77999);
        
    
        var popup_57fca532e94043adbe3000a69ba641ce = L.popup({"maxWidth": "100%"});

        
            var html_8b84a053b0ac41759d048d4bb8dc6ecb = $(`<div id="html_8b84a053b0ac41759d048d4bb8dc6ecb" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_genoa.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Genoa, ITALY</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;5.74°C   /   42.33°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_57fca532e94043adbe3000a69ba641ce.setContent(html_8b84a053b0ac41759d048d4bb8dc6ecb);
        

        marker_64a1493108594ad38faf320aca894895.bindPopup(popup_57fca532e94043adbe3000a69ba641ce)
        ;

        
    
    
            marker_64a1493108594ad38faf320aca894895.bindTooltip(
                `<div>
                     Genoa
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7231706b22ff485cbebf29905e54e617 = L.marker(
                [29.311661, 47.481766],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_85cd8b91e5364b3284cb8d132aa50467 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_7231706b22ff485cbebf29905e54e617.setIcon(icon_85cd8b91e5364b3284cb8d132aa50467);
        
    
        var popup_d9358e8d8ac04a57a0b7cc4e37635587 = L.popup({"maxWidth": "100%"});

        
            var html_6848c043bdbb46c08c0154409836e187 = $(`<div id="html_6848c043bdbb46c08c0154409836e187" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_kuwait.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Kuwait City, KUWAIT</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;21:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;10.0°C   /   50.0°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_d9358e8d8ac04a57a0b7cc4e37635587.setContent(html_6848c043bdbb46c08c0154409836e187);
        

        marker_7231706b22ff485cbebf29905e54e617.bindPopup(popup_d9358e8d8ac04a57a0b7cc4e37635587)
        ;

        
    
    
            marker_7231706b22ff485cbebf29905e54e617.bindTooltip(
                `<div>
                     Kuwait City
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_806d7cec0522421887561fdb599b3247 = L.marker(
                [9.081999, 8.675277],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_7f2cf3b2b8c647929c72ad7491218634 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_806d7cec0522421887561fdb599b3247.setIcon(icon_7f2cf3b2b8c647929c72ad7491218634);
        
    
        var popup_66e5b3f6f9dd49ffbe887c2fbbe16862 = L.popup({"maxWidth": "100%"});

        
            var html_c27a2cbb0306495a9f529e74798df3d7 = $(`<div id="html_c27a2cbb0306495a9f529e74798df3d7" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_nigeria.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Abuja, NIGERIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;33.0°C   /   91.4°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_66e5b3f6f9dd49ffbe887c2fbbe16862.setContent(html_c27a2cbb0306495a9f529e74798df3d7);
        

        marker_806d7cec0522421887561fdb599b3247.bindPopup(popup_66e5b3f6f9dd49ffbe887c2fbbe16862)
        ;

        
    
    
            marker_806d7cec0522421887561fdb599b3247.bindTooltip(
                `<div>
                     Abuja
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_be8ca5acee294148bd54c5d59fa54b96 = L.marker(
                [25.285446, 51.53104],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_131238cefe6e48f082c867b92194e132 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_be8ca5acee294148bd54c5d59fa54b96.setIcon(icon_131238cefe6e48f082c867b92194e132);
        
    
        var popup_fd4646ecc3f24a62bd1d855d4a53640e = L.popup({"maxWidth": "100%"});

        
            var html_1881f4e9471041e4874c26d9debfd8d8 = $(`<div id="html_1881f4e9471041e4874c26d9debfd8d8" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_qatar.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Doha, QATAR</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;21:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;14.56°C   /   58.21°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;</td> </tr>  </tbody> </table> </div>`)[0];
            popup_fd4646ecc3f24a62bd1d855d4a53640e.setContent(html_1881f4e9471041e4874c26d9debfd8d8);
        

        marker_be8ca5acee294148bd54c5d59fa54b96.bindPopup(popup_fd4646ecc3f24a62bd1d855d4a53640e)
        ;

        
    
    
            marker_be8ca5acee294148bd54c5d59fa54b96.bindTooltip(
                `<div>
                     Doha
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f0e12c4675ad42cdba957bb9529a1e65 = L.marker(
                [59.913868, 10.752245],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_98a7b3bfe9a4435c8d3f08eea7b53cce = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_f0e12c4675ad42cdba957bb9529a1e65.setIcon(icon_98a7b3bfe9a4435c8d3f08eea7b53cce);
        
    
        var popup_5ae74aca7e254c2ab95c2cbb9ec28e2a = L.popup({"maxWidth": "100%"});

        
            var html_de4448b1865548768c8318ccebd8db12 = $(`<div id="html_de4448b1865548768c8318ccebd8db12" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_oslo.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Oslo, NORWAY</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;0.63°C   /   33.13°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_5ae74aca7e254c2ab95c2cbb9ec28e2a.setContent(html_de4448b1865548768c8318ccebd8db12);
        

        marker_f0e12c4675ad42cdba957bb9529a1e65.bindPopup(popup_5ae74aca7e254c2ab95c2cbb9ec28e2a)
        ;

        
    
    
            marker_f0e12c4675ad42cdba957bb9529a1e65.bindTooltip(
                `<div>
                     Oslo
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d57f760c986040738dcd68dc7f3170f3 = L.marker(
                [58.964432, 5.72625],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_b353e3c0bc394ffea8226360e88c9719 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_d57f760c986040738dcd68dc7f3170f3.setIcon(icon_b353e3c0bc394ffea8226360e88c9719);
        
    
        var popup_751c207446de4ae8a05ecba6db6c5eed = L.popup({"maxWidth": "100%"});

        
            var html_ee45786fd00c4667a4f1e3a06d24f06e = $(`<div id="html_ee45786fd00c4667a4f1e3a06d24f06e" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_stavanger.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Stavanger, NORWAY</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.17°C   /   39.51°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_751c207446de4ae8a05ecba6db6c5eed.setContent(html_ee45786fd00c4667a4f1e3a06d24f06e);
        

        marker_d57f760c986040738dcd68dc7f3170f3.bindPopup(popup_751c207446de4ae8a05ecba6db6c5eed)
        ;

        
    
    
            marker_d57f760c986040738dcd68dc7f3170f3.bindTooltip(
                `<div>
                     Stavanger
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_6013afb3cc234fe1925e601d9f2ba835 = L.marker(
                [51.11055, 17.02556],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_2949f64604904e0698894a502c806901 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_6013afb3cc234fe1925e601d9f2ba835.setIcon(icon_2949f64604904e0698894a502c806901);
        
    
        var popup_9ee3f52fcaba4daeb10b7ebe4bd0bee6 = L.popup({"maxWidth": "100%"});

        
            var html_b085e7d6bf18401cad5467fcc1930349 = $(`<div id="html_b085e7d6bf18401cad5467fcc1930349" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_wroclaw.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Wroclaw, POLAND</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;3.31°C   /   37.96°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_9ee3f52fcaba4daeb10b7ebe4bd0bee6.setContent(html_b085e7d6bf18401cad5467fcc1930349);
        

        marker_6013afb3cc234fe1925e601d9f2ba835.bindPopup(popup_9ee3f52fcaba4daeb10b7ebe4bd0bee6)
        ;

        
    
    
            marker_6013afb3cc234fe1925e601d9f2ba835.bindTooltip(
                `<div>
                     Wroclaw
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5d4e6c2abc83448a9991d39b35b1a3cc = L.marker(
                [40.416775, -3.70379],
                {}
            ).addTo(feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d);
        
    
            var icon_71b187150aff4ad4990912da955a4eb5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "purple", "prefix": "fa"}
            );
            marker_5d4e6c2abc83448a9991d39b35b1a3cc.setIcon(icon_71b187150aff4ad4990912da955a4eb5);
        
    
        var popup_7d3fb81cda844e30b25e6181ff728187 = L.popup({"maxWidth": "100%"});

        
            var html_38ce8d2c83c74ed183663f4aab4f5709 = $(`<div id="html_38ce8d2c83c74ed183663f4aab4f5709" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_madrid.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Madrid, SPAIN</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Sunday, 01/12/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.38°C   /   39.88°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_7d3fb81cda844e30b25e6181ff728187.setContent(html_38ce8d2c83c74ed183663f4aab4f5709);
        

        marker_5d4e6c2abc83448a9991d39b35b1a3cc.bindPopup(popup_7d3fb81cda844e30b25e6181ff728187)
        ;

        
    
    
            marker_5d4e6c2abc83448a9991d39b35b1a3cc.bindTooltip(
                `<div>
                     Madrid
                 </div>`,
                {"sticky": true}
            );
        
    
            var feature_group_5cc3dfbb7f2345849fddc413e9db3545 = L.featureGroup(
                {}
            ).addTo(map_3f1e88876c28404ebe016265acb234f0);
        
    
            var marker_40a46f9c584c4df5883275673dd36fbd = L.marker(
                [-37.82076, 144.94809],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_b3506c42a2a34e5e8cce2c38173d39a7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_40a46f9c584c4df5883275673dd36fbd.setIcon(icon_b3506c42a2a34e5e8cce2c38173d39a7);
        
    
        var popup_613294fb9e33403a85f3cdf1266f5431 = L.popup({"maxWidth": "100%"});

        
            var html_280bd53582804c1fa02da2821cbdc4c7 = $(`<div id="html_280bd53582804c1fa02da2821cbdc4c7" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_melbourne.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Melbourne, AUSTRALIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;05:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;26.52°C   /   79.74°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_613294fb9e33403a85f3cdf1266f5431.setContent(html_280bd53582804c1fa02da2821cbdc4c7);
        

        marker_40a46f9c584c4df5883275673dd36fbd.bindPopup(popup_613294fb9e33403a85f3cdf1266f5431)
        ;

        
    
    
            marker_40a46f9c584c4df5883275673dd36fbd.bindTooltip(
                `<div>
                     Melbourne
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_3f0ce8f7efb64655a27e145936122d91 = L.marker(
                [17.44735, 78.37211],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_e0394ccb8d494c6aa344c88a876fe687 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_3f0ce8f7efb64655a27e145936122d91.setIcon(icon_e0394ccb8d494c6aa344c88a876fe687);
        
    
        var popup_bfaac31b1b684fd895692ac2e05481b4 = L.popup({"maxWidth": "100%"});

        
            var html_4bc3b20666ab44a7868c7ac7604052c4 = $(`<div id="html_4bc3b20666ab44a7868c7ac7604052c4" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_hyderabad.jpeg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Hyderabad, INDIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;00:24</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19.22°C   /   66.6°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_bfaac31b1b684fd895692ac2e05481b4.setContent(html_4bc3b20666ab44a7868c7ac7604052c4);
        

        marker_3f0ce8f7efb64655a27e145936122d91.bindPopup(popup_bfaac31b1b684fd895692ac2e05481b4)
        ;

        
    
    
            marker_3f0ce8f7efb64655a27e145936122d91.bindTooltip(
                `<div>
                     Hyderabad
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_b5949a93ba954f2cad77fe10512673b0 = L.marker(
                [12.92272, 77.6577],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_28b83d1ca8934408826ec816050fb2f1 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_b5949a93ba954f2cad77fe10512673b0.setIcon(icon_28b83d1ca8934408826ec816050fb2f1);
        
    
        var popup_2aa9a4995b9149d19854622ab527c456 = L.popup({"maxWidth": "100%"});

        
            var html_3ed4e34e7fb74ce49ae4301ea3b21353 = $(`<div id="html_3ed4e34e7fb74ce49ae4301ea3b21353" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://upload.wikimedia.org/wikipedia/commons/thumb/3/36/Bangalore_.jpg/220px-Bangalore_.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Bangalore, INDIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;00:24</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;19.0°C   /   66.2°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_2aa9a4995b9149d19854622ab527c456.setContent(html_3ed4e34e7fb74ce49ae4301ea3b21353);
        

        marker_b5949a93ba954f2cad77fe10512673b0.bindPopup(popup_2aa9a4995b9149d19854622ab527c456)
        ;

        
    
    
            marker_b5949a93ba954f2cad77fe10512673b0.bindTooltip(
                `<div>
                     Bangalore
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_489ebe39345a477f83024f66f07bcf66 = L.marker(
                [39.966696, 116.38094],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_d4d08de1fd9a4903939835a330a376ec = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_489ebe39345a477f83024f66f07bcf66.setIcon(icon_d4d08de1fd9a4903939835a330a376ec);
        
    
        var popup_5a8c848d7bff40f1a135fab20ccb21c3 = L.popup({"maxWidth": "100%"});

        
            var html_260337c41ea54a2f92b8006b70b383bc = $(`<div id="html_260337c41ea54a2f92b8006b70b383bc" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_beijing.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Beijing, CHINA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;02:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;-4.23°C   /   24.39°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_5a8c848d7bff40f1a135fab20ccb21c3.setContent(html_260337c41ea54a2f92b8006b70b383bc);
        

        marker_489ebe39345a477f83024f66f07bcf66.bindPopup(popup_5a8c848d7bff40f1a135fab20ccb21c3)
        ;

        
    
    
            marker_489ebe39345a477f83024f66f07bcf66.bindTooltip(
                `<div>
                     Beijing
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_d5b996e3833846fd9173c6a92f5f4099 = L.marker(
                [28.5356, 77.20908],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_a89935ec237d4ed1b455306472dbe27f = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_d5b996e3833846fd9173c6a92f5f4099.setIcon(icon_a89935ec237d4ed1b455306472dbe27f);
        
    
        var popup_5ade5e436f2f4a3fbfa6fcb3ac5b84f3 = L.popup({"maxWidth": "100%"});

        
            var html_89de0ef22c904ff1a07c0a82313e29a5 = $(`<div id="html_89de0ef22c904ff1a07c0a82313e29a5" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_new-delhi.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>New Delhi, INDIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;00:24</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;14.93°C   /   58.87°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_5ade5e436f2f4a3fbfa6fcb3ac5b84f3.setContent(html_89de0ef22c904ff1a07c0a82313e29a5);
        

        marker_d5b996e3833846fd9173c6a92f5f4099.bindPopup(popup_5ade5e436f2f4a3fbfa6fcb3ac5b84f3)
        ;

        
    
    
            marker_d5b996e3833846fd9173c6a92f5f4099.bindTooltip(
                `<div>
                     New Delhi
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_71beedf1f9d24a0481d1aee789dab0fd = L.marker(
                [19.11876, 72.91378],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_90ec2ea6668f440288f2af121bed3067 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_71beedf1f9d24a0481d1aee789dab0fd.setIcon(icon_90ec2ea6668f440288f2af121bed3067);
        
    
        var popup_278b3bd6dd244555b0955963e7a522f9 = L.popup({"maxWidth": "100%"});

        
            var html_766b390ebb8d4a47b87027a730fffb2b = $(`<div id="html_766b390ebb8d4a47b87027a730fffb2b" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_mumbai.jpeg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Mumbai, INDIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;00:24</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;26.0°C   /   78.8°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_278b3bd6dd244555b0955963e7a522f9.setContent(html_766b390ebb8d4a47b87027a730fffb2b);
        

        marker_71beedf1f9d24a0481d1aee789dab0fd.bindPopup(popup_278b3bd6dd244555b0955963e7a522f9)
        ;

        
    
    
            marker_71beedf1f9d24a0481d1aee789dab0fd.bindTooltip(
                `<div>
                     Mumbai
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_4cb8bbb597944ca8a5c260f1567d5883 = L.marker(
                [-31.95387, 115.85204],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_8bbfc2fc99d94be097a141685ee64673 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_4cb8bbb597944ca8a5c260f1567d5883.setIcon(icon_8bbfc2fc99d94be097a141685ee64673);
        
    
        var popup_428fcad6bef94759b538bd5ae41b79ce = L.popup({"maxWidth": "100%"});

        
            var html_d853039e8a884f5883cd0956906d1d6d = $(`<div id="html_d853039e8a884f5883cd0956906d1d6d" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_perth.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Perth, AUSTRALIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;02:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;20.5°C   /   68.9°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_428fcad6bef94759b538bd5ae41b79ce.setContent(html_d853039e8a884f5883cd0956906d1d6d);
        

        marker_4cb8bbb597944ca8a5c260f1567d5883.bindPopup(popup_428fcad6bef94759b538bd5ae41b79ce)
        ;

        
    
    
            marker_4cb8bbb597944ca8a5c260f1567d5883.bindTooltip(
                `<div>
                     Perth
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_7df8d4da340841d2a97a8c8d217d28ed = L.marker(
                [-27.46452, 153.03075],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_626421a8915f45e196617db9e9b40124 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_7df8d4da340841d2a97a8c8d217d28ed.setIcon(icon_626421a8915f45e196617db9e9b40124);
        
    
        var popup_eb4e2332bacb4fb495a96d0ecf6e55f2 = L.popup({"maxWidth": "100%"});

        
            var html_a633f6c454f54caaaac85335ba78e169 = $(`<div id="html_a633f6c454f54caaaac85335ba78e169" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_brisbane.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Brisbane, AUSTRALIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;04:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;22.01°C   /   71.62°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_eb4e2332bacb4fb495a96d0ecf6e55f2.setContent(html_a633f6c454f54caaaac85335ba78e169);
        

        marker_7df8d4da340841d2a97a8c8d217d28ed.bindPopup(popup_eb4e2332bacb4fb495a96d0ecf6e55f2)
        ;

        
    
    
            marker_7df8d4da340841d2a97a8c8d217d28ed.bindTooltip(
                `<div>
                     Brisbane
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_5ce0a692ca8d4eefa0a0df828ac5b822 = L.marker(
                [22.28018, 114.17165],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_3b33cde2d9834cdab44db989f8a1ae79 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_5ce0a692ca8d4eefa0a0df828ac5b822.setIcon(icon_3b33cde2d9834cdab44db989f8a1ae79);
        
    
        var popup_467fd5637e894f7a9f05d443fcb2d7ae = L.popup({"maxWidth": "100%"});

        
            var html_f6f4d23e398e489eb263306af35bfdd7 = $(`<div id="html_f6f4d23e398e489eb263306af35bfdd7" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_wanchai.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Hong Kong, CHINA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;02:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;17.44°C   /   63.39°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_467fd5637e894f7a9f05d443fcb2d7ae.setContent(html_f6f4d23e398e489eb263306af35bfdd7);
        

        marker_5ce0a692ca8d4eefa0a0df828ac5b822.bindPopup(popup_467fd5637e894f7a9f05d443fcb2d7ae)
        ;

        
    
    
            marker_5ce0a692ca8d4eefa0a0df828ac5b822.bindTooltip(
                `<div>
                     Hong Kong
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_857f7b30b6ef43b28d70d3f57a46b19c = L.marker(
                [31.246027, 121.483385],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_cc687d577dd44ee9b49287b6039a22a7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_857f7b30b6ef43b28d70d3f57a46b19c.setIcon(icon_cc687d577dd44ee9b49287b6039a22a7);
        
    
        var popup_18ae5a6b91a44905bb168dba4997fcd8 = L.popup({"maxWidth": "100%"});

        
            var html_cd93a104ef1c44fb9eb8c1e14155c6a5 = $(`<div id="html_cd93a104ef1c44fb9eb8c1e14155c6a5" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_shanghai.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Shanghai, CHINA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;02:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;4.2°C   /   39.56°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_18ae5a6b91a44905bb168dba4997fcd8.setContent(html_cd93a104ef1c44fb9eb8c1e14155c6a5);
        

        marker_857f7b30b6ef43b28d70d3f57a46b19c.bindPopup(popup_18ae5a6b91a44905bb168dba4997fcd8)
        ;

        
    
    
            marker_857f7b30b6ef43b28d70d3f57a46b19c.bindTooltip(
                `<div>
                     Shanghai
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_45dac7fa59204dd98ae43742e43d6358 = L.marker(
                [25.04652, 121.46538],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_ab6aef5645ef4012b12046328e8e38d5 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_45dac7fa59204dd98ae43742e43d6358.setIcon(icon_ab6aef5645ef4012b12046328e8e38d5);
        
    
        var popup_0913bf5176ac4ebb983b9690e725251f = L.popup({"maxWidth": "100%"});

        
            var html_8f18cf33301b4677b40ca4d5ea06f9eb = $(`<div id="html_8f18cf33301b4677b40ca4d5ea06f9eb" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_guangzhou.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Guangzhou, CHINA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;02:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;14.58°C   /   58.24°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_0913bf5176ac4ebb983b9690e725251f.setContent(html_8f18cf33301b4677b40ca4d5ea06f9eb);
        

        marker_45dac7fa59204dd98ae43742e43d6358.bindPopup(popup_0913bf5176ac4ebb983b9690e725251f)
        ;

        
    
    
            marker_45dac7fa59204dd98ae43742e43d6358.bindTooltip(
                `<div>
                     Guangzhou
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_90c75e1322004cf28e3f425a8625ffc6 = L.marker(
                [-6.17511, 106.865036],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_0d373cbbb3ce444d9c77ac725268724e = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_90c75e1322004cf28e3f425a8625ffc6.setIcon(icon_0d373cbbb3ce444d9c77ac725268724e);
        
    
        var popup_a2a8b4d998fa4d5ba72bb882b81135ee = L.popup({"maxWidth": "100%"});

        
            var html_629d4370592142b1ba15d5fdb87038d7 = $(`<div id="html_629d4370592142b1ba15d5fdb87038d7" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_indonesia.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Jakarta, INDONESIA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;01:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;26.08°C   /   78.94°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_a2a8b4d998fa4d5ba72bb882b81135ee.setContent(html_629d4370592142b1ba15d5fdb87038d7);
        

        marker_90c75e1322004cf28e3f425a8625ffc6.bindPopup(popup_a2a8b4d998fa4d5ba72bb882b81135ee)
        ;

        
    
    
            marker_90c75e1322004cf28e3f425a8625ffc6.bindTooltip(
                `<div>
                     Jakarta
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_f91d30930f95433a944fe3ae69848998 = L.marker(
                [35.443707, 139.638031],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_944f386b9d1d4aeba52a9a6131b38160 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_f91d30930f95433a944fe3ae69848998.setIcon(icon_944f386b9d1d4aeba52a9a6131b38160);
        
    
        var popup_9d2c9358f359422f846261bd3527ad7a = L.popup({"maxWidth": "100%"});

        
            var html_bad199f277a6407899fad8b9b2a63ec7 = $(`<div id="html_bad199f277a6407899fad8b9b2a63ec7" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_yokohama.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Yokohama, JAPAN</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;03:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;5.31°C   /   41.56°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_9d2c9358f359422f846261bd3527ad7a.setContent(html_bad199f277a6407899fad8b9b2a63ec7);
        

        marker_f91d30930f95433a944fe3ae69848998.bindPopup(popup_9d2c9358f359422f846261bd3527ad7a)
        ;

        
    
    
            marker_f91d30930f95433a944fe3ae69848998.bindTooltip(
                `<div>
                     Yokohama
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_06c4bb48f9ee410d9090294fce70faa9 = L.marker(
                [37.566536, 126.977966],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_ccd2ad72b2934909a79d81ef5a7124c7 = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_06c4bb48f9ee410d9090294fce70faa9.setIcon(icon_ccd2ad72b2934909a79d81ef5a7124c7);
        
    
        var popup_38f2cd3cab4b46e4acf9a6e05d05ccf7 = L.popup({"maxWidth": "100%"});

        
            var html_eb521fadf7b94b128573843f48db90ce = $(`<div id="html_eb521fadf7b94b128573843f48db90ce" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_seoul.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Seoul, SOUTH KOREA</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;03:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;-3.97°C   /   24.85°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_38f2cd3cab4b46e4acf9a6e05d05ccf7.setContent(html_eb521fadf7b94b128573843f48db90ce);
        

        marker_06c4bb48f9ee410d9090294fce70faa9.bindPopup(popup_38f2cd3cab4b46e4acf9a6e05d05ccf7)
        ;

        
    
    
            marker_06c4bb48f9ee410d9090294fce70faa9.bindTooltip(
                `<div>
                     Seoul
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_37c501aeac084e6f9f0d4ccd8a642ae4 = L.marker(
                [23.697809, 120.960518],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_e8c356ffb03548acb4c49328c446146a = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_37c501aeac084e6f9f0d4ccd8a642ae4.setIcon(icon_e8c356ffb03548acb4c49328c446146a);
        
    
        var popup_650712712ade4b3696312be2036092e9 = L.popup({"maxWidth": "100%"});

        
            var html_fc7e16635f184fc5b69303dc3b856e4c = $(`<div id="html_fc7e16635f184fc5b69303dc3b856e4c" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_taiwan.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Taipei, TAIWAN</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;02:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;14.6°C   /   58.28°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_650712712ade4b3696312be2036092e9.setContent(html_fc7e16635f184fc5b69303dc3b856e4c);
        

        marker_37c501aeac084e6f9f0d4ccd8a642ae4.bindPopup(popup_650712712ade4b3696312be2036092e9)
        ;

        
    
    
            marker_37c501aeac084e6f9f0d4ccd8a642ae4.bindTooltip(
                `<div>
                     Taipei
                 </div>`,
                {"sticky": true}
            );
        
    
            var marker_bb04632214bf48a095349fe4e9b3f228 = L.marker(
                [1.352083, 103.819839],
                {}
            ).addTo(feature_group_5cc3dfbb7f2345849fddc413e9db3545);
        
    
            var icon_1703f9dc5513498f9a44e76398af110c = L.AwesomeMarkers.icon(
                {"extraClasses": "fa-rotate-0", "icon": "map-marker", "iconColor": "white", "markerColor": "red", "prefix": "fa"}
            );
            marker_bb04632214bf48a095349fe4e9b3f228.setIcon(icon_1703f9dc5513498f9a44e76398af110c);
        
    
        var popup_05bb5e90b6714df2baa62f0194e7aad0 = L.popup({"maxWidth": "100%"});

        
            var html_05ffad719f474decad56742b00c2a518 = $(`<div id="html_05ffad719f474decad56742b00c2a518" style="width: 100.0%; height: 100.0%;"> <body> <img src=https://www.aveva.com/-/media/RedesignV2/English/Pages-Template/Contact/Worldwide-Offices/Office-Images/aveva_office_singapore.jpg width="220" height="140"> </body> <h4 style="color: #2e6c80"><span style="color: #000000;"><strong>Hougang, SINGAPORE</strong></span></h2> <table style="width: 225px;" cellpadding="0"> <tbody>  <tr> <td style="width: 109px;"><strong>Time&nbsp;</strong></td> <td style="width: 181px;">&nbsp;02:54</td> </tr>  <tr> <td style="width: 109px;"><strong>Date&nbsp;</strong></td> <td style="width: 181px;">&nbsp;Monday, 01/13/20</td> </tr>  <tr> <td style="width: 109px;"><strong>Temperature&nbsp;</strong></td> <td style="width: 181px;">&nbsp;1.67°C   /   35.01°F</td> </tr>  <tr> <td style="width: 109px;"><strong>Compliance&nbsp;</strong></td> <td style="width: 181px;">&nbsp;McAfee Version = 5.6.2</td> </tr>  <tr> <td style="width: 109px;"><strong>Contacts&nbsp;</strong></td> <td style="width: 181px;">&nbsp;exec@email.com <br> (555-555-5555)</td> </tr>  </tbody> </table> </div>`)[0];
            popup_05bb5e90b6714df2baa62f0194e7aad0.setContent(html_05ffad719f474decad56742b00c2a518);
        

        marker_bb04632214bf48a095349fe4e9b3f228.bindPopup(popup_05bb5e90b6714df2baa62f0194e7aad0)
        ;

        
    
    
            marker_bb04632214bf48a095349fe4e9b3f228.bindTooltip(
                `<div>
                     Hougang
                 </div>`,
                {"sticky": true}
            );
        
    
            var layer_control_ff044a2826254f35b243d4b1e23c7063 = {
                base_layers : {
                    "openstreetmap" : tile_layer_761d9851b2964eb5a81c990cfc24f15e,
                },
                overlays :  {
                    "NAM" : feature_group_25ef0eed750248cea3908f2b268793db,
                    "EMEA" : feature_group_dc449d8be7ba4dd3b4a4a712bd7aab8d,
                    "APA" : feature_group_5cc3dfbb7f2345849fddc413e9db3545,
                },
            };
            L.control.layers(
                layer_control_ff044a2826254f35b243d4b1e23c7063.base_layers,
                layer_control_ff044a2826254f35b243d4b1e23c7063.overlays,
                {"autoZIndex": true, "collapsed": true, "position": "topright"}
            ).addTo(map_3f1e88876c28404ebe016265acb234f0);
        
</script>

## Libraries
* [**Folium**](https://python-visualization.github.io/folium/) to create the map, markers, and interactivity.
* [**PyOWM**](https://pyowm.readthedocs.io/en/latest/) for interacting with the OpenWeatherMap API
* [**PyTz**](http://pytz.sourceforge.net/) for querying TimeZone database
