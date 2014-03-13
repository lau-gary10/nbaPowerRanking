'''
Parse the html file and save the stat into csv file

#########################################################################
The MIT License (MIT)

Copyright (c) 2014 Gary Lau

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
#########################################################################
'''

import common_lib

class list_of_team_stats():
    listOfTeamStats = [['TEAM_NAME', 'WIN', 'LOSS', 'PCT', 'ROAD_WIN', 'HOME_LOSS']]

##############################
#class list_of_team_stats():
 #   listOfTeamStats = [['TEAM_NAME', 'WIN', 'LOSS', 'PCT', 'GAMES_BACK', 'CONFERENCE_WIN', 'CONFERENCE_LOSS', 'DIVISION_WIN', 'DIVISION_LOSS', 'HOME_WIN', 'HOME_LOSS', 'ROAD_WIN', 'ROAD_LOSS', 'LAST_10_WIN', 'LAST_10_LOSS', 'STREAK']]

def parse_td(data):
    startPos = data.find('<td>')
    endPos = data.__len__()
    data = data[startPos:endPos]

    startPos = data.find('>')
    endPos = data.find('</td>')
    varName = data[startPos:endPos]
    varName = varName.replace('>', '')

    startPos = endPos
    endPos = data.__len__()
    data = data[startPos:endPos]
    return varName, data

# Get the values from html file and append it to existing list
def parse_html_file(data):

    # Parsing through data.
    startPos = data.find('<td class="team">')
    endPos = data.__len__()
    data = data[startPos:endPos]

    startPos = data.find('<a href=')
    endPos = data.__len__()
    data = data[startPos:endPos]

    # Get team name
    startPos = data.find('/')
    endPos = data.find('>')
    teamName = data[startPos:endPos]
    teamName = teamName.replace('/', '')
    teamName = teamName.replace('"', '')

    startPos = endPos
    endPos = data.__len__()
    data = data[startPos:endPos]

    # Get number of wins
    curTuple = parse_td(data)
    data = curTuple[1]
    win = curTuple[0]

    # Get number of losses
    curTuple = parse_td(data)
    data = curTuple[1]
    loss = curTuple[0]

    # Get pct
    curTuple = parse_td(data)
    data = curTuple[1]
    pct = curTuple[0]

    # Get games back
    curTuple = parse_td(data)
    data = curTuple[1]
    gamesBack = curTuple[0]

    # Get conference win
    curTuple = parse_td(data)
    data = curTuple[1]
    conf = curTuple[0]
    startPos = 0
    endPos = conf.find('-')
    confWin = conf[startPos:endPos]

    # Get conference loss
    startPos = conf.find('-')
    endPos = conf.__len__()
    confLoss = conf[startPos:endPos]
    confLoss = confLoss.replace('-', '')

    # Get division win
    curTuple = parse_td(data)
    data = curTuple[1]
    divi = curTuple[0]
    startPos = 0
    endPos = divi.find('-')
    diviWin = divi[startPos:endPos]

    # Get division loss
    startPos = divi.find('-')
    endPos = divi.__len__()
    diviLoss = divi[startPos:endPos]
    diviLoss = diviLoss.replace('-', '')

    # Get home win
    curTuple = parse_td(data)
    data = curTuple[1]
    home = curTuple[0]
    startPos = 0
    endPos = home.find('-')
    homeWin = home[startPos:endPos]

    # Get home loss
    startPos = home.find('-')
    endPos = home.__len__()
    homeLoss = home[startPos:endPos]
    homeLoss = homeLoss.replace('-', '')

    # Get road win
    curTuple = parse_td(data)
    data = curTuple[1]
    road = curTuple[0]
    startPos = 0
    endPos = road.find('-')
    roadWin = road[startPos:endPos]

    # Get road loss
    startPos = road.find('-')
    endPos = road.__len__()
    roadLoss = road[startPos:endPos]
    roadLoss = roadLoss.replace('-', '')

    # Get last 10
    curTuple = parse_td(data)
    data = curTuple[1]
    lastTen = curTuple[0]
    startPos = 0
    endPos = lastTen.find('-')
    lastTenWin = lastTen[startPos:endPos]

    # Get road loss
    startPos = lastTen.find('-')
    endPos = lastTen.__len__()
    lastTenLoss = lastTen[startPos:endPos]
    lastTenLoss = lastTenLoss.replace('-', '')

    # Get streak
    curTuple = parse_td(data)
    data = curTuple[1]
    streak = curTuple[0]

    # Append data to list
    list_of_team_stats.listOfTeamStats.append([teamName, win, loss, pct, gamesBack, confWin, confLoss, diviWin, diviLoss, homeWin, homeLoss, roadWin, roadLoss, lastTenWin, lastTenLoss, streak])
    return data
##############################

# Cut off all other data except for the expanded standings
def get_all_expanded_standings(data):
    startPos = data.find('id="all_expanded-standings"')
    endPos = data.find('id="all_team-vs-team"')
    data = data[startPos:endPos]
    return data

def transitioning_through_parsing(data, endPos):
    startPos = endPos
    endPos = data.__len__()
    data = data[startPos:endPos]
    startPos = data.find('<td align="')
    endPos = data.__len__()
    data = data[startPos:endPos]
    return data

# Get the values from html file and append it to existing list
def parse_data_get_true_pct(data):
    startPos = data.find('<a href="/teams/')
    endPos = data.__len__()
    data = data[startPos:endPos]

    # Get TEAM_NAME
    startPos = data.find('>')
    endPos = data.find('</a>')
    teamName = data[startPos:endPos]
    teamName = teamName.replace('>', '')
    data = transitioning_through_parsing(data, endPos)

    # Get WIN and LOSS
    startPos = data.find('>')
    endPos = data.find('</td>')
    loss = data[startPos:endPos]
    loss = loss.replace('>', '')
    startPosA = 0
    endPosA = loss.find('-')
    win = loss[startPosA:endPosA]
    startPosA = endPosA
    endPosA = loss.__len__()
    loss = loss[startPosA:endPosA]
    loss = loss.replace('-','')
    data = transitioning_through_parsing(data, endPos)

    # Get PCT
    pct = float(win) / ( float(win) + float(loss) )
    pct = str(pct)

    # Get HOME_LOSS
    startPos = data.find('>')
    endPos = data.find('</td>')
    homeLoss = data[startPos:endPos]
    startPosA = homeLoss.find('-')
    endPosA = homeLoss.__len__()
    homeLoss = homeLoss[startPosA:endPosA]
    homeLoss = homeLoss.replace('-', '')
    data = transitioning_through_parsing(data, endPos)

    # Get ROAD_WIN
    startPos = data.find('>')
    endPos = data.find('</td>')
    roadWin = data[startPos:endPos]
    startPosA = 0
    endPosA = roadWin.find('-')
    roadWin = roadWin[startPosA:endPosA]
    roadWin = roadWin.replace('>', '')

    # Append data to list
    list_of_team_stats.listOfTeamStats.append([teamName, win, loss, pct, roadWin, homeLoss])
    return data

def start_main():
    data = common_lib.open_file(common_lib.NBA_STANDING_HTML_FILE)
    data = get_all_expanded_standings(data)

    while data.find('<a href="/teams/') > 0:
        data = parse_data_get_true_pct(data)

#########################
#    while data.find('<td class="team">') > 0:
 #       data = parse_html_file(data)
#########################

    thisList = common_lib.convert_list_into_str(list_of_team_stats.listOfTeamStats)
    common_lib.write_file(thisList, common_lib.NBA_STANDING_CSV_FILE)

# Prints the run time of this program
def actual_run_time():
    def new_function():
        start_main()
    from timeit import timeit
    numSec = timeit(new_function, number=1)
    from datetime import timedelta
    seconds = timedelta(seconds=float(numSec))
    name = common_lib.module_name() + '.py'
    print('Actual run time on ' + name + ':', seconds)

def main():
    actual_run_time()

main()