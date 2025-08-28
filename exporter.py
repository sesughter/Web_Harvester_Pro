def export_to_csv(df, filename="exports/books.csv"):
    df.to_csv(filename, index=False)
    print(f"data exported to {filename}")

def export_to_excel(df, filename="exports/books.xlsx"):
    df.to_excel(filename, index=False)
    print(f"data exported to {filename}")