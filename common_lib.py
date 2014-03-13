'''
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


#NBA_STANDINGS_URL = 'http://www.nba.com/standings/team_record_comparison/conferenceNew_Std_Div.html?ls=iref:nba:gnav'

NBA_STANDING_DIR = 'C:/Users/glau/Downloads/nbaStanding/'

NBA_STANDING_HTML_FILE = NBA_STANDING_DIR + 'nbaStandings.html'
NBA_CHAMPION_HTML_FILE = NBA_STANDING_DIR + 'nbaChampion.html'

NBA_STANDING_CSV_FILE = NBA_STANDING_DIR + 'nbaStandings.csv'
NBA_LEADING_TEAM_CHAMPION_CHECK_CSV_FILE = NBA_STANDING_DIR + 'nbaLeadingChampionCheck.csv'

# Download data from the web and return the data as str
def get_data_from_web(urlStr):
    from urllib.request import urlopen
    from urllib.error import URLError, HTTPError, ContentTooShortError
    # Get data
    try:
        print('Connecting to', urlStr)
        response = urlopen(urlStr)
    except URLError:
        print('URL ERROR')
        html = 'ERROR: URL'
    except HTTPError:
        print('HTTP ERROR')
        html = 'ERROR: HTTP'
    except ContentTooShortError:
        print('CONTENT TOO SHORT ERROR')
        html = 'ERROR: CONTENT TOO SHORT'
    except: # Other exceptions
        from sys import exc_info
        e = exc_info()[0]
        print("Error: %s" % e)
        html = "Error: %s" % e
    else:
        print('Response:', response.status, response.reason)
        html = response.read()
    return html

# Write a file in binary
def write_binary_file(dataStr, filename):
    # Write dataStr to a new file
    target = open(filename, 'wb')
    target.write(dataStr)
    target.close

# Write a file
def write_file(dataStr, filename):
    # Write dataStr to a new file
    target = open(filename, 'w')
    target.write(dataStr)
    target.close

# Append a file
def append_file(dataStr, filename):
    # Append dataStr to a file
    target = open(filename, 'a')
    target.write(dataStr)
    target.close

# Open downloaded file and read file into string
def open_file(filename):
    try:
        with open(filename) as myfile:
            data = myfile.read()
    except FileNotFoundError:
        return 'FileNotFoundError'
    return data

# Converts list into dataStr to write to csv
def convert_list_into_str(theList):
    # rows contains the list of lists
    lines = []
    for row in theList:
        lines.append(','.join(map(str, row)))
        dataStr = '\n'.join(lines)
    return dataStr

# Opens csv file and prints multiple columns
# get_multiple_col(csvFile, 0, 1, 2)
def get_multiple_col(filename, *col):
    def get_it_now(filename, list_of_col):
        from csv import reader
        for row in reader(open(filename), delimiter=','):
            for i in list_of_col:
                yield [row[i]]
    col = list(col)
    resultList = list(get_it_now(filename, col))
    resultList.reverse()
    return resultList

# This module is necessary to return a pure string element.
def parse_the_popped_element_to_return_str(element):
    element = str(element)
    element = element.replace('[', '')
    element = element.replace(']', '')
    element = element.replace("'", "")
    return element

# Calls another module
def call_another_module(strOfModName):
    from subprocess import call
    from sys import stderr
    try:
        retcode = call(strOfModName, shell=True)
        if retcode < 0:
            print("Child was terminated by signal", -retcode, file=stderr)
        else:
            print("Child returned", retcode, file=stderr)
    except OSError as e:
        print("Execution failed:", e, file=stderr)

# Get module name
def module_name():
    from sys import argv
    from os import path
    filename= argv[0]
    name = path.splitext(path.basename(filename))[0]
    return name