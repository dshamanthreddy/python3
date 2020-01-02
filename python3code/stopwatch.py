import time

start_time = time.localtime()
print(f"timer started at {time.strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press any key to stop timer ")
stop_time = time.localtime()
diff = time.mktime(stop_time) - time.mktime(start_time)
print (f"timmer stopped at {time.strftime('%X', stop_time)}")
print(f"total time : {diff} seconds")