### Лабораторная работа 3. Использование API openweathermap.org
***
#### Описание задачи
Написать реализацию функции get_weather_data(place, api_key=None) (в модуле getweatherdata), в которой необходимо получить данные о погоде с сайта https://openweathermap.org/.

Функция должна возвращать объект в формате JSON, включающий:

+ информацию о названии города (в контексте openweathermap),
+ код страны (2 символа),
+ широту и долготу, на которой он находится,
+ его временной зоне,
+ а также о значении температуры (как она ощущается).

Значение временной зоны выводить в формате UTC±N, где N - цифра временного сдвига. Протестировать выполнение программы со следующими городами: Чикаго, СПб, Дакка.

Пример вызова функции и получаемого результата.

```python
get_weather_data('Kiev', api_key=key)
>>> {"name": "Kyiv", "coord": {"lon": 30.52, "lat": 50.43}, "country": "UA", "feels_like": 21.96, "timezone": "UTC+3"}
```

```python
def get_weather_data(place, api_key=None):
  with request.urlopen(
      f'https://api.openweathermap.org/data/2.5/weather?q={place}&appid={api_key}'
  ) as f:
    res = f.read().decode('utf-8')
    res_obj = json.loads(res)
    #print(res_obj)

    for id in res_obj:
      if id == 'name':
        res_dict['name'] = res_obj[id]
      if id == 'coord':
        res_dict['coord'] = res_obj[id]
      if id == 'timezone':
        res_dict['timezone'] = str(timezone(timedelta(seconds=res_obj[id])))
      if id == 'sys':
        for elem in res_obj[id]:
          if elem == 'country':
            res_dict['country'] = res_obj[id][elem]
      if id == 'main':
        for elem in res_obj[id]:
          if elem == 'feels_like':
            res_dict['feels_like'] = round(res_obj[id][elem] - 273.15, 2)
    #print(res_dict)
    #print(res_obj)

  print(json.dumps(res_dict))
  with open('result.json', 'w') as f:
    json.dump(res_dict, f, ensure_ascii=False, indent=4)
  ```
