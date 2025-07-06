import pandas as pd
from bs4 import BeautifulSoup


with open('file_name.html', 'r', encoding='utf-8') as file:
    file_content = file.read()


soup = BeautifulSoup(file_content, 'html.parser')

data = []

for div in soup.find_all('div', class_='col-md-12 col-sm-12 main-bo-lis pad-top-bot ng-scope'):
    for dep_block in div.find_all('div',class_='col-md-2 col-sm-2 col-xs-4 top5'):
        for dep_time in dep_block.find_all('span',class_="txt-r2-n ng-binding"):
            depart_time = dep_time.text.strip()
        for dep_port in dep_block.find('span',class_='txt-r3-n ng-binding'):
            depart_port = dep_port.text.strip()
    for arv_block in div.find_all('div',class_="col-md-2 col-sm-2 col-xs-3 top5 txdir"):
        for arv_time in arv_block.find_all('span',class_='txt-r2-n ng-binding'):
            arv_time = arv_time.text.strip()
        for arv_port in arv_block.find_all('span',class_='txt-r3-n ng-binding'):
            arv_port = arv_port.text.strip()
    for price_block in div.find_all('div',class_="col-md-10 col-sm-8 col-xs-9 txt-r6-n exPrc 11"):
        for price in price_block.find_all('span',class_='ng-binding'):
            fare = price.text.strip()

    for time_stop_block in div.find_all('div',class_='col-md-2 col-sm-2 col-xs-5 non-st wd14c'):
        for durations_time in time_stop_block.find_all('span',class_='dura_md ng-binding'):
            duration_time = durations_time.text.strip()
        for durations_stop in time_stop_block.find_all('span',class_='dura_md2 ng-scope'):
            duration_stop = durations_stop.text.strip()
    for airline_info in div.find_all('div',class_='col-md-7 col-sm-7 padd-lft airl-txt-n'):
        for airline in airline_info.find_all('span',class_='txt-r4 ng-binding'):
            airline_name = airline.text.strip()
        for airline_codes_block in airline_info.find_all('span',class_='txt-r5'):
            for airline_codes in airline_codes_block.find_all('span', {'ng-bind': lambda x: x and '.AC' in x}):
                airline_code = airline_codes.text.strip()
            for flights_number in airline_codes_block.find_all('span', {'ng-bind' : lambda x:x and '.FN' in x}):
                flight_number = flights_number.text.strip()
        for cabins_class in airline_info.find_all('span',class_='txt-r5 ng-binding'):
            cabin_class = cabins_class.text.strip()

        for aircrafts_style in airline_info.find_all('span',class_="_plntyp ng-binding ng-scope"):
            aircraft_style = aircrafts_style.text.strip()
    for meal_block in div.select_one('div',class_='adodis_v4 ng-binding ng-scope'):
        meal = meal_block.text.strip()

    data.append({
        'Airline': airline_name,
        'Airline_Code': airline_code,
        'Flight_Number': flight_number,
        'Cabin_Class': cabin_class,
        'Aircraft_Type': aircraft_style,
        'Departure_Time': depart_time,
        'Departure_Port': dep_port,
        'Arrival_Time': arv_time,
        'Arrival_Port': arv_port,
        'Duration': duration_time,
        'Stop': duration_stop,
        'Fare': fare,
        'Meal': meal
    })

final_df = pd.DataFrame(data)
print(final_df)

final_df.to_csv('flights_.csv', index=False, encoding='utf-8')