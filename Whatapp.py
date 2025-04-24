import pywhatkit
import pyautogui
import time

phone_no = input("Enter phone number: ")
message = "Hello".encode("utf-8").decode("utf-8")

# Schedule the message at 1:07 PM (13:07 in 24-hour format)
pywhatkit.sendwhatmsg(phone_no, message, 13, 4, wait_time=7)

# Wait for WhatsApp to open
time.sleep(10)

# Automatically press "Enter" to send the message
pyautogui.press("enter")

print("Message sent successfully!")

