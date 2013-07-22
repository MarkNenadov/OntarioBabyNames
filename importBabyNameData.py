import sys
import MySQLdb

DB_HOST = "localhost"
DB_USER = "mark"
DB_PASSWORD = "data9"
DB_NAME = "data_monging"

def insertCsvLineIntoDb( gender, record, cursor ):
   name = record.split( "," )[1]
   year = record.split( "," )[0]
   occurances = record.split( "," )[2].replace("\r\n","")
   name = record.split( "," )[1]
   if year.isdigit():
        sql = "INSERT INTO web_baby_name_year (name, year, occurances, gender) VALUES (\"" + name + "\", " + year + " , " + occurances + ", '" + gender + "' )"
        try:
            unicode( sql, 'ISO-8859-1' )
            cursor.execute( sql )
        except UnicodeEncodeError:
            print( "record skipped due to encoding error ["+name+"]" )
mysql = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASSWORD, db=DB_NAME)
cursor = mysql.cursor()

maleCsvFileName = "ontariotopbabynames_male_1917-2010_english.csv"
maleCsvFile = open( maleCsvFileName, "r" )
maleCsvRecords = maleCsvFile.readlines()

femaleCsvFileName = "ontariotopbabynames_female_1917-2010_english.csv"
femaleCsvFile = open( femaleCsvFileName, "r" )
femaleCsvRecords = femaleCsvFile.readlines()

print( "importBabyNamesData.py is importing " + str( len( maleCsvRecords ) + len( femaleCsvRecords ) ) + " CSV records " )

for maleRecord in maleCsvRecords:
    insertCsvLineIntoDb( "M", maleRecord, cursor )

for femaleRecord in femaleCsvRecords:
    insertCsvLineIntoDb( "F", femaleRecord, cursor )

