import time 
for i in range(100):
    print(i)
    time.sleep(1)

# If output is buffered, when will I get logs? = 100 seconds

# What would happen if your scripts crashes during the run

# If output is not bufferd, when will I get logs? = after every count
# What would happen if your scripts crashes during the run = I will know exactly at what number the app is crashing on

# Application - critical, cannot be Interrupted
# Paralell Executions, Can be interrupted = have output buffered