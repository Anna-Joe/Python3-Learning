def formatted_city_country(city,country,population=0):

    if population!=0:
        formatted_string=city.title()+','+country.title()+' - population '+str(population)
    else:
        formatted_string=city.title()+','+country.title()

    return formatted_string
