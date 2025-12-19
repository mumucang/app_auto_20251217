
import logging
import os
import time

from config import logs_path


class LoggerUtil:
    @staticmethod
    def get_logger(log_name):
        # 创建一个日志器对象
        logger = logging.getLogger(log_name)
        # 设置日志级别为DEBUG，可以根据需要调整
        logger.setLevel(logging.DEBUG)

        # 避免重复添加handler

            # 创建日志文件路径
        str_time = time.strftime("%Y%m%d")
        log_file = os.path.join(logs_path, log_name+"_"+str_time + '.log')

        # 创建文件处理器，用于将日志写入文件
        file_handler = logging.FileHandler(log_file,encoding='utf-8')
        file_handler.setLevel(logging.DEBUG)

        # 创建控制台处理器，用于将日志输出到控制台
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # 创建日志格式
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        # 设置处理器的日志格式
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # 将处理器添加到日志器
        logger.addHandler(file_handler)
        # logger.addHandler(console_handler)

        return logger

# 使用示例
if __name__ == "__main__":
    # 动态生成日志名称，例如根据测试用例名称
    dynamic_log_name = "test_case_1"
    logger = LoggerUtil.get_logger(dynamic_log_name)
    logger.info("这是一个信息日志")
    logger.error("这是一个错误日志")
