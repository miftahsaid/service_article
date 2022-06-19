import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "1",
    database = "article"
)

mycursor = mydb.cursor() 

mycursor.execute("CREATE TABLE posts (id INT(11) NOT NULL AUTO_INCREMENT,Title VARCHAR(200) NULL DEFAULT NULL ,Content TEXT NULL DEFAULT NULL ,Category VARCHAR(100) NULL DEFAULT NULL ,Created_date TIMESTAMP NULL DEFAULT NULL,Updated_date TIMESTAMP NULL DEFAULT NULL,Status VARCHAR(100) NULL DEFAULT NULL COMMENT 'Publish | Draft | Thrash' ,PRIMARY KEY (id) USING BTREE);")
