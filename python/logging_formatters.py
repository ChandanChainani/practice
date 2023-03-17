from sys import stdout as sys_stdout
import logging

logger = logging.getLogger('one')
logger.setLevel(logging.DEBUG)

sh = logging.StreamHandler(sys_stdout)
# formatter = logging.Formatter('%(asctime)s.%(msecs)d, %(created).0f, %(levelname)s, %(module)s, %(process)s, %(processName)s, %(thread)d, %(threadName)s, %(pathname)s:%(lineno)s, %(filename)s:%(lineno)s, %(name)s, %(funcName)s, %(message)s', "%Y-%m-%d %H:%M:%S")
formatter = logging.Formatter('[%(name)s], %(asctime)s.%(msecs)d, %(created).0f, %(levelname)s, %(process)s, %(processName)s, %(thread)d, %(threadName)s, %(module)s, %(filename)s:%(lineno)s, %(funcName)s, %(message)s', "%Y-%m-%d %H:%M:%S")
sh.setFormatter(formatter)
logger.addHandler(sh)

logger.info(1)
# print(dir(logger))

logger_two = logger.getChild('two')
logger_two.debug(2)

logger_three = logger.getChild('three')

def my_function():
  logger_three.info(3)

my_function()

logger.warning('four')
logger_two.critical('five')
