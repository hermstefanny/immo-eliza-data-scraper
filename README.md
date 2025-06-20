# Immo-Eliza Web Scraper

## Introduction

This project scraps data from individual properties for sale available on: https://immovlan.be/en

This project implements:

- Scrapping
- Data cleaning
- csv files handling
- pandas

## Description

The properties are selected with the following constraints:

- Properties are either classifed as house or apartment
- Annuity living properties (living sales) are not taken into account
- Projects (not completed) are not taken into account

This project contains:

- Jupyter Notebooks: All .ipynb files are drafts made for testing
- Python files:
  - _links_scrapping.py_: Implements the listingScrapping class to scrape the listings from the website.
  - _property_scrapping.py_: Implements the PropertyScrapping class to scrape each individual property
  - _preliminar_cleaning.py_: Implements the PreliminarCleaning class that contains utilities to perform cleaning of non-necessary attributes from the scrapped properties
  - _main.py_: Implements the logic for scrapping urls, properties and performing cleaning
- data <directory>: csv files with both URLs data and properties data
  - _listing_links(n).csv_ files: each file contains a subsection of the raw scrapped urls for the properties listing
  - _final_links(n).csv_ files: each file contains a subsection of the clean (without 'projects' links) scrapped urls for the properties listing
  - _scrapped_properties(n).csv_ files: each file contains a subsection of the scrapped properties attributes for the properties listing
  - _final_listing_links.csv_:contains the totality of raw URLS
  - _complete_listing_links.csv_:contains the totality of clean (without 'projects' links) URLS
  - _final_data.csv_: contains the totality of clean properties attributes

## Requirements

- Python version: Python 3.10.4
- Recommended IDE : VsCode with Jupyter Notebook extension.

## Installation

1. Clone the directory from its repository
2. Create a Python virtual environment using the requirements file in this directory:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use venv\Scripts\activate
   python -m pip install -r requirements.txt
   ```

### Usage

### Jupyter notebooks

1.  Run the cells one by one as needed

**IMPORTANT**: These notebooks are not intended to be final products, but mere drafts. Therefore, they are not mean to be run to scrap, clean or process data

### Python files

1. Open your terminal in the appropiate directory
2. Run the file with _python main.py_

**IMPORTANT** Running the Python file will overwrite the csv files
