import threading
import time

import pytest


@pytest.fixture()
def get_unique_name():
    tag_name = str(time.time()) + threading.currentThread().name  # 获取时间戳,时间戳+threading.currentThread().name解决多线程的问题
    # 在并行用例的时候，tag_name=time.time()代码会出现问题
    return tag_name