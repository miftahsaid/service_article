# service_article
#buat database article
CREATE DATABASE IF NOT EXISTS article

#buat table posts
CREATE TABLE `posts` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`Title` VARCHAR(200) NULL DEFAULT NULL ,
	`Content` TEXT NULL DEFAULT NULL ,
	`Category` VARCHAR(100) NULL DEFAULT NULL ,
	`Created_date` TIMESTAMP NULL DEFAULT NULL,
	`Updated_date` TIMESTAMP NULL DEFAULT NULL,
	`Status` VARCHAR(100) NULL DEFAULT NULL COMMENT 'Publish | Draft | Thrash' ,
	PRIMARY KEY (`id`) USING BTREE
);


#set database mysql 
config/db.py

#install virtualenv 
#LINUX
sudo apt install python3-virtualenv


#activate env
source venv/bin/activate 
pip install fastapi sqlalchemy pymysql uvicorn
uvicorn index:app --reload
- lalu jalankan http yang terbentuk oleh uvicorn.
