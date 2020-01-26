# Laptop Info Scraper

## Description

This program scrapes laptop due dates from Alma and outputs them in a concise list to the terminal. Additionally, it notifies the employee of any due dates that are still at `23:59:00`. Tech desk employees have to manually click on each laptop in Alma to verify green-sheet due dates, so this program saves minutes of tedious clicking. 

## Dependencies

* Chromedriver Excutable

* Selenium for Python

## Installation

1. Install the Selenium Python library: `pip install selenium`

2. [Download](https://chromedriver.chromium.org/downloads) the correct chromedriver executable for your operating system and version of Chrome.

3. Download `Laptop_Status.py` from this repository.

4. Place `Laptop_Status.py` and the chromedriver executable in a common folder.

## Usage

1. Run `Laptop_Status.py` by either:

    a. Opening a terminal window, navigating to inside the folder containing `Laptop_Status.py`, and entering the command: `python Laptop_Status.py` OR

    b. (Windows) Double clicking on `Laptop_Status.py`

2. The program will begin running it's own Chrome instance.

3. Enter your UW NetID Credentials.

4. The program will begin rapidly navigating Alma and will output laptop info to the terminal.
