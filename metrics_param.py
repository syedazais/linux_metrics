import sys
import psutil

#if(sys.argv[1] == "cpu")
print(str(sys.argv[1]))
print(str(sys.argv[1]) == 'cpu')
#print("cpuVar: ",$cpuVar)
print("cpu param", str(sys.argv))
#if(print(str(sys.argv[1]) == 'cpu')
#print('cpu')

#param1 = print(%sys.argv[1])
#print("param1: %s",$param1)
#param = % sys.argv[1]
#print('param: %s',% param)
#if(param == 'cpu')
print('******************cpu usage:***************** \n',psutil.cpu_times())
#print('**********************memory full info:************** \n', psutil.memory_full_info())

print('*********swap memory:**************** \n', psutil.swap_memory())
print('*********virtual memory :********* ', psutil.virtual_memory()._asdict())
