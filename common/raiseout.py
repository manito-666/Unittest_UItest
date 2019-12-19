import traceback
from util.log.mylog import Log

def raiseout():
    Log().error( "This is a error log.")
    with open(Log().logname, 'a+') as f:
        f.writelines(traceback.format_exc())