import psutil
print('******************cpu usage:***************** \n',psutil.cpu_times())
#print('**********************memory full info:************** \n', psutil.memory_full_info())
print('*********swap memory:**************** \n', psutil.swap_memory())
print('*********virtual memory :********* ', psutil.virtual_memory()._asdict())
