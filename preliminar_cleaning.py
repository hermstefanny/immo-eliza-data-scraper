from typing import List
import pandas as pd
import os


class PreliminarCleaning:
    """
    Class that implements functionalities to perform cleaning on the properties data
    """

    def __init__(self, file_name: str) -> None:
        """
        Class constructor
        """
        self.file_name = file_name
        self.has_header = True

    def url_file_has_header(self) -> bool:
        """
        Function-utility to understand if a url file has header
        """
        with open(self.file_name, "r", encoding="utf-8") as f:
            sample = f.readline()
            return "http" not in sample.lower()

    def open_csv_file(self) -> pd:
        """
        Function to open a properties file
        """
        try:
            if self.has_header:
                df = pd.read_csv(self.file_name, header=0)
            else:
                df = pd.read_csv(self.file_name, header=None)

        except Exception as e:
            print(f"Error {e}")

        return df

    def removing_urls(self, string_to_remove: str, df: pd) -> pd:
        """
        Function to remove urls from urls files according to a specific parameter
        """
        try:
            final_df = df[~df.iloc[:, 0].str.contains(string_to_remove)]

        except Exception as e:
            print(f"Error {e}")

        return final_df

    def save_to_csv(self, df: pd, outfile_name: str) -> None:
        """
        Function to save a dataframe to csv
        """
        df.to_csv(outfile_name, index=False, header=False)

    def column_cleaning(
        self, df: pd, columns_to_clean: List[str], in_place: bool = False
    ) -> pd:
        """
        Function to drop columns when passed a list of names
        """
        try:
            df = df.drop(columns=columns_to_clean, inplace=in_place)

        except Exception as e:
            print(f"Error {e}")

        # dropping columns that have less than 10% values
        clean_pd = df.dropna(axis=1, thresh=0.10 * len(df))
        return clean_pd

    def row_cleaning(self, df: pd, attribute_to_check) -> pd:
        """
        Function to drop properties if certain attribute is not existent
        """
        return df[~df[attribute_to_check].isnull()]

    def columns_selection(self, df: pd) -> List[str]:
        """
        Function that defines which columns to drop from dataset
        """
        columns_to_eliminate = []
        all_columns = list(df.columns.values)

        columns_to_eliminate = [
            column
            for column in all_columns
            if column.endswith(
                (".pdf", ".png", ".jpg", "jpeg", "docx", "termsandconditions")
            )
        ]

        columns_2 = [
            column for column in all_columns if column.startswith("documents?id")
        ]
        columns_to_eliminate.extend(columns_2)

        columns_3 = [column for column in all_columns if "score_represents" in column]

        columns_to_eliminate.extend(columns_3)

        print(len(columns_to_eliminate))

        return columns_to_eliminate
