import requests
import json
import asyncio
import websockets

Exit = False
while Exit == False :
    print ("---------------------------------------------------------")
    print ("Welcome! ")
    print ("A. Leagues Standing")
    print ("B. Players")
    print ("C. Results ")
    print ("E. Exit ")
    user_input = input ("Please Choose an option (A , B , C , E) : ")

    if user_input == "e" or user_input == "E" :
        user_input == input("Do You Want To Close Program ? Y. Yes N. No :")
        if user_input == "y" or user_input == "y" :
            print("Program Closed! Have a Nice Day!")
            Exit == True
        break

    elif user_input == "a" or user_input == "A":
        print ("A. Spain")
        print ("B. England")
        print ("C. Itally")
        user_input = input ("Pls Choose a Option (A , B , C) : ")
        if user_input ==  "A" or user_input == "a":

            laliga_url = "https://apiv3.apifootball.com/?action=get_standings&league_id=302&APIkey=6498a30fee58cfd2d3bcece08eeab77a25bd3cc54f2e5a4da2ee30316f796ce8"
            laliga_response = requests.get(laliga_url)

            if laliga_response.status_code == 200:
                laliga_data = laliga_response.json()

                sorted_teams = sorted(laliga_data, key=lambda x: x.get('points', 0), reverse=True)

                print("La Liga Standings :")
                for index, team in enumerate(sorted_teams, start=1):
                    team_name = team['team_name']
                    position = index
                    print(f"Position: {position}, Team {team_name}")

            else:
                print("Error: ", laliga_response.status_code)
            

    elif user_input == "b" or user_input =="B" :
        print ("A. Antoine Griezmann")
        print ("B. Benzema")
        print ("C. Lionel Messi")
        user_input = input ("Pls Choose a Player (A , B , C) : ")
        if user_input == "A" or user_input == "a" :
            players_url = ("https://apiv3.apifootball.com/?action=get_players&player_name=Griezmann&APIkey=6498a30fee58cfd2d3bcece08eeab77a25bd3cc54f2e5a4da2ee30316f796ce8")
            players_response = requests.get(players_url)

            if players_response.status_code == 200:
                players_data = players_response.json()
                if isinstance(players_data, list):
                    sorted_players = sorted(players_data, key=lambda x: (x.get('player_name', ''), x.get('age', 31)))
                    print ("Player Info :")
                
                    for index, player in enumerate(sorted_players, start=1):
                        player_name = player.get ("player_name" , "")
                        player_type = player.get("player_type" , "")
                        player_age  = player.get("player_age" , 31)
                        team_name   = player.get("team_name" , "")
                        plaer_rating = player.get("player_rating" , "9/1")

                        print (f"Name: {player_name} , Type : {player_type} , Age :{player_age} , Team : {team_name} , Rate : {plaer_rating}  ")
                else :
                    print("Error: Invalid data format from API.")
            else:
                print("Error: ", player_response.status_code)        

    elif user_input == "C" or user_input == "c" :
        print ("A. Laliga Last 2 Matches")
        print ("B. Premier Leauge Last 2 Matches")
        print ("C. SerieA Last 2 Matches ")
        user_input = input ("Pls Choose a Player (A , B , C) : ")
        if user_input == "B" or user_input == "b" :
        
            results_url = ("https://apiv3.apifootball.com/?action=get_events&from=2023-04-05&to=2023-04-05&league_id=152&APIkey=6498a30fee58cfd2d3bcece08eeab77a25bd3cc54f2e5a4da2ee30316f796ce8")
            results_response = requests.get(results_url)

            if results_response.status_code == 200 :
                results_data = results_response.json()

                sorted_results = sorted(results_data, key=lambda x: (x.get('match_hometeam_name', ''), x.get('match_awayteam_name', ''), x.get('match_hometeam_score', 0) + x.get('match_awayteam_score', 0)), reverse=True)
                print ("Matches Results :")

                for result in sorted_results:
                    match_hometeam_name = result.get('match_hometeam_name', '')
                    match_awayteam_name = result.get('match_awayteam_name', '')
                    match_hometeam_score = result.get('match_hometeam_score', 0)
                    match_awayteam_score = result.get('match_awayteam_score', 0)
                    print(f"Team Home: {match_hometeam_name}, Team Away: {match_awayteam_name}, Goals Home: {match_hometeam_score}, Goals Away: {match_awayteam_score}")
            
            else:
                print("Error: ", response.status_code)        

    

    else :
        print("invaild Command...")    