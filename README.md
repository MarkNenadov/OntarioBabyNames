OntarioBabyNames
================

A Django web-site based on baby name data (1917-2010) from "Ontario open data".

--

Instructions.

1. Note: This product does not come with the baby data. You need to download the data and use the included Python code to import the CSV into MySQL. Download http://www.ontario.ca/sites/default/files/opendata/ontariotopbabynames_female_1917-2010_english.csv and http://www.ontario.ca/sites/default/files/opendata/ontariotopbabynames_male_1917-2010_english.csv
2. Import the SQL schema file babynames.sql into your MySQL.
3. Edit "importBabyNameData.py" to include your MySQL server info.
4. Run "importBabyNamesData.py" in the same folder as these two CSV files.
5. Setup your Django install with the files included (don't forget to edit the settings.py to reflect your MySQL database). 

--

by Mark Nenadov (2013) - This product is licensed under the LGPL. A copy of the LGPL should be included in a file called LICENSE.
