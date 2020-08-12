from selenium import webdriver
from pprint import pprint
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import requests


def estimatedtotal():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2019-20&SeasonType=Regular%20Season&DateFrom=07%2F31%2F2020&DateTo=07%2F01%2F2021')
    soup = BeautifulSoup(driver.page_source, 'html.parser').find('div', {'class':'nba-stat-table__overflow'})

    headers, [_, *data] = [i.text for i in soup.find_all('th')], [[i.text for i in b.find_all('td')] for b in soup.find_all('tr')]
    final_data = [i for i in data if len(i) > 1]
    data_attrs = [dict(zip(headers, i)) for i in final_data]
    team = [i['TEAM'] for i in data_attrs]
    stripedteam = []

    for element in team:
        stripedteam.append(element.strip())

    points = [i['PTS'] for i in data_attrs]
    global result
    result = dict(zip(stripedteam, points))
    newresult = dict((k,float(v)) for k,v in result.items())
    driver.quit()
    return newresult

newresult = estimatedtotal()

def estimated1stquarter():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2019-20&SeasonType=Regular%20Season&DateFrom=07%2F31%2F2020&DateTo=07%2F01%2F2021&Period=1')
    soup = BeautifulSoup(driver.page_source, 'html.parser').find('div', {'class':'nba-stat-table__overflow'})

    headers, [_, *data] = [i.text for i in soup.find_all('th')], [[i.text for i in b.find_all('td')] for b in soup.find_all('tr')]
    final_data = [i for i in data if len(i) > 1]
    data_attrs = [dict(zip(headers, i)) for i in final_data]
    team = [i['TEAM'] for i in data_attrs]
    stripedteam = []

    for element in team:
        stripedteam.append(element.strip())

    points = [i['PTS'] for i in data_attrs]
    global result
    result = dict(zip(stripedteam, points))
    result1stquarter = dict((k,float(v)) for k,v in result.items())
    driver.quit()
    return result1stquarter

result1stquarter = estimated1stquarter()

def estimated2ndquarter():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2019-20&SeasonType=Regular%20Season&DateFrom=07%2F31%2F2020&DateTo=07%2F01%2F2021&Period=2')
    soup = BeautifulSoup(driver.page_source, 'html.parser').find('div', {'class':'nba-stat-table__overflow'})

    headers, [_, *data] = [i.text for i in soup.find_all('th')], [[i.text for i in b.find_all('td')] for b in soup.find_all('tr')]
    final_data = [i for i in data if len(i) > 1]
    data_attrs = [dict(zip(headers, i)) for i in final_data]
    team = [i['TEAM'] for i in data_attrs]
    stripedteam = []

    for element in team:
        stripedteam.append(element.strip())

    points = [i['PTS'] for i in data_attrs]
    global result
    result = dict(zip(stripedteam, points))
    result2ndquarter = dict((k,float(v)) for k,v in result.items())
    driver.quit()
    return result2ndquarter

result2ndquarter = estimated2ndquarter()

def estimated3rdquarter():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2019-20&SeasonType=Regular%20Season&DateFrom=07%2F31%2F2020&DateTo=07%2F01%2F2021&Period=3')
    soup = BeautifulSoup(driver.page_source, 'html.parser').find('div', {'class':'nba-stat-table__overflow'})

    headers, [_, *data] = [i.text for i in soup.find_all('th')], [[i.text for i in b.find_all('td')] for b in soup.find_all('tr')]
    final_data = [i for i in data if len(i) > 1]
    data_attrs = [dict(zip(headers, i)) for i in final_data]
    team = [i['TEAM'] for i in data_attrs]
    stripedteam = []

    for element in team:
        stripedteam.append(element.strip())

    points = [i['PTS'] for i in data_attrs]
    global result
    result = dict(zip(stripedteam, points))
    result3rdquarter = dict((k,float(v)) for k,v in result.items())
    driver.quit()
    return result3rdquarter

result3rdquarter = estimated3rdquarter()

def estimated4thquarter():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://stats.nba.com/teams/traditional/?sort=W_PCT&dir=-1&Season=2019-20&SeasonType=Regular%20Season&DateFrom=07%2F31%2F2020&DateTo=07%2F01%2F2021&Period=4')
    soup = BeautifulSoup(driver.page_source, 'html.parser').find('div', {'class':'nba-stat-table__overflow'})

    headers, [_, *data] = [i.text for i in soup.find_all('th')], [[i.text for i in b.find_all('td')] for b in soup.find_all('tr')]
    final_data = [i for i in data if len(i) > 1]
    data_attrs = [dict(zip(headers, i)) for i in final_data]
    team = [i['TEAM'] for i in data_attrs]
    stripedteam = []

    for element in team:
        stripedteam.append(element.strip())

    points = [i['PTS'] for i in data_attrs]
    global result
    result = dict(zip(stripedteam, points))
    result4thquarter = dict((k,float(v)) for k,v in result.items())
    driver.quit()
    return result4thquarter

result4thquarter = estimated4thquarter()

def userInput():
    team1 = input('Team 1: ')
    team2 = input('Team 2: ')
    return team1, team2

team1, team2 = userInput()

def totalaverage(team1, team2):
    if team1 and team2 in newresult:
        total = newresult[team1] + newresult[team2]
        return total

def total1stquarter(team1, team2):
    if team1 and team2 in result1stquarter:
        total = result1stquarter[team1] + result1stquarter[team2]
        return total

def total2ndquarter(team1, team2):
    if team1 and team2 in result2ndquarter:
        total = result2ndquarter[team1] + result2ndquarter[team2]
        return total

def total3rdquarter(team1, team2):
    if team1 and team2 in result3rdquarter:
        total = result3rdquarter[team1] + result3rdquarter[team2]
        return total

def total4thquarter(team1, team2):
    if team1 and team2 in result4thquarter:
        total = result4thquarter[team1] + result4thquarter[team2]
        return total

print('Total: ' + str(totalaverage(team1, team2)))
print('1st Quarter: ' + str(total1stquarter(team1, team2)))
print('2nd Quarter: ' + str(total2ndquarter(team1, team2)))
print('3rd Quarter: ' + str(total3rdquarter(team1, team2)))
print('4th Quarter: ' + str(total4thquarter(team1, team2)))