from Scraper import Wiley

# which journal do you want to crawl
target_journal = "International Economic Review"
scraper = Wiley.Wileyscraper()
df = scraper.scrape(target_journal)
df.to_csv("output.csv", header=True)
