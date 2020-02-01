# Laptop Info Scraper

[**Download Here**](https://github.com/VictorSuciu/README-Assets/tree/master/Laptop_Status)

## Description

This program scrapes laptop due dates from Alma and outputs them in a concise list to the terminal. Additionally, it notifies the employee of any due dates that are still at `23:59:00`. Tech desk employees have to manually click on each laptop in Alma to verify green-sheet due dates, so this program saves minutes of tedious clicking. 

## User Instructions

1. [Download](https://github.com/VictorSuciu/README-Assets/tree/master/Laptop_Status) the application folder and unzip it.

2. Run Laptop_Status.exe by double clicking on it.

3. The program will begin running it's own Chrome instance and open the Alma login page.

4. Enter your UW NetID Credentials.

5. The program will begin rapidly navigating Alma and will output laptop info to the terminal.

## Development Dependencies

* Python 2.7 or 3.4+

* Chromedriver Excutable

* Selenium for Python

## Development Installation

1. Install [Selenium](https://pypi.org/project/selenium/) Python package: `pip install selenium`

2. Download the correct [chromedriver](https://chromedriver.chromium.org/downloads) executable for your operating system and version of Chrome.

3. Download `Laptop_Status.py` from this repository.

4. Place `Laptop_Status.py` in a folder.

5. Create another folder next to `Laptop_Status.py` called `driver` an place the chromedriver executable inside.

The project directories should look like this:

```
project/
|
|-- Laptop_Status.py
|-- driver/
    |
    |-- chromedriver.exe
```

## Sample Output

**Note:** The following information is completely fake, and was made up by me. None of the due dates or times reflect real information in the Alma system. This section is meant to showcase the format in which real information would be presented.

```
 1: 8-16  |  6:00 PM
 2: 8-21  | 10:30 PM
 3: 8-05  |  6:00 PM
 4: 8-04  | 10:30 PM
 5: IN
 6: IN
 7: 8-15  | 10:30 PM
 8: 8-14  |  6:00 PM
 9: 8-23  | 10:30 PM
10: 8-17  |  6:00 PM
11: 8-22  | 10:30 PM
12: IN
13: 8-12  | 10:30 PM
14: 8-17  |  6:00 PM
15: 8-02  |  6:00 PM
16: 8-10  | 10:30 PM
17: IN
18: 8-24  |  6:00 PM
19: 8-19  | 10:30 PM
20: IN
21: IN
22: 8-18  |  6:00 PM
23: 8-14  | 10:30 PM
24: IN
25: IN

=======================

   Late Laptops:
   # 3
   # 15

   Laptops Due Today:
   # 13
   # 14

=======================
```