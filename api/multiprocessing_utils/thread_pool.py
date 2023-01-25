from concurrent.futures import ThreadPoolExecutor

THREADPOOL_EXECUTOR: ThreadPoolExecutor = ThreadPoolExecutor(max_workers=4)