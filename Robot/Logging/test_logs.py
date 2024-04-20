import inspect
import logging

class Test_Logs:
    @staticmethod
    def custom_logs(self, level=logging.DEBUG):
        log_name = inspect.stack()[1][3]
        logger = logging.getLogger(log_name)
        logger.setLevel(level)
        fh = logging.FileHandler("test_log.log")
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")
        fh.setFormatter(formatter)
        logger.addHandler(fh)
        return logger

