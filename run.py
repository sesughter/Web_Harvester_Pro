from books_to_scrape import scrape_books
from cleaner import clean_data
from exporter import export_to_csv, export_to_excel
from notifier import send_email_notification
from datetime import datetime

def main():
    print("starting scrape...")
    raw_data = scrape_books(pages=2)
    print(f"scraped {len(raw_data)}items")

    print("cleaning data")
    cleaned_df = clean_data(raw_data)

    print("exporting data...")
    export_to_csv(cleaned_df, f"exports/books_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.csv")
    export_to_excel(cleaned_df, f"exports/books_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.xlsx")

    send_email_notification(
        subject="Daily Scrapped Completed",
        body="your competitors data has been scrapped and saved in /export",
        to_email="siortsor@gmail.com"
    )

    print("all done")

if __name__ == "__main__":
    main()