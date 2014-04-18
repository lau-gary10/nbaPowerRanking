'''
The main file to run

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

def start_main():

    # Modules to run if you want to get the current true power ranking
    def run_to_get_current_power_ranking():
        common_lib.call_another_module('get_html_data.py' + NBA_STANDINGS_URL + NBA_CHAMPION_URL)
        common_lib.call_another_module('parse_html_file.py')
        common_lib.call_another_module('evaluate_true_power_ranking.py' + NBA_POWER_RANKING_CSV_FILE)
        common_lib.call_another_module('evaluate_gap.py' + NBA_POWER_RANKING_CSV_FILE)
#        common_lib.call_another_module('open_excel_instance.py' + NBA_POWER_RANKING_CSV_FILE)

    # Modules that run to get true power ranking
    def run_to_get_history_of_finals_teams_in_relation_to_true_power_rank():
        common_lib.call_another_module('get_html_data.py' + NBA_STANDINGS_URL + NBA_CHAMPION_URL)
        common_lib.call_another_module('parse_html_file.py')
        common_lib.call_another_module('evaluate_true_power_ranking.py' + NBA_POWER_RANKING_CSV_FILE)
        common_lib.call_another_module('evaluate_gap.py' + NBA_POWER_RANKING_CSV_FILE)
        common_lib.call_another_module('evaluate_true_power_ranking_with_champion.py' + NBA_POWER_RANKING_CSV_FILE + YEAR)

    flag = False
    START_YEAR = 1950
    END_YEAR = 2014
    LAST_MAX = END_YEAR + 1

################################
# Use these variables to get the specific year of nba standings.
#   Otherwise, comment them out:
    flag = True
    FLAG_YEAR = 2014
################################

    if flag == False:
        for i in range(START_YEAR, LAST_MAX):
            year = str(i)
            NBA_STANDINGS_URL = ' ' + 'http://www.basketball-reference.com/leagues/NBA_' + year + '_standings.html'
            NBA_CHAMPION_URL = ' ' + 'http://www.basketball-reference.com/leagues/NBA_' + year + '.html'
            NBA_POWER_RANKING_CSV_FILE = ' ' + common_lib.NBA_STANDING_DIR + 'nbaPowerRanking' + year + '.csv'
            YEAR = ' ' + year
            run_to_get_history_of_finals_teams_in_relation_to_true_power_rank()
            from time import sleep
            sleep(3)
    else:
        FLAG_YEAR = str(FLAG_YEAR)
        NBA_STANDINGS_URL = ' ' + 'http://www.basketball-reference.com/leagues/NBA_' + FLAG_YEAR + '_standings.html'
        NBA_CHAMPION_URL = ' ' + 'http://www.basketball-reference.com/leagues/NBA_' + FLAG_YEAR + '.html'
        NBA_POWER_RANKING_CSV_FILE = ' ' + common_lib.NBA_STANDING_DIR + 'nbaPowerRanking' + FLAG_YEAR + '.csv'
        run_to_get_current_power_ranking()

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

if __name__ == '__main__':
    main()