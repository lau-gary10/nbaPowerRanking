'''
Gets html file and saves it

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
    data = common_lib.get_data_from_web(common_lib.NBA_STANDINGS_URL)
    common_lib.write_binary_file(data, common_lib.NBA_STANDING_HTML_FILE)

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