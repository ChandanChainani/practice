# clogger
import os
import logging
import datetime
from pytz import timezone, utc

clogger = None

if clogger is None:
    current_directory = os.path.dirname(os.path.abspath(__file__))
    log_file_name = os.path.join(current_directory, "debug.log")

    clogger = logging.getLogger("logger")
    clogger.propagate = False
    clogger.setLevel(logging.DEBUG)

    if not clogger.handlers:
        fh = logging.FileHandler(log_file_name, mode='a')
        formatter = logging.Formatter('%(asctime)s.%(msecs)d %(name)s %(levelname)-8s [%(pathname)s(%(lineno)d):%(funcName)s] %(message)s', datefmt='%a, %d %b %Y %H:%M:%S')
        fh.setFormatter(formatter)
        clogger.addHandler(fh)

        def customTime(*args):
            utc_dt = utc.localize(datetime.datetime.utcnow())
            local_tz = timezone("Asia/Kolkata")
            return utc_dt.astimezone(local_tz).timetuple()

        formatter.converter = customTime
