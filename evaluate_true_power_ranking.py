'''
Get the true power ranking

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

class globalListClass:
    globalListVar = []

# Sort through true_pct
def sort_true_pct_ranking():
    list2 = []

    # Get values and append the file
    thisList = common_lib.get_multiple_col(common_lib.NBA_STANDING_CSV_FILE, 0, 10, 11, 3)

    teamName = thisList.pop()
    teamName = common_lib.parse_the_popped_element_to_return_str(teamName)
    homeLoss = thisList.pop()
    homeLoss = common_lib.parse_the_popped_element_to_return_str(homeLoss)
    roadWin = thisList.pop()
    roadWin = common_lib.parse_the_popped_element_to_return_str(roadWin)
    pct = thisList.pop()
    pct = common_lib.parse_the_popped_element_to_return_str(pct)
    truePct = 'TRUE_PCT'
    list2.append([teamName, roadWin, homeLoss, pct, truePct])

    i = 0
    while i < len(thisList):
        teamName = thisList.pop()
        teamName = common_lib.parse_the_popped_element_to_return_str(teamName)
        homeLoss = thisList.pop()
        homeLoss = common_lib.parse_the_popped_element_to_return_str(homeLoss)
        roadWin = thisList.pop()
        roadWin = common_lib.parse_the_popped_element_to_return_str(roadWin)
        pct = thisList.pop()
        pct = common_lib.parse_the_popped_element_to_return_str(pct)
        truePct = float(roadWin) / (float(roadWin) + float(homeLoss))
        truePct = str(truePct)
        list2.append([teamName, roadWin, homeLoss, pct, truePct])

    # Sort by descending true_pct (priority on true_pct, then pct)
    list2.sort(key=lambda x: x[4])
    length = len(list2)
    header = list2.pop()
    list3 = list2
    finalList = []
    finalList.append(header)


    for i in range(length):
        try:
            element1 = list3.pop()
            element2 = list3.pop()
        except IndexError:
            finalList.append(element2)
            break
        else:
            floatTruePct1 = float(element1[3])
            floatTruePct2 = float(element2[3])

            # If true_pct are the same, sort by pct.
            if floatTruePct1 == floatTruePct2:
                floatPct1 = float(element1[4])
                floatPct2 = float(element2[4])

                if floatPct2 > floatPct1:
                    finalList.append(element2)
                    list3.append(element1)
                else:
                    finalList.append(element1)
                    list3.append(element2)
            else:
                finalList.append(element1)
                list3.append(element2)

    # Clean out the lists
    del list2[:]
    del list3[:]
    return finalList

def start_main():
    tmpList = sort_true_pct_ranking()

    tmpList = common_lib.convert_list_into_str(tmpList)
    common_lib.write_file(tmpList, common_lib.NBA_POWER_RANKING_CSV_FILE)

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