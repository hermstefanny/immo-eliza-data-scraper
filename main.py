from links_scrapping import listingScrapping


def main():
    listings = listingScrapping()
    listings.call_driver()
    listings.save_to_csv("listing_links-7-9-prov.csv")


if __name__ == "__main__":
    main()
