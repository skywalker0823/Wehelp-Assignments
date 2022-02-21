
## 要求3
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("John Doe","test","test",1);
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("Kirito","Kirigaya","Kazuto",776);
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("Asuna","Yuuki","Asuna",999);
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("Hisukurifu","Kayaba","Akihiko",1000);
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("Tzu Hsuan Yang","admin","admin",777);
![3-1](https://user-images.githubusercontent.com/56625237/150732310-67d1defc-da23-43f6-bf8c-3ee0ce855476.PNG)

SELECT * FROM `member`;
![3-2](https://user-images.githubusercontent.com/56625237/150732366-0f5f8def-e998-4a8e-a9f3-83cb2095ff5f.PNG)

SELECT * FROM `member` ORDER BY `time` DESC;
![3-3](https://user-images.githubusercontent.com/56625237/150732395-7caf056a-3465-49a4-965c-2c0abf6c6af2.PNG)

SELECT * FROM `member` ORDER BY `time` DESC LIMIT 1,3;
![3-4](https://user-images.githubusercontent.com/56625237/150732404-59a9326f-e2e9-41a8-801a-8f0dab8f8e96.PNG)

SELECT * FROM `member` WHERE `username`="test";
![3-5](https://user-images.githubusercontent.com/56625237/150732416-bdc50d3d-3457-4322-ad27-58f5857accea.PNG)

SELECT * FROM `member` WHERE `username`="test" AND `password`="test";
![3-6](https://user-images.githubusercontent.com/56625237/150732423-c13a67d7-c09e-4f0c-ba82-a45ac93a14cb.PNG)

UPDATE `member` SET `name`="test2" WHERE `username`="test";
![3-7](https://user-images.githubusercontent.com/56625237/150732436-0a75ffa6-3466-4750-8c5d-e376445315b7.PNG)



## 要求4
SELECT COUNT(*) FROM `member`;
![4-1](https://user-images.githubusercontent.com/56625237/150732464-c80338e0-a2bc-4826-82d4-39cb2df0e772.PNG)

SELECT SUM(`follower_count`) FROM `member`; 這張沒截好 請看下一張ＱＱ
![4-2](https://user-images.githubusercontent.com/56625237/150732477-8ef3e56b-5e4a-4028-b6e7-861f8748bae9.PNG)

SELECT AVG(`follower_count`) FROM `member`;
![4-3](https://user-images.githubusercontent.com/56625237/150732483-1d6dead1-86fd-4c59-a519-ab3f37d11484.PNG)



## 要求5-1
CREATE TABLE `message` (
 `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
 `member_id` BIGINT NOT NULL ,
 `content` VARCHAR(255) NOT NULL,
 `time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(`member_id`) REFERENCES member(`id`)
);
![5-1](https://user-images.githubusercontent.com/56625237/150732507-3e4188f3-e512-4aad-b4c2-f46a9e451b55.PNG)


### 自我發揮橋段
DESCRIBE `message`;
SELECT * FROM `message`;
INSERT INTO `message` (`member_id`,`content`) VALUES(1,"慘 怎麼上傳作業比作業本身還難");
INSERT INTO `message` (`member_id`,`content`) VALUES(2,"A TRUE NO-BODY");
INSERT INTO `message` (`member_id`,`content`) VALUES(3,"幫我稱十秒");
INSERT INTO `message` (`member_id`,`content`) VALUES(4,"我不是公車!");
INSERT INTO `message` (`member_id`,`content`) VALUES(5,"這雖然是遊戲，但可不是鬧著玩的");

## 要求5-2
SELECT `member`.`id`,`member`.`name`,`message`.`content`
FROM `member` JOIN `message`
ON `member`.`id`=`message`.`member_id`;
![5-2](https://user-images.githubusercontent.com/56625237/150732521-1064fb3a-6d5b-4cbe-bc75-91073304b3da.PNG)

## 要求5-3
SELECT `member`.`username`,`message`.`content`
FROM `member` JOIN `message`
ON `member`.`id`=`message`.`member_id`
WHERE `username`="test";
![5-3](https://user-images.githubusercontent.com/56625237/150732526-b78715c5-6f7d-4b20-857c-505261380198.PNG)


