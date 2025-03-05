# Basic Student Data Management (Tkinter + MySQL)
This is a Tkinter-based GUI application that allows users to insert student data into a MySQL database and view the stored records in a tabular format.

Features
-Fetches and displays student records in a table view
-User-friendly GUI using Tkinter
-Inserts student name and password into MySQL database

Installation
Setup MySQL Database
1. Open MySQL and create a database:
   CREATE DATABASE tkinter1;
2. Switch to the database:
   USE tkinter1;
3. Create the student table:
   CREATE TABLE student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL
   );

Usage
1. Enter Name and Password in the GUI form
2. Click Submit to insert data into the MySQL database
3. The data will be displayed in a new window with a table view
