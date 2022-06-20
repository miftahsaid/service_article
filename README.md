# service_article <br>
#buat database article <br>
CREATE DATABASE IF NOT EXISTS article <br>

#buat table posts <br>
CREATE TABLE `posts` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`Title` VARCHAR(200) NULL DEFAULT NULL ,
	`Content` TEXT NULL DEFAULT NULL ,
	`Category` VARCHAR(100) NULL DEFAULT NULL ,
	`Created_date` TIMESTAMP NULL DEFAULT NULL,
	`Updated_date` TIMESTAMP NULL DEFAULT NULL,
	`Status` VARCHAR(100) NULL DEFAULT NULL COMMENT 'Publish | Draft | Thrash' ,
	PRIMARY KEY (`id`) USING BTREE
); <br>
<br>

#config database mysql  <br>
config/db.py <br>
<br>
#install virtualenv  <br>
#LINUX <br>
sudo apt install python3-virtualenv <br>
 <br>
 <br>
#activate env <br>
source venv/bin/activate  <br>
pip install fastapi sqlalchemy pymysql uvicorn <br>
uvicorn index:app --reload <br>
- lalu jalankan http yang terbentuk oleh uvicorn. <br>

#install virtualenv  <br>
#WINDOWS <br>
py -m pip install --upgrade pip <br>
py -m pip install --user virtualenv <br>

#activate env <br>
py -m venv env <br>
.\env\Scripts\activate <br>
pip install fastapi sqlalchemy pymysql uvicorn <br>
uvicorn index:app --reload <br>
<br>
<br>
#service request postman <br>
- service_article.postman_collection.json <br>
