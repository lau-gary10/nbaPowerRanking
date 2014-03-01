'''
Find the gap between each team and put them on a tier

If the true_pct gap between teams are 5% or greater, than the lesser team belongs on a lesser
tier.

Explanation of tiers:
    Tier A - Title Contenders. Teams that are capable of winning the championship.
    Tier B - Playoff Contenders. Teams that are capable of making it into the playoffs. They are
        the dark horses to get the championship.
    Tier C and D - Playoff Strugglers. Teams that will struggle getting into the playoffs. Very
             unlikely to win the championship.
    Tier E and below - See-You-Next-Year. Teams that are tanking, or just does not have any
            potential to reach the playoffs.

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
PCT_GAP_CUTOFF = .05

def start_main():
    list2 = []
    finalList = []

    theList = common_lib.get_multiple_col(common_lib.NBA_POWER_RANKING_CSV_FILE, 0,1,2,3,4)

    i = 0
    while i < len(theList):
        teamName = common_lib.parse_the_popped_element_to_return_str(theList.pop())
        roadWin = common_lib.parse_the_popped_element_to_return_str(theList.pop())
        homeLoss = common_lib.parse_the_popped_element_to_return_str(theList.pop())
        pct = common_lib.parse_the_popped_element_to_return_str(theList.pop())
        truePct = common_lib.parse_the_popped_element_to_return_str(theList.pop())
        list2.append([teamName, roadWin, homeLoss, pct, truePct])

    # Add column 'PCT_GAP' and 'TIER' onto header
    list2.reverse()
    header = list2.pop()
    header.append('PCT_GAP')
    header.append('TIER')
    finalList.append(header)

    # Evaluates team's TRUE_PCT to find PCT_GAP and TIER

    # Set initial values up for looping
    length = len(list2)
    tier = 0
    letterTier = chr(tier + ord('A')) # Converts the int to corresponding english alphabet
    element1 = list2.pop()
    element1.append('0')
    element1.append(str(letterTier))
    list2.append(element1)
    for i in range(length):
#    for i in range(0,1):
        try:
            # Grab two elements from the list
            element1 = list2.pop()
            element2 = list2.pop()
        except IndexError:
            finalList.append(element2)
            break
        else:
            # Get PCT_GAP
            floatTruePct1 = float(element1[4])
            floatTruePct2 = float(element2[4])
            pctGap = (floatTruePct1 / floatTruePct2) - 1

            # Get TIER
            if pctGap > PCT_GAP_CUTOFF:
                tier += 1
                letterTier = chr(tier + ord('A'))

            element2.append(str(pctGap))
            element2.append(str(letterTier))
            finalList.append(element1)
            list2.append(element2)

    finalList = common_lib.convert_list_into_str(finalList)
    common_lib.write_file(finalList, common_lib.NBA_POWER_RANKING_CSV_FILE)

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
