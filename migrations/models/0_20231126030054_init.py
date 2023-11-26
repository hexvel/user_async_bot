from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `scripts` (
    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `recommendation` BOOL NOT NULL  DEFAULT 0,
    `auto_farm` BOOL NOT NULL  DEFAULT 0,
    `auto_status` BOOL NOT NULL  DEFAULT 0,
    `auto_cover` BOOL NOT NULL  DEFAULT 0,
    `cover_id` INT NOT NULL  DEFAULT 1
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `users` (
    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `token` LONGTEXT NOT NULL,
    `balance` INT NOT NULL  DEFAULT 0,
    `squad` LONGTEXT NOT NULL,
    `rank` INT NOT NULL  DEFAULT 1,
    `username` LONGTEXT NOT NULL,
    `prefix_command` LONGTEXT NOT NULL,
    `prefix_script` LONGTEXT NOT NULL,
    `prefix_admin` LONGTEXT NOT NULL,
    `ignore_list` JSON NOT NULL,
    `trust_list` JSON NOT NULL,
    `profile_photo` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
