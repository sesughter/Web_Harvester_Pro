from apscheduler.schedulers.blocking import BlockingScheduler
from run import main

def job():
    print("Running scheduler scrape...")
    main()

if __name__ == "__main__":
    scheduler = BlockingScheduler()
    # running one a day at 9:00am
    scheduler.add_job(job, 'cron', hour=9, minute=0)
    print("scheduling started press ctrl + c to exit.")
    scheduler.start()