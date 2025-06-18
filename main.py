from links_scrapping import listingScrapping
from property_scrapping import PropertyScrapping


def main():
    # listings = listingScrapping()
    # listings.call_driver()
    # listings.save_to_csv("listing_links.csv")

    scrapping = PropertyScrapping()
    scrapping.open_links_file("listing_links-7-9-prov.csv", 75)
    scrapping.run_scrapping()
    scrapping.save_to_csv("scrapped_properties-7-9.csv")


if __name__ == "__main__":
    main()
