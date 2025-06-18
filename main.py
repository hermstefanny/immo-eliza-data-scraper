from links_scrapping import listingScrapping


def main():
    listings = listingScrapping()
    listings.call_driver()
    listings.save_to_csv("listing_links.csv")


if __name__ == "__main__":
    main()
