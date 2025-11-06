from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd


class Scraper:
    def __init__(self, url: str):
        self.html_content = self.get_selenium_html_content(url)

    def get_selenium_html_content(self, url: str):
        driver = webdriver.Chrome()
        driver.get(url)
        html_content = driver.execute_script("return document.body.innerHTML")
        return html_content

    def scrape_ai_deadlines_org(self):
        data = {
            "title": [],
            "note1": [],
            "date": [],
            "place": [],
            "note2": [],
            "deadline": [],
        }
        soup = BeautifulSoup(self.html_content, "html.parser")
        coming_conferences = soup.find("div", id="coming_confs")
        conferences = coming_conferences.find_all("div", class_="ConfItem")
        for conf in conferences:
            title = conf.find("a")
            notes = conf.find_all("div", class_="note")
            date = conf.find("span", class_="conf-date")
            place = conf.find("span", class_="conf-place")
            deadline = conf.find("span", class_="deadline-time")

            title_text = title.text.strip()
            note1_text = notes[0].text.strip()
            date_text = date.text.strip()
            place_text = place.text.strip()
            note2_text = notes[1].text.strip() if len(notes) > 1 else None
            deadline_text = deadline.text.strip()
            date_place_text = f"{date_text} {place_text}"

            data["title"].append(title_text)
            data["note1"].append(note1_text)
            data["date"].append(date_text)
            data["place"].append(place_text)
            data["note2"].append(note2_text)
            data["deadline"].append(deadline_text)

            print(title_text)
            print(note1_text)
            print(date_place_text)
            if note2_text is not None:
                print(note2_text)
            print(deadline_text)
            print()

        self.convert_to_csv(
            data,
            f"./csvs/ai_deadline_org_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv",
        )

    def convert_to_csv(self, data: dict, path: str):
        pd.DataFrame(data).to_csv(path, index=False)
