def describe_city(city, country='UAE'):
    """Describe a city."""
    msg = city.title() + " is in " + country.title() + "."
    print(msg)

describe_city('Abu Dhabi')
describe_city('Ajman')
describe_city('Dubai')