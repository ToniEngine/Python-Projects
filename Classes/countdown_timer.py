import time

def countdown_timer(seconds):
    while seconds > 0:
        mins = seconds // 60  # Calculate minutes
        secs = seconds % 60   # Calculate remaining seconds
        timer = f'{mins:02d}:{secs:02d}'  # Format as mm:ss
        print(timer, end="\r")  # Print timer on the same line
        time.sleep(1)  # Wait for 1 second
        seconds -= 1  # Decrease the total time by one second
    
    print("Time's up!")  # Timer has finished

# Input time in seconds
seconds_input = int(input("Enter the time in seconds: "))
countdown_timer(seconds_input)
