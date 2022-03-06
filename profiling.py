
import psutil
from subprocess import Popen

# Subprocess Command
cmd = "python3 bellmanFord.py"
po = Popen(cmd.split())
print("Process ID:", po.pid)


p = psutil.Process(po.pid)
print(p)

print(p.name())

print(p.exe())

print(p.cwd())

print(p.cmdline())

print(p.parent())

print("process cpu util in percentage is : ",p.cpu_percent(interval=1.0))
print("process memory in percentage is : ", p.memory_info() )





# Check the status of process
# poll() method returns 'None' if the process is running else returns the exit code
#print(p.poll())