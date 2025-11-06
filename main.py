from constants import AI_DEADLINES_ORG_URL
from scraper import Scraper

if __name__ == "__main__":
    print("Starting Scraper")
    s = Scraper(AI_DEADLINES_ORG_URL)
    s.scrape_ai_deadlines_org()
    print("Scraper Finished")
