'''
Checks if the best team of the true power ranking is the champion.
'''

import common_lib, sys

NBA_POWER_RANKING_CSV_FILE = sys.argv[1]
YEAR = sys.argv[2]


def get_two_leading_teams_of_true_power_ranking(teamList):
    header = teamList.pop()
    leadingTeam = teamList.pop()
    secondLeadingTeam = teamList.pop()
    return leadingTeam, secondLeadingTeam

def get_team_champion_from_html(filename):
    data = common_lib.open_file(filename)

    # Parsing through the file to get League Champion
    startPos = data.find('League Champion:')
    endPos = data.__len__()
    data = data[startPos:endPos]

    startPos = data.find('.html">')
    endPos = data.__len__()
    data = data[startPos:endPos]

    startPos = data.find('>')
    endPos = data.find('</a>')
    leagueChampion = data[startPos:endPos]
    leagueChampion = leagueChampion.replace('>', '')

    return leagueChampion

def get_team_finals_runner_up_from_html(filename):
    data = common_lib.open_file(filename)

    # Parsing through the file to get Finals Runner Up
    startPos = data.find('League Playoffs')
    endPos = data.__len__()
    data = data[startPos:endPos]

    startPos = data.find('Finals</span>')
    endPos = data.__len__()
    data = data[startPos:endPos]

    startPos = data.find('over <a href="')
    endPos = data.__len__()
    data = data[startPos:endPos]

    startPos = data.find('>')
    endPos = data.find('</a>')
    runnerUp = data[startPos:endPos]
    runnerUp = runnerUp.replace('>', '')

    return runnerUp

def change_element_into_str(theElement):
    theStr = str(theElement)
    theStr = theStr.replace("['", "")
    theStr = theStr.replace("']", "")
    return theStr

# Get rid of the original NBA_LEADING_TEAM_CHAMPION_CHECK_CSV_FILE
def cleanup():
    data = common_lib.open_file(common_lib.NBA_LEADING_TEAM_CHAMPION_CHECK_CSV_FILE)
    if data == 'FileNotFoundError':
        pass
    else:
        data = ''
        from os import remove
        remove(common_lib.NBA_LEADING_TEAM_CHAMPION_CHECK_CSV_FILE)

def start_main():
    cleanup()

    finalList = []
    teamList = common_lib.get_multiple_col(NBA_POWER_RANKING_CSV_FILE, 0)
    leadingTeamsTuple = get_two_leading_teams_of_true_power_ranking(teamList)
    leadingTeam = leadingTeamsTuple[0]
    secondLeadingTeam = leadingTeamsTuple[1]
    championTeam = get_team_champion_from_html(common_lib.NBA_CHAMPION_HTML_FILE)
    finalsRunnerUpTeam = get_team_finals_runner_up_from_html(common_lib.NBA_CHAMPION_HTML_FILE)


    # Check if file exist.
    data = common_lib.open_file(common_lib.NBA_LEADING_TEAM_CHAMPION_CHECK_CSV_FILE)
    if data == 'FileNotFoundError':
        finalList.append(['YEAR', 'TRUE_POWER_RANK_LEAD_TEAM', 'TRUE_POWER_RANK_SECOND_LEAD_TEAM', 'CHAMPION_TEAM', 'FINALS_RUNNER_UP_TEAM', 'SAME?'])

    # if the program cannot find a championTeam, then print 'No Champion'.
    if not championTeam:
        championTeam = 'No Champion'

    if not finalsRunnerUpTeam:
        finalsRunnerUpTeam = 'No Runner Up'

    # Check if leadingTeam is the same as championTeam
    leadingTeam = change_element_into_str(leadingTeam)
    secondLeadingTeam = change_element_into_str(secondLeadingTeam)
    if leadingTeam.lower() == championTeam.lower():
        sameTeam = True
    elif leadingTeam.lower() == finalsRunnerUpTeam.lower():
        sameTeam = True
    elif secondLeadingTeam.lower() == championTeam.lower():
        sameTeam = True
    elif secondLeadingTeam.lower() == finalsRunnerUpTeam.lower():
        sameTeam = True
    else:
        sameTeam = False

    finalList.append([YEAR, leadingTeam, secondLeadingTeam, championTeam, finalsRunnerUpTeam, sameTeam])
    dataStr = common_lib.convert_list_into_str(finalList)
    dataStr = dataStr + '\n'

    common_lib.append_file(dataStr, common_lib.NBA_LEADING_TEAM_CHAMPION_CHECK_CSV_FILE)

# Get run time of the parameter module
def actual_run_time():
    def new_func():
        start_main()
    from timeit import timeit
    seconds = timeit(new_func, number=1)
    from datetime import timedelta
    seconds = timedelta(seconds=float(seconds))

    name = common_lib.module_name() + '.py'
    print('Actual run time on ' + name + ':', seconds)

def main():
    actual_run_time()

main()