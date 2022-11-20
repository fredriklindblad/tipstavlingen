import pandas as pd
import shutil
import os

def get_pivot():
    # Läser in och skapar df av csv-filer
    xls = pd.ExcelFile('tipsen.xlsm')
    users_tb = pd.read_excel(xls, 'users')
    leagues_tb = pd.read_excel(xls, 'leagues')
    teams_tb = pd.read_excel(xls, 'teams')
    tips_as_tb = pd.read_excel(xls, 'tips_as')

    print(users_tb)
    print(leagues_tb)
    print(teams_tb)
    print(tips_as_tb)

    merged_tips = pd.merge(teams_tb, tips_as_tb, on='team_id')
    merged_tips = pd.merge(users_tb, merged_tips, on='user_id')
    merged_tips = pd.merge(leagues_tb, merged_tips, on='league_id')

    #TO DO - Webscrape league tables
    #TO DO - Add difference column

    print(merged_tips)

    pivot = pd.pivot_table(merged_tips, values='position', index='team_name', columns='first_name')

    result = pivot.to_html()
    # write html to file
    # path = "C:\Users\Fredrik\Documents\GitHub\tipstavlingen\templates\pivot.html"
    text_file = open(r"C:\Users\Fredrik\Documents\GitHub\tipstavlingen\templates\pivot.html", "w")
    text_file.write('<!doctype html>\n<html lang="en">\n' + result + '\n</html>')
    text_file.close()

    # print(result)

    return result

get_pivot()