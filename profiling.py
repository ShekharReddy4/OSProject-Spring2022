

from subprocess import Popen

# Subprocess Command
cmd = "python3 bellmanFord.py"
po = Popen(cmd.split())
cmdd = "python3 floydWarshall.py"
po = Popen(cmdd.split())
