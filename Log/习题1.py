import logging
log_formart = "%(asctime)s ----- %(levelname)s ----- %(message)s"
logging.basicConfig(level=logging.DEBUG, format=log_formart, filename="习题1.log")
logging.debug("这是习题---debug级别的日志")
logging.info("这是习题---info级别的日志")
logging.warning("这是习题---warning级别的日志")
logging.error("这是习题---error级别的日志")
logging.critical("这是习题---critical级别的日志")
