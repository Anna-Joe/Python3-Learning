import json
import pygal
from pygal.style import RotateStyle
from country_code import get_country_code

filename="population_data.json"
chart_info={}
with open(filename) as f:
    pop_data=json.load(f)

for pop_dict in pop_data:
    if pop_dict['Year']==2016:
        country_name=pop_dict['Country Name']
        code=get_country_code(country_name)
        population=pop_dict['Value']
        if code:
            chart_info[code]=population

cp1,cp2,cp3={},{},{}
for country_code,population in chart_info.items():
    if population<10000000:
        cp1[country_code]=population
    elif population<100000000:
        cp2[country_code]=population
    else:
        cp3[country_code]=population


wmc_style=RotateStyle('#336699')
world_map_chart=pygal.maps.world.World(style=wmc_style)
world_map_chart.title="World Population in 2016"
world_map_chart.add('0-10m',cp1)
world_map_chart.add('10m-1bn',cp2)
world_map_chart.add('>1bn',cp3)
world_map_chart.render_to_file('world_population.svg')

