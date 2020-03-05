 #  Salaries is a file that includes salary data on special force community. It includes employees name position, salary, etc...
#  importing the csv file: each row is a dictionary
"""
What: Moving data from csv to Sqlite
When: Feb 20, 2020 
Who: Alwatheq Zboun
"""
import csv               #Impport csv python module    
import sqlite3
import sys

DB_FILE = 'Salaries.db'  #Create database file
conn = sqlite3.connect(DB_FILE) # connect to the database file 
  
def create_table():
    """This will be where the csv data loaded to 
    """
    c = conn.cursor()
    str_sql = """
        CREATE TABLE if not exists employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            EmployeeName text,
            JobTitle text,
            BasePay float,
            Agency text
        );
        """
    c.execute(str_sql)
    conn.commit()

def open_cvs_insert_intodb():
    cur=conn.cursor()
    row_count= 0
    with open('Salaries.csv', 'r') as csv_fi:
        reader = csv.DictReader(csv_fi)
        for SalariesDic in reader:
            row_count += 1
            ### extract each var from dicitionary 
            t_name = SalariesDic['EmployeeName']
            t_salary=SalariesDic['BasePay']
            t_agency = SalariesDic['Agency']
            t_job = SalariesDic['JobTitle']
            ### sql str, data tuple execute &commit
            sql_str_insert_with_param = """
                INSERT INTO employees
                    (EmployeeName,BasePay,Agency,JobTitle)
                VALUES
                    (?,?,?,?);
                    """
            data_tuple =(t_name,t_salary,t_agency,t_job)
            cur.execute(sql_str_insert_with_param, data_tuple)
            conn.commit()
            ### print data to the use so they know where they are in processing 
            if row_count <= 10 or row_count % 100000 == 0: 
                print('{0:>6} Name: {1:<50}   Title:  {2:<50}       Agency:{3: <20}' .format(
                     row_count, t_name, t_job,  t_salary, t_agency))
    cur.close()
        
def main():
    create_table()
    open_cvs_insert_intodb()
    conn.close() 

if __name__ == "__main__":
    main()


   




