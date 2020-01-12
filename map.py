import pyowm
from locations import locations
from folium import FeatureGroup, LayerControl, Map, Marker, Icon, GeoJson, Figure
from datetime import datetime
from pytz import timezone
from folium.plugins import Search, MousePosition


API_KEY = 'SANITIZED'
owm = pyowm.OWM(API_KEY)

m = Map(
    max_bounds=True,
    location=[45.372, -121.6972],
    zoom_start=3,
    min_zoom=2,
    min_lat = -190,
    max_lat = 190,
    min_lon = -50,
    max_lon = 75)

nam_group = FeatureGroup(name='NAM')
emea_group = FeatureGroup(name='EMEA')
asia_group = FeatureGroup(name='APA')


formatter = "function(num) {return L.Util.formatNum(num, 3) + ' º ';};"

MousePosition(
    position='topright',
    separator=' | ',
    empty_string='',
    lng_first=True,
    num_digits=20,
    prefix='Coordinates:',
    lat_formatter=formatter,
    lng_formatter=formatter,
).add_to(m)


def get_date(timezone):
    date = datetime.now(timezone)
    return date.strftime("%A, %D")


def get_time(timezone):
    time = datetime.now(timezone)
    return time.strftime("%H:%M")


def get_temp(location): # -> (celsius, fahr)
    observation = owm.weather_at_place(location)
    w = observation.get_weather()
    return (w.get_temperature('celsius')['temp'], w.get_temperature('fahrenheit')['temp'])


def format_html(location, time, date, temp_c, temp_f, info, image):
    return f"""
<body> <img src={image} width="200" height="150"> </body>
<h4 style="color: #2e6c80"><span style="color: #000000;"><strong>{location}</strong></span></h2>
<table style="width: 225px;" cellpadding="0">
<tbody>

<tr>
<td style="width: 109px;"><strong>Time&nbsp;</strong></td>
<td style="width: 181px;">&nbsp;{time}</td>
</tr>

<tr>
<td style="width: 109px;"><strong>Date&nbsp;</strong></td>
<td style="width: 181px;">&nbsp;{date}</td>
</tr>

<tr>
<td style="width: 109px;"><strong>Temperature&nbsp;</strong></td>
<td style="width: 181px;">&nbsp;{temp_c}°C   |   {temp_f}°F</td>
</tr>

<tr>
<td style="width: 109px;"><strong>Network Speed&nbsp;</strong></td>
<td style="width: 181px;">&nbsp;{info}</td>
</tr>

<tr>
<td style="width: 109px;"><strong>Contacts&nbsp;</strong></td>
<td style="width: 181px;">&nbsp;{info}</td>
</tr>

</tbody>
</table>
"""


def add_marker(html, group, tooltip):
    if group == 'NAM':
        Marker(location=coords, popup=html, tooltip=tooltip, icon=Icon(color='green', icon='map-marker', prefix='fa')).add_to(nam_group)
    elif group == 'EMEA':
        Marker(location=coords, popup=html, tooltip=tooltip, icon=Icon(color='purple', icon='map-marker', prefix='fa')).add_to(emea_group)
    elif group == 'APA':
        Marker(location=coords, popup=html, tooltip=tooltip, icon=Icon(color='red', icon='map-marker', prefix='fa')).add_to(asia_group)



for loc in locations:
    coords, region, tz, info, image = locations[loc][0], locations[loc][1], locations[loc][2], locations[loc][3], locations[loc][4]
    tooltip = loc.split(',')[0]
    time = get_time(timezone(tz))
    date = get_date(timezone(tz))
    temp = get_temp(tooltip)
    temp_c, temp_f = temp[0],temp[1]
    html = format_html(loc, time, date, temp_c, temp_f, info, image)


    add_marker(html, region, tooltip)


nam_group.add_to(m)
emea_group.add_to(m)
asia_group.add_to(m)

LayerControl().add_to(m)

m.save('corporate_map.html')