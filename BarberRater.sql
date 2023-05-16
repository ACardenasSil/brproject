DROP TABLE IF EXISTS `User`;
DROP TABLE IF EXISTS `Shop`;
DROP TABLE IF EXISTS `Barber`;


CREATE TABLE `User` ( 
 `User_ID` int(11) NOT NULL AUTO_INCREMENT,
 `User_FirstName` varchar(255) NOT NULL DEFAULT '0',
 `User_LastName` varchar(255) NOT NULL DEFAULT '0',
 `Username` varchar(255) NOT NULL DEFAULT '0',
 `Email` varchar(255) NOT NULL DEFAULT '0',
 `Phone` varchar(18) NOT NULL DEFAULT '0',
 `Password` varchar(255) NOT NULL DEFAULT '0',
 `image_path` text,
 PRIMARY KEY (`User_ID`) 
);
CREATE TABLE `Shop` (
 `Shop_ID` int(11) NOT NULL AUTO_INCREMENT,
 `Name` varchar(255),
 `Address` varchar(255),
 `Zipcode` varchar(255),
 `image_path` text,
 PRIMARY KEY (`Shop_ID`)
);
CREATE TABLE `Barber` (
 `Barber_ID` int(11) NOT NULL AUTO_INCREMENT,
 `User_ID` int(11) NOT NULL,
 `Shop_ID` int(11) NOT NULL DEFAULT '1',
 PRIMARY KEY (`Barber_ID`),
 FOREIGN KEY (`User_ID`) REFERENCES User(`User_ID`),
 FOREIGN KEY (`Shop_ID`) REFERENCES Shop(`Shop_ID`)
);
CREATE TABLE `Review` (
 `Review_ID` int(11) NOT NULL AUTO_INCREMENT,
 `Barber_ID` int(11) NOT NULL,
 `Client_ID` int(11) NOT NULL,
 `Rating` int(1) NOT NULL,
 `Review_Text` text,
 `image_path` text,
 PRIMARY KEY (`Review_ID`),
 FOREIGN KEY (`Barber_ID`) REFERENCES Barber(`Barber_ID`),
 FOREIGN KEY (`Client_ID`) REFERENCES User(`User_ID`)
);