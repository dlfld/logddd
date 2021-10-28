import inspect
import time
from os.path import basename


def dlog(*args):
    callFrame = inspect.currentframe().f_back
    frameInfo = inspect.getframeinfo(callFrame)
    filename = basename(frameInfo.filename)
    code = str(frameInfo.code_context).replace(" ", '').replace('\\n', '').replace('\'', '').replace('[', '').replace(
        ']', '')
    cur_time = time.asctime()
    res = f"\033[1;33m {filename}\tline:{frameInfo.lineno}\033[0m -> \033[32m{code}\033[0m : \033[1;34m {args}\033[0m {cur_time}"
    print(res)


