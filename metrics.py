import psutil
print('******************cpu usage:***************** \n',psutil.cpu_times())
print('*********swap memory:**************** \n', psutil.swap_memory())
print('*********virtual memory :********* ', psutil.virtual_memory()._asdict())
