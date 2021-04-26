import requests
import json
import ast
import itertools

'''
覺得酷的事情 server回傳的資料型態是 byte而不是str
starwar有自己的api 可以拉請求, 但我安裝套件有問題可能是我mac的版本問題
網站上的星際大戰只有更新到第六部，但實際上應該有9部🤨
官方有提供 wookie 可以將server傳的bytes 轉為json, 但我發現目前狀態是disabled的
第三題內 Emergency Firespeeder 大部分資料都是unknown(包含馬力)
'''


try:
    # This function is to convert the data type from bytes to dictionary
    def byte_to_dic_converter(byte_content):
        dic_content = ""
        str_content = byte_content.decode("utf-8")
        dic_content = ast.literal_eval(str_content)
        return dic_content

    the_six_film = requests.get("https://swapi.dev/api/films/6")
    the_six_film_dic = byte_to_dic_converter(the_six_film.content)
    print("總共有:", len(the_six_film_dic['species']), "個不同種族的人出現在電影中")

    # List films name, ascending

    vehicles_in_films = []
    for i in range(1, 7):
        all_films = requests.get("https://swapi.dev/api/films/"+str(i))
        all_films_dic = byte_to_dic_converter(all_films.content)
        print("第", i, "集:", all_films_dic['title'])
        vehicles_in_films.append(all_films_dic['vehicles'])

    # Handle api list that to avoid the duplication.
    dup_vehicles_list = (
        list(itertools.chain.from_iterable(vehicles_in_films)))
    unique_vehicles_set = set(dup_vehicles_list)
    unique_vehicles_list = list(unique_vehicles_set)

    # The vehicles that hp over 1,000 would be stored into list.
    hp_over_1000 = []

    for x in unique_vehicles_list:
        r3 = requests.get(x)
        dict_all_vehicles = byte_to_dic_converter(r3.content)
        try:
            if int(dict_all_vehicles['max_atmosphering_speed']) > 1000:
                hp_over_1000.append(dict_all_vehicles['name'])
        except:
            print("There's an exception can not be processed,vehicle name:",
                  dict_all_vehicles['name'])

    print("馬力超過一千的車輛有:", hp_over_1000)
# Print error msg & error code for debugging
except Exception as e:
    print('Error! Code: {c}, Message, {m}'.format(
        c=type(e).__name__, m=str(e)))
