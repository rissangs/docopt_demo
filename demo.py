# author: Tiffany Timbers
# date: 2020-01-15

"""This script prints out docopt args.
Usage: docopt.py <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg4>]          Takes any value (this is an optional positional argument)
"""

from docopt import docopt
opt = docopt(__doc__)

def main(opt, arg4):
    print(opt)
    print(type(opt))
    print(f'The value of arg4 is {arg4} and the type of arg4 is {type(arg4)}')

if __name__ == "__main__":
    main(opt, opt["<arg4>"])