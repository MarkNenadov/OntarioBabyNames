OntarioBabyNames
================

http://github.com/MarkNenadov/OntarioBabyNames

developed by Mark Nenadov (2013)

A Django web-site based on baby name data (1917-2010) from "Ontario open data".

Please note that the data set used for this excluded names that have less than 5 occurances in a particular year. 

This distribution contains information licensed under the Open Government Licence - Ontario. See the end of this file for a link to details about that license.

--

Basic Instructions

1. Import the SQL schema file babynames.sql into your MySQL (this will take care of both the schema and the baby names data).
2. Setup your Django install with the files included (do not forget to edit the settings.py to reflect your MySQL database). 

--

Optional Instructions

The full set of baby name data is contained the babynames.sql import. That said, if for whatever reason you want to reimport the data directly from the CSV into MySQL again, you can always do that with the code I provided. Here is how you do it:

1. Truncate the baby names table (ie. in the data_monging database, execute "truncate web_babyname").
2. Download the CSV files from "Ontario open data". The links are: http://www.ontario.ca/sites/default/files/opendata/ontariotopbabynames_female_1917-2010_english.csv and http://www.ontario.ca/sites/default/files/opendata/ontariotopbabynames_male_1917-2010_english.csv
3. Edit "importBabyNamesData.py" to include your MySQL server info.
4. Run "importBabyNamesData.py" in the same folder you have the two CSV files stored. There are likely going to be two or three issues you will have to fix in the female CSV data, particularily integer fields that have an extra alpha character in them. Once you run it successfuly, you will then have refreshed the baby name data in MySQL. 

--

The code for this product is licensed under the LGPL. A copy of the LGPL should be included in a file called LICENSE.

The data in the original CSV format (not provided in this software distribution) is licensed under the Open Government License - Ontario (see http://www.ontario.ca/government/open-government-licence-ontario). Under the terms of the license, the CSV data has been translated into MySQL insert statements (which are included in this distribution) 
