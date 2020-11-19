# author: Tiffany Timbers
# date: 2020-01-15

"This script prints out docopt args.
Usage: demo.R <arg1> --arg2=<arg2> [--arg3=<arg3>] [<arg4>]

Options:
<arg>             Takes any value (this is a required positional argument)
--arg2=<arg2>     Takes any value (this is a required option)
[--arg3=<arg3>]   Takes any value (this is an optional option)
[<arg4>]          Takes any value (this is an optional positional argument)
" -> doc

library(docopt)
opt <- docopt(doc)

main <- function(opt, arg4){
    print(opt)
    print(typeof(opt))
    print(paste0("The value for arg4 is ",arg4, " and the type of arg4 is ", typeof(arg4)))
}

main(opt, opt$arg4)

