travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    }
]

#To write a function that will allow new country
#new country to be added to the travel_log
def add_new_country(countries,times_visited, cities_visited):
    empty_dict={}
    empty_dict["country"] = countries
    empty_dict["visits"] = times_visited
    empty_dict["cities"] = cities_visited
    travel_log.append(empty_dict)

add_new_country("Russia", 2, ["Moscow", "Saint Petersbu"])
print(travel_log)
