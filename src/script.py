import RPi.GPIO as GPIO # only works on raspberry pi
import time
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

# email config
sender = os.getenv("EMAIL_SENDER") # email you want to send notification with
receiver = os.getenv("EMAIL_RECEIVER") # email you want to be notified by
password = os.getenv("EMAIL_PASSWORD") # google app password
subject = "Oliver's feeder is low!"
message = "Our kitty's food bin needs to be refilled ASAP!"
text = f"Subject: {subject}\n\n{message}"

# gpio config
TRIG = 23
ECHO = 24
THRESHOLD_DISTANCE = 10.0
MIN_DISTANCE = 2.0
RETRY_C = 3 # only allow 3 retries before giving up
RETRY_D = 5 # 5 seconds in between retries

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setmode(ECHO, GPIO.IN)

def sendAlert():
    for attempt in range(RETRY_C):
        try:
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls() # secure, encrypted connection
                server.login(sender, password)
                server.sendmail(sender, receiver, text)
                print(f"Email has been sent to {receiver}")
                return True
        except Exception as e:
            print(f"Failed to send email: {e}")
            if attempt < RETRY_C -1:
                time.sleep(RETRY_D)
    print(f"Failed to send email after {RETRY_C} attempts")
    return False

def measure_distance():
    for attempt in range(RETRY_C):
        try:
            # ensures trigger pin is low
            GPIO.output(TRIG, False)
            time.sleep(2)

            # send a 10us pulse to the trigger pin
            GPIO.output(TRIG, True)
            time.sleep(.00001)
            GPIO.output(TRIG, False)

            # measure echo time
            pulse_start = time.time()
            while GPIO.input(ECHO) == 0:
                pulse_start = time.time()

            pulse_end = time.time()
            while GPIO.input(ECHO) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            
            #calculate distance
            distance = pulse_duration * 17150 # speed of sound in cm/us divided by 2 (round trip)
            distance = round(distance, 2)

            if distance > MIN_DISTANCE:
                return distance
            else:
                print(f"Measured distance {distance} is less than the minimum measurable distance {MIN_DISTANCE} cm")
        
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < RETRY_C - 1:
                time.sleep(RETRY_D)

    print(f"Failed to measure distance after {RETRY_C} attempts")
    return None

def main():
    try:
        distance = measure_distance()
        if distance is not None and distance < THRESHOLD_DISTANCE:
            sendAlert()
    except Exception as e:
        print(f"Error in main loop: {e}")
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    while True:
        main()
        time.sleep(8*60*60)