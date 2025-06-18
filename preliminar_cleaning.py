import pandas as pd


class PreliminarCleaning:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.has_header = False

    def file_has_header(self) -> None:
        with open(self.file_name, "r", encoding="utf-8") as f:
            sample = f.readline()
            self.has_header = "http" not in sample.lower()

    def open_csv_file(self) -> pd:

        try:
            if self.has_header:
                urls_df = pd.read_csv(self.file_name, header=0)
            else:
                urls_df = pd.read_csv(self.file_name, header=None)

        except Exception as e:
            print(f"Error {e}")

        return urls_df

    def removing_urls(self, string_to_remove: str, df: pd) -> pd:

        try:
            final_df = df[~df.iloc[:, 0].str.contains(string_to_remove)]

        except Exception as e:
            print(f"Error {e}")

        return final_df

    def save_to_csv(self, df: pd, outfile_name: str) -> None:
        df.to_csv(outfile_name, index=False, header=False)


if __name__ == "__main__":
    cleaning = PreliminarCleaning("listing_links-10-11.csv")
    preliminar_df = cleaning.open_csv_file()
    final_df = cleaning.removing_urls("project", preliminar_df)
    cleaning.save_to_csv(final_df, "final_links_10-11.csv")
