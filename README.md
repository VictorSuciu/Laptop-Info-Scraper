# Laptop Info Scraper

## Description

Scrapes laptop due dates from Alma and outputs them in a concise list to the terminal. Tech desk employees have to manually click on each laptop to verify green-sheet due dates, and this program saves minutes of tedious clicking.

## Dependencies

* Chromedriver Excutable

* Selenium for Python

## Installation

1. Install the Selenium Python library: `pip install selenium`

2. [Download](https://chromedriver.chromium.org/downloads) the correct chromedriver executable for your operating system and version of Chrome.

3. Download `Laptop_Status.py` from this repository.

4. Place `Laptop_Status.py` and the chromedriver executable in a common folder.

## Usage

1. Open a terminal window, navigate to inside the folder containing `Laptop_Status.py`.

2. Enter `python Laptop_Status.py` into the terminal.

3. The program will begin running it's own Chrome instance and output laptop info to the terminal.
