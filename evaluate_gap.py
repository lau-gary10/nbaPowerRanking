'''
Find the gap between each team and put them on a tier

If the true_pct gap between teams are 4.5% or greater, than the lesser team belongs on a lesser
tier.

Explanation of tiers:
    Tier A - Title Contender. Teams that are fully capable of winning the championship.
        Projection: Conference Finals - League Finals
    Tier B - Playoff Contender. Teams that are fully capable of getting into the playoffs.
            Possibly Title Contender.
        Projection: 2nd Round - League Finals
    Tier C and D - Playoff Runner. Teams that can get into the playoffs. Unlikely to contend
            for a title.
        Projection: 1st Round - Conference Finals
    Tier E and F - Playoff Struggler. Teams that will struggle to get into playoffs. Highly
            unlikely to contend for a title.
        Projection: 10th Conference Place - 2nd Round
    Tier G and below - Yawner. Teams that are tanking, or just do not have any
            potential to reach the playoffs. Unlikely to pay tickets to see these teams.
        Projection: Lottery Picks

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
PCT_GAP_CUTOFF = .045

# Assigns a label to the letter
def assign_label_to_tier(letter):
    if 'A' == letter:
        label = 'Title Contender'
    elif 'B' == letter:
        label = 'Playoff Contender'
    elif 'C' == letter:
        label = 'Playoff Runner'
    elif 'D' == letter:
        label = 'Playoff Runner'
    elif 'E' == letter:
        label = 'Playoff Struggler'
    elif 'F' == letter:
        label = 'Playoff Struggler'
    else:
        label = 'Yawner'
    return label

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

    # Add column 'PCT_GAP', 'TIER', and 'LABEL' onto header
    list2.reverse()
    header = list2.pop()
    header.append('PCT_GAP')
    header.append('TIER')
    header.append('LABEL')
    finalList.append(header)

# Evaluates team's TRUE_PCT to find PCT_GAP, TIER, and LABEL

    # Set initial values up for looping
    length = len(list2)
    tier = 0
    letterTier = chr(tier + ord('A')) # Converts the int to corresponding english alphabet
    label = assign_label_to_tier(letterTier)
    element1 = list2.pop()
    element1.append('0')
    element1.append(str(letterTier))
    element1.append(str(label))
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

            # Assign LABEL to corresponding TIER
            label = assign_label_to_tier(letterTier)

            element2.append(str(pctGap))
            element2.append(str(letterTier))
            element2.append(str(label))
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
