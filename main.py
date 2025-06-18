from links_scrapping import listingScrapping
from property_scrapping import PropertyScrapping
from preliminar_cleaning import PreliminarCleaning


def main():
    # listings = listingScrapping()
    # listings.call_driver()
    # listings.save_to_csv("data/listing_links.csv")

    cleaning = PreliminarCleaning("data/final_links_10-11.csv")
    scrapping = PropertyScrapping()
    scrapping.open_links_file(
        "data/final_links_10-11.csv", cleaning.file_has_header(), 10
    )
    scrapping.run_scrapping()
    scrapping.save_to_csv("data/scrapped_properties_10-11.csv")


if __name__ == "__main__":
    main()
