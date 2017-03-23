#!/usr/bin/python
# -*- coding: utf-8 -*-

import cx_Oracle
import impala.dbapi

#from impala.dbapi import connect
from impala.util import as_pandas

# Convenience classes

class Database(object):
    
    def __init__(self):
        """ The constructor for the class 'Database'.
            
            Args:
            N/A
            
            Returns (Database):
            An instance of 'Database'.
            """
        
        self.platform = input("Enter data platform: ").upper()
        if self.platform in ['HADOOP', 'HIVE', 'IMPALA']:
            self.host = 'DNS_HOSTNAME_PLACEHOLDER'
            self.port = 10000
        elif self.platform == 'ORACLE':
            self.host = 'DNS_HOSTNAME_PLACEHOLDER'
            self.port = 1521

    def connect(self, srvc):
        """ Returns a database connection object.
        
        Args:
        srvc (str): A database service name (Oracle only).
        
        Returns (Settings):
        A database connection object.
        """
    
        person = Person()
        if self.platform in ['HADOOP', 'HIVE', 'IMPALA']:
            return impala.dbapi.connect(host=self.host,
                                        port=self.port,
                                        auth_mechanism='PLAIN',
                                        user=person.user,
                                        password=person.password)
        elif self.platform == 'ORACLE':
            return cx_Oracle.connect("%s/%s@%s/%s" % (person.user, person.password, self.host, srvc))

class Person(object):
    
    def __init__(self):
        """ The constructor for the class 'Person'.
            
        Args:
        N/A
            
        Returns (Person):
        An instance of 'Person'.
        """

        self.user = input("Enter username: ")
        self.password = input("Enter password: ")

def main():

    # Load database settings.

    db = Database()

    # Specify query.
    
    srce_db = input("Enter database name -- e.g. 'EDWSTATS': ")
    srce_tbl = input("Enter table name -- e.g. 'L_QC_COLUMN_RESULT': ")

    query_template = '''
    SELECT COUNT(*) AS row_count
    FROM {}.{}
    '''
    
    query = query_template.format(srce_db, srce_tbl)

    # Connect to database.

    conn = db.connect('ds01')
    
    # Execute query.
    
    cur = conn.cursor()
    cur.execute(query)

    conn.commit();

    # Convert query results to data frame.
    
    df = as_pandas(cur)
    
    # Disconnect from database.
    
    conn.close()
    
    # Demo some basic data frame operations.
    # For more info, see:
    # http://www.datadependence.com/2016/05/scientific-python-pandas/
    
    result1 = df.head(1)  # Show first row.
    result2 = df.head(2)  # Show first 2 rows.
    result3 = df.tail(1)  # Show last row.
    result4 = len(df)     # Show # of rows.
    result5 = df.describe # Show data frame summary stats

    print("df.head(1) = {}".format(result1))
    print("df.head(2) = {}".format(result2))
    print("df.tail(1) = {}".format(result3))
    print("len(df) = {}".format(result4))
    print("df.describe = {}".format(result5))

# NOTE: For unit testing purposes, execute as self-test only if being run as a top-level script.
if __name__ == "__main__":
    main()
