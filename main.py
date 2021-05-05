# -*- coding: utf-8 -*-
"""
Created on Wed May  5 16:34:12 2021

@author: FarhanAshraf
"""

f = open('Desktop/abc.pdf', 'rb') #I have changed the file name to abc.pdf

import PyPDF2  #pip install PyPDF2 (third party library)  I have used it, we can go with other library as well.

file = PyPDF2.PdfFileReader(f)

page1 = file.getPage(0)  #selects the page

pdfData = page1.extractText()  #returns string containing entire text of the page


#below are the parameters to be populated in db schema, we are assigning them into variables.
L = pdfData.split(" ")
naam = L[4]
years = L[7][1:]
dr = L[16]


#below code is for figuring out gender
#as Male is merged with the last name in the string pdfData, I am using regex to fetch out gender and check whether it is male or female.


import re 

sir_name = re.search('Male', L[5])
if (sir_name.group()) == 'Male':
    gen = 'Male'
elif (sir_name.group()) == 'Female':
    gen = 'Female'


#Establishing Database connection
#we need to create a database with name 'db' and a table name: patient 
import mysql.connector
db = mysql.connector.connect(host = 'localhost', user='root', password='root', database='db')  #password should be yours, otherwise access denied error will come.

cur = db.cursor()

s = "INSERT INTO patient (patient_name, sex, age, Ref_by_DR) VALUES(%s, %s, %s, %s)"  #writing query statement

val = (naam, gen, years, dr)
cur.execute(s, val)

db.commit()  #comitting changes. Done.
