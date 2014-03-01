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
    # Modules that only need to run once, and are not updated daily (ex: height)
    def run_once():
        return
    # Modules that run multiple times, and are updated daily.
    def run_multiple_times():
        common_lib.call_another_module('get_html_data.py')
        common_lib.call_another_module('parse_html_file.py')
        common_lib.call_another_module('evaluate_true_power_ranking.py')
        common_lib.call_another_module('evaluate_gap.py')

    run_once()
    run_multiple_times()

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