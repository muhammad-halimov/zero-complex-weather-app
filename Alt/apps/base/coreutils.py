import requests
import json


def write_to_json(city: str) -> str:
    api_key = "Z5GWD253FDL5HJJMXJ6H94XFE"
    url = f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/last6days?unitGroup=metric&key={api_key}&include=days&elements=datetime,temp,tempmax,tempmin,feelslike'
    result = requests.get(url=url)

    if result.status_code == 200:
        data = result.json()
        with open("result.json", "w+", encoding="UTF8") as file:
            json.dump(data, file, indent=4)
        return "Succesfully written."
    else:
        return f"Error: {result.status_code} - {result.text}"


def read_from_json() -> list:
    try:
        with open("result.json", "r", encoding="UTF8") as file:
            json_data = file.read()

        data = json.loads(json_data)
        inner_array: list = list()
        outer_array: list = list()

        for i in range(0, len(data['days'])):
            # Accessing the values for a specific day
            inner_array.append('.'.join(data['days'][i]['datetime'].split('-')))
            inner_array.append(round(data['days'][i]['tempmax']))
            inner_array.append(round(data['days'][i]['tempmin']))
            inner_array.append(round(data['days'][i]['temp']))
            inner_array.append(round(data['days'][i]['feelslike']))
            inner_array.append(data['resolvedAddress'])
            outer_array.append(inner_array)
            inner_array = list()  # reset inner_array for the next iteration

        return outer_array
    except FileNotFoundError:
        # If the file doesn't exist, return an empty list
        return list()
