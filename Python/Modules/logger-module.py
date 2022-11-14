import logging

'''
logging.basicConfig(level=logging.DEBUG)

logging.info("Info Message")
logging.warning("Warning Message")
logging.error("Error Message")
logging.debug("Debug Message")
logging.critical("Critical Message")

print()
print ("--------------------------")
print()

logger = logging.getLogger("H4x0r")
logger.info("Info Message")
logger.critical("Crtical Message")
logger.log(logging.ERROR, "An error occcured")
'''

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger('H4x0r')

logger.setLevel(logging.DEBUG)

handler = logging.FileHandler("logs.log")
handler.setLevel(logging.INFO)

logger.addHandler(handler)

logger.debug("Debug Message")
logger.info("Info Message")
