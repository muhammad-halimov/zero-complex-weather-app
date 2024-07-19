# import requests
# import json
#
# city = str(input())
#
# API_KEY = "Z5GWD253FDL5HJJMXJ6H94XFE"
#
# result = requests.get(f'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{city}/last7days?unitGroup=metric&key={API_KEY}&include=days&elements=datetime,temp,tempmax,tempmin,feelslike')
#
# if result.status_code == 200:
#     data = result.json()
#     with open("result.json", "w+", encoding="UTF8") as file:
#         json.dump(data, file, indent=4)
#     print("Succesfully written.")
# else:
#     print(f"Error: {result.status_code} - {result.text}")
#
# with open("result.json", "r") as file:
#     json_data = file.read()
#
# data = json.loads(json_data)
#
# # # Accessing the values for a specific day
# # print(data['days'][0]['datetime'])  # Output: '2024-07-03'
# # print(data['days'][0]['tempmax'])   # Output: 29.9
# # print(data['days'][0]['tempmin'])   # Output: 16.6
# # print(data['days'][0]['temp'])      # Output: 23.7
# # print(data['days'][0]['feelslike']) # Output: 24.1
#
#
# for i in range(0, len(data['days'])):
#     # Accessing the values for a specific day
#     print("Day", data['days'][i]['datetime'])                 # Output: '2024-07-03'
#     print("Max temp:", data['days'][i]['tempmax'])            # Output: 29.9
#     print("Min temp:", data['days'][i]['tempmin'])            # Output: 16.6
#     print("Avg temp:", data['days'][i]['temp'])               # Output: 23.7
#     print("Feels Like:", data['days'][i]['feelslike'], "\n")  # Output: 24.1


# with open("../../../last_city.csv", "r+", encoding="UTF8") as file:
#     last_cities: list = list("".join(file.readlines()).split("\n"))
#     print(last_cities)

try:
    with open('../../../last_city.csv', 'r', encoding='utf-8') as file:
        lines = file.readlines()

        cities = []

        for line in lines:
            city = line.strip('\n')
            cities.append(city)

        # Print all cities at once
        print(cities)

except FileNotFoundError:
    print([])
    