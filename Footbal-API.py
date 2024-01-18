import requests
import json

exit = False

while exit == False :
    print ("A. Leagues Standing")
    print ("B. Players")
    print ("C. ")
    user_input = input ("Pls Choose a Option (A , B , C) or Exit : ")
    
    if user_input == "a" or user_input == "A":
        print ("A1. Spain")
        print ("B1. England")
        print ("C1. Itally")
        user_input = input ("Pls Choose a Option (A1 , B1 , C1) ")
        if user_input ==  "A1" or user_input == "a1":
            url = ("https://apiv3.apifootball.com/?action=get_standings&league_id=152&APIkey=6498a30fee58cfd2d3bcece08eeab77a25bd3cc54f2e5a4da2ee30316f796ce8")
            response = requests.get(url)

            print(response.json())

    





