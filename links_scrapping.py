from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from fake_useragent import UserAgent

import time
import random
import csv


class listingScrapping:
    """
    Class that implements the functionalities needed to scrape the URLs listing from https://immovlan.be/en

    """

    def __init__(self) -> None:
        """
        Class constructor that initializes an empty list for links
        """
        self.links = []

    def get_listing_links(self, driver, url: str) -> None:
        """Function to get the urls from each page"""
        driver.get(url)
        time.sleep(random.uniform(3, 5))

        # Click the cookie banner if present
        try:
            accept_button = driver.find_element(By.ID, "didomi-notice-agree-button")
            accept_button.click()

        except Exception as e:
            print(f"{e}: Cookie banner not found")

        try:
            not_now_button = driver.find_element(By.CLASS_NAME, "button-link")
            not_now_button.click()
        except Exception as e:
            print(f"{e} application banner not found")

        page = driver.page_source

        # Transforming to BeautifulSoup
        the_soup = BeautifulSoup(page, "html.parser")

        # Getting all the links from the page

        for card in the_soup.find_all(class_="card-title ellipsis pr-2 mt-1 mb-0"):
            print(card)

            link = card.find("a").get("href")
            print(link)
            self.links.append(link)

    def call_driver(self) -> None:
        """
        Function to move between pages
        """

        # Divide listiings by provinces
        self.provinces = [
            "antwerp",
            "vlaams-brabant",
            "brabant-wallon",
            "east-flanders",
            "west-flanders",
            "hainaut",
            "brussels",
            "liege",
            "limburg",
            "namur",
            "luxembourg",
        ]

        # User agent for driver
        ua = UserAgent()

        # Options for Driver
        options = Options()
        options.add_argument("start-maximized")
        options.add_argument(f"user-agent={ua.random}")
        options.add_argument("--enable-javascript")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option("useAutomationExtension", False)

        # Selenium Driver
        driver = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        driver.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
            },
        )

        # Looping through provinces and 50 first pages for each provinces
        for province in self.provinces:
            for page in range(1, 51):

                listing_url = f"https://immovlan.be/en/real-estate?transactiontypes=for-sale,in-public-sale&propertytypes=house,apartment&provinces={province}&islifeannuity=no&page={str(page)}&noindex=1"

                self.get_listing_links(driver, listing_url)

        driver.close()

    def save_to_csv(self, file_name: str) -> None:
        """
        Function to save links to a csv file
        """
        with open(file_name, "w") as file:
            csv_writer = csv.writer(file)
            for link in self.links:
                csv_writer.writerow([link])
