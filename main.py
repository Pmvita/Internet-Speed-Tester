# Import the speedtest module to measure internet speed
import speedtest

# Define a function to convert bytes to megabytes
def bytes_to_mb(bytes):
    # Define constants for kilobytes and megabytes
    KB = 1024
    MB = KB * 1024
    # Return the result of dividing the input bytes by megabytes, rounded to the nearest integer
    return int(bytes/MB)

# Create an instance of the Speedtest class
st = speedtest.Speedtest()

# Get user input to start the test
start = input('Press Enter to Start')

# Measure download speed in bytes and convert it to megabytes
down_speed = str(bytes_to_mb(st.download()))

# Measure upload speed in bytes and convert it to megabytes
up_speed = str(bytes_to_mb(st.upload()))

# Get the ping result from the speedtest instance
ping = st.results.ping

# Print the download speed, upload speed, and ping result
print(down_speed + 'mb/s')
print(up_speed + 'mb/s')
print(ping)