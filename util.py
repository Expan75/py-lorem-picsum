import sys

def progressbar(iterable, prefix="", size=60, file=sys.stdout):
    """ Simple progressbar ripped from: 
        https://stackoverflow.com/questions/3160699/python-progress-bar/34482761#34482761

        Can be used on any iterable but brakes on generators without list casting
    """
    count = len(iterable)
    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" % (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()        
    show(0)
    for i, item in enumerate(iterable):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()
