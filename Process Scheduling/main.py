import sys
sys.path.append("scheduling_policies")  
from util import read_processes_from_file

#from fifo import fifo_function
#from sjf import sjf_function
from rr import rr_function


processes = read_processes_from_file("config.txt") 
#fifo_function(processes)
#sjf_function(processes)
rr_function(processes, time_quantum=4)  
