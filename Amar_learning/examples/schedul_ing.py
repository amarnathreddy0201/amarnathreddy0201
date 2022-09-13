# Schedule Task
# pip install schedule
from re import L
import schedule
# func 1
def best_luck():
    print("Best of Luck for Interview")
# func2 
def Read():
    print("Don't forget to Read Article")
# func3
def Motivation():
    print("Work smarter not harder")

schedule.every().seconds.do(Motivation)
schedule.every(1).minutes.do(Motivation)
schedule.every().hour.do(Read)
schedule.every().thursday.do(best_luck)
schedule.every().day.at("21:16").do(Read)
while True:
    schedule.run_pending()