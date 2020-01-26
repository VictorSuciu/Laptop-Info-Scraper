# Laptop Info Scraper

## Description

This program scrapes laptop due dates from Alma and outputs them in a concise list to the terminal. Additionally, it notifies the employee of any due dates that are still at `23:59:00`. Tech desk employees have to manually click on each laptop in Alma to verify green-sheet due dates, so this program saves minutes of tedious clicking. 

## Dependencies

* Python 2.7 or 3.4+

* Chromedriver Excutable

* Selenium for Python

## Installation

1. Install [Selenium](https://pypi.org/project/selenium/) Python library: `pip install selenium`

2. Download the correct [chromedriver](https://chromedriver.chromium.org/downloads) executable for your operating system and version of Chrome.

3. Download `Laptop_Status.py` from this repository.

4. Place `Laptop_Status.py` and the chromedriver executable in a common folder.

## Usage

1. Run `Laptop_Status.py` by either:

    a. Opening a terminal window, navigating to inside the folder containing `Laptop_Status.py`, and entering the command: `python Laptop_Status.py` OR

    b. (Windows) Double clicking on `Laptop_Status.py`

2. The program will begin running it's own Chrome instance and open the Alma login page.

3. Enter your UW NetID Credentials.

4. The program will begin rapidly navigating Alma and will output laptop info to the terminal.

## Sample Output

**Note:** The following information is completely fake, and was made up by me. None of the due dates or times reflect real information in the Alma system. This section is meant to showcase the format in which real information would be presented.

```
1:  13/16/2015 |  6:00 PM
2:  13/21/2015 | 11:59 PM <-- Change Due Date
3:  13/05/2015 |  6:00 PM
4:  13/04/2015 | 10:30 PM
5:  IN
6:  IN
7:  13/15/2015 | 10:30 PM
8:  13/14/2015 |  6:00 PM
9:  13/23/2015 | 11:59 PM <-- Change Due Date
10: 13/17/2015 |  6:00 PM
11: 13/22/2015 | 10:30 PM
12: IN
13: 13/12/2015 | 10:30 PM
14: 13/17/2015 |  6:00 PM
15: 13/02/2015 |  6:00 PM
16: 13/10/2015 | 10:30 PM
17: IN
18: 13/24/2015 |  6:00 PM
19: 13/19/2015 | 10:30 PM
20: IN
21: IN
22: 13/18/2015 |  6:00 PM
23: 13/14/2015 | 10:30 PM
24: IN
25: IN
```