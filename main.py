from links_scrapping import listingScrapping
from property_scrapping import PropertyScrapping
from preliminar_cleaning import PreliminarCleaning
import pandas as pd
import os


def scrape_URLS() -> None:
    """
    Function to obtain the URLS files
    """
    listings = listingScrapping()
    listings.call_driver()
    listings.save_to_csv("data/listing_links.csv")


def scrape_properties(input_file: str, output_file: str) -> None:
    """
    Function to scrape the proeprties listed in the URLs file
    """
    cleaning_links_file = PreliminarCleaning("data/final_links_10-11.csv")

    scrapping = PropertyScrapping()
    scrapping.open_links_file(
        "data/final_links_10-11.csv", cleaning_links_file.url_file_has_header(), 10
    )
    scrapping.run_scrapping()
    scrapping.save_to_csv("data/scrapped_properties_10-11.csv")


def cleaning_files() -> None:
    """
    Function to clean the scrapped files
    """
    cleaning_properties_file = PreliminarCleaning("data/scrapped_properties_1-3.csv")
    print(cleaning_properties_file.open_csv_file())

    properties_file_names = [
        "scrapped_properties_1-3.csv",
        "scrapped_properties_4-6.csv",
        "scrapped_properties_7-9.csv",
        "scrapped_properties_10-11.csv",
    ]

    # Parameters to clean extra attributes

    columns_to_preserve = [
        "furnished",
        "garage",
        "garden",
        "kitchen_equipment",
        "kitchen_type",
        "livable_surface",
        "locality",
        "number_of_bathrooms",
        "number_of_bedrooms",
        "number_of_facades",
        "number_of_floors",
        "price",
        "property_code",
        "property_url",
        "state_of_the_property",
        "surface_garden",
        "surface_terrace",
        "swimming_pool",
        "terrace",
        "total_land_surface",
        "type_of_heating",
        "type_of_property",
    ]

    all_dfs = []
    ## Loop will perform cleaning in each file, dropping out the columns that are garbage attributes, but also
    ## the columns that are deemed unnecessary
    for file in properties_file_names:
        file_path = os.path.join("data", file)
        cleaning_properties_file = PreliminarCleaning(file_path)
        raw_df = cleaning_properties_file.open_csv_file()

        ### Garbage attributes deletion
        column_clean__first_df = cleaning_properties_file.column_cleaning(
            raw_df, cleaning_properties_file.columns_selection(raw_df)
        )
        ### Unnecessary attributes deletion
        columns_to_drop = [
            column
            for column in column_clean__first_df.columns.values
            if column not in columns_to_preserve
        ]
        column_clean_df = cleaning_properties_file.column_cleaning(
            column_clean__first_df, columns_to_drop
        )
        clean_df = cleaning_properties_file.row_cleaning(
            column_clean_df, "property_code"
        )

        all_dfs.append(clean_df)

    total_df = pd.concat(all_dfs, ignore_index=True, sort=True)

    total_df.to_csv("data/final_data.csv", index=False)


def main():
    """Scrapping URLS"""
    # scrape_URLS()

    """Scrapping each property by batches"""
    ## changing manually the name everytime

    # scrape_properties(data/final_links_10-11.csv, data\scrapped_properties_10-11.csv)

    """Performing cleaning of the singular files and obtain a csv"""
    cleaning_files()


if __name__ == "__main__":
    main()
