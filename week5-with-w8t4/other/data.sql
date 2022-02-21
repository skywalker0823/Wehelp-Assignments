USE `website`;
DROP TABLE `member`;
describe `member`;

SELECT * FROM `member`;

SET SQL_SAFE_UPDATES = 0;
-- 要求2(已經在terminal中練習過拉QQ)
CREATE TABLE `member` (
 `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
 `name` VARCHAR(255) NOT NULL,
 `username` VARCHAR(255) NOT NULL,
 `password` VARCHAR(255) NOT NULL,
 `follower_count` INT NOT NULL DEFAULT 0,
 `time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- 要求3
-- 使用 INSERT 指令新增一筆資料到 member 資料表中，這筆資料的 username 和 password 欄位必須是 test。接著繼續新增至少 4 筆隨意的資料
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("John Doe","test","test",1);
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("Kirito","Kirigaya","Kazuto",776);
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("Asuna","Yuuki","Asuna",999);
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("Hisukurifu","Kayaba","Akihiko",1000);
INSERT INTO `member` (`name`,`username`,`password`,`follower_count`) VALUES("Tzu Hsuan Yang","admin","admin",777);
-- 使用 SELECT 指令取得所有在 member 資料表中的會員資料
SELECT * FROM `member`;
-- 使用 SELECT 指令取得所有在 member 資料表中的會員資料，並按照 time 欄位，由近到遠排序
SELECT * FROM `member` ORDER BY `time` DESC;
-- 使用 SELECT 指令取得 member 資料表中第 2 ~ 4 共三筆資料，並按照 time 欄位，由近到遠排序。( 並非編號 2、3、4 的資料，而是排序後的第 2 ~ 4 筆資料 )
SELECT * FROM `member` ORDER BY `time` DESC LIMIT 1,3;
-- 使用 SELECT 指令取得欄位 username 是 test 的會員資料
SELECT * FROM `member` WHERE `username`="test";
-- 使用 SELECT 指令取得欄位 username 是 test、且欄位 password 也是 test 的資料
SELECT * FROM `member` WHERE `username`="test" AND `password`="test";
-- 使用 UPDATE 指令更新欄位 username 是 test 的會員資料，將資料中的 name 欄位改成 test2
UPDATE `member` SET `name`="test2" WHERE `username`="test";


-- 要求4
-- 取得 member 資料表中，總共有幾筆資料 ( 幾位會員 )
SELECT COUNT(*) FROM `member`;
-- 取得 member 資料表中，所有會員 follower_count 欄位的總和
SELECT SUM(`follower_count`) FROM `member`;
-- 取得 member 資料表中，所有會員 follower_count 欄位的平均數
SELECT AVG(`follower_count`) FROM `member`;


-- 要求5
-- 在資料庫中，建立新資料表，取名字為 message
CREATE TABLE `message` (
 `id` BIGINT AUTO_INCREMENT PRIMARY KEY,
 `member_id` BIGINT NOT NULL ,
 `content` VARCHAR(255) NOT NULL,
 `time` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
 FOREIGN KEY(`member_id`) REFERENCES member(`id`)
);

-- 自我發揮橋段
DESCRIBE `message`;
SELECT * FROM `message`;
INSERT INTO `message` (`member_id`,`content`) VALUES(1,"慘 怎麼上傳作業比作業本身還難");
INSERT INTO `message` (`member_id`,`content`) VALUES(2,"A TRUE NO-BODY");
INSERT INTO `message` (`member_id`,`content`) VALUES(3,"幫我稱十秒");
INSERT INTO `message` (`member_id`,`content`) VALUES(4,"我不是公車!");
INSERT INTO `message` (`member_id`,`content`) VALUES(5,"這雖然是遊戲，但可不是鬧著玩的");



-- 使用 SELECT 搭配 JOIN 語法，取得所有留言，結果須包含留言者會員的姓名
SELECT `member`.`id`,`member`.`name`,`message`.`content`
FROM `member` JOIN `message`
ON `member`.`id`=`message`.`member_id`;

-- 使用 SELECT 搭配 JOIN 語法，取得 member 資料表中欄位 username 是 test 的所有留言，資料中須包含留言者會員的姓名
SELECT `member`.`username`,`message`.`content`
FROM `member` JOIN `message`
ON `member`.`id`=`message`.`member_id`
WHERE `username`="test";
