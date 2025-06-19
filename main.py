from links_scrapping import listingScrapping
from property_scrapping import PropertyScrapping
from preliminar_cleaning import PreliminarCleaning


def main():

    # Scrapping URLS
    ## listings = listingScrapping()
    ## listings.call_driver()
    ## listings.save_to_csv("data/listing_links.csv")

    # Scrapping each property
    # cleaning_links_file = PreliminarCleaning("data/final_links_10-11.csv")

    # scrapping = PropertyScrapping()
    # scrapping.open_links_file(
    #    "data/final_links_10-11.csv", cleaning_links_file.file_has_header(), 10
    # )
    # scrapping.run_scrapping()
    # scrapping.save_to_csv("data/scrapped_properties_10-11.csv")

    cleaning_properties_file = PreliminarCleaning("data/scrapped_properties_1-3.csv")
    print(cleaning_properties_file.open_csv_file())

    properties_file_names = [
        "scrapped_properties_1-3.csv",
        "scrapped_properties_4-6.csv",
        "scrapped_properties_7-9.csv",
        "scrapped_properties_10-11.csv",
    ]


if __name__ == "__main__":
    main()
