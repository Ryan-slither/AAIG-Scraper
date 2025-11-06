from bs4 import BeautifulSoup
from constants import AI_DEADLINES_ORG_URL
from selenium import webdriver


def get_selenium_html_content(url: str):
    driver = webdriver.Chrome()
    driver.get(url)
    html_content = driver.execute_script("return document.body.innerHTML")
    return html_content


def scrape_ai_deadlines_org():
    soup = BeautifulSoup(get_selenium_html_content(AI_DEADLINES_ORG_URL), "html.parser")
    coming_conferences = soup.find("div", id="coming_confs")
    conferences = coming_conferences.find_all("div", class_="ConfItem")
    for conf in conferences:
        title = conf.find("a")
        print(title.text)


if __name__ == "__main__":
    print("Starting Scraper")
    scrape_ai_deadlines_org()
