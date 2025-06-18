import requests
import random
import pandas as pd

from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from time import time, sleep


# Class definition
class PropertyScrapping:
    def __init__(self) -> None:
        self.properties = []
        self.urls = []
        self.total_time = 0

    def open_links_file(
        self, csv_path: str, has_header: bool, number_of_rows: int = None
    ) -> None:

        try:
            if has_header:
                urls_df = pd.read_csv(csv_path, header=0, nrows=number_of_rows)
                if "link" in urls_df.columns:
                    self.urls = urls_df["link"].tolist()
                else:
                    self.urls = urls_df.iloc[:, 0].tolist()
            else:
                urls_df = pd.read_csv(csv_path, header=None, nrows=number_of_rows)
                self.urls = urls_df.iloc[:, 0].tolist()

        except Exception as e:
            print(f"Error {e}")

    def get_raw_property(self, url: str, session: requests.Session) -> BeautifulSoup:

        start_time = time()

        sleep(random.uniform(0.1, 0.25))

        try:
            response = session.get(url)
            content = response.content
            print(response)
            soup = BeautifulSoup(content, "html.parser")
        except Exception as e:
            print(f"Error {e}")

        end_time = time()
        scrapping_duration = end_time - start_time
        print(f"This scrap has taken {scrapping_duration}")
        self.total_time += scrapping_duration

        return soup

    def get_property_characteristics(self, url: str, soup: BeautifulSoup) -> dict:

        property_characteristics = dict()

        try:
            type_prop = soup.find(class_="detail__header_title_main")
            type_of_property = type_prop.text.split()[0]
        except Exception as e:
            print(f"TYPE PROPERTY error {e} when trying to access  {url}\n")
            type_of_property = None

        try:
            code = soup.find(class_="vlancode").text
        except Exception as e:
            print(f"CODE error {e} when trying to access  {url}\n")
            code = None

        try:
            price = soup.find(class_="detail__header_price_data").text
        except Exception as e:
            print(f"PRICE error {e} when trying to access  {url}\n")
            price = None

        try:
            locality = soup.find(class_="city-line").text
        except Exception as e:
            print(f"LOCALITY error {e} when trying to access  {url}\n")
            locality = None

        property_characteristics["property_code"] = code
        property_characteristics["type_of_property"] = type_of_property
        property_characteristics["price"] = price
        property_characteristics["locality"] = locality

        for tag in soup.find_all("h4", class_=False):
            characteristic_name = "_".join(list(map(str.lower, tag.text.split())))
            property_characteristics[characteristic_name] = tag.find_next().text

        property_characteristics["property_url"] = url

        return property_characteristics

    def run_scrapping(self) -> None:
        ua = UserAgent()
        headers = {
            "User-Agent": ua.random,
            "Accept": (
                "text/html,application/xhtml+xml,application/xml;q=0.9,"
                "image/avif,image/webp,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.5",
            "Accept-Encoding": "gzip, deflate, br",
            "Connection": "keep-alive",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1",
            "TE": "trailers",
        }

        s = requests.Session()
        s.headers.update(headers)

        for url in self.urls:
            soup = self.get_raw_property(url, s)
            self.properties.append(self.get_property_characteristics(url, soup))

        print(f"This scrapping has lasted {self.total_time/60} minutes")

    def save_to_csv(self, file_name: str) -> None:
        df_properties = pd.json_normalize(self.properties)
        df_properties.to_csv(file_name, index=False, encoding="utf-8")
