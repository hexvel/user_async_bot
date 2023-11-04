from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `aliases` (
    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `new_command` LONGTEXT NOT NULL,
    `command` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;
        CREATE TABLE IF NOT EXISTS `scripts` (
    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `auto_farm` INT NOT NULL  DEFAULT 0,
    `auto_status` INT NOT NULL  DEFAULT 0,
    `auto_status_stamp` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;
        CREATE TABLE IF NOT EXISTS `templates` (
    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` LONGTEXT NOT NULL,
    `message` LONGTEXT NOT NULL,
    `type` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `aliases`;
        DROP TABLE IF EXISTS `scripts`;
        DROP TABLE IF EXISTS `templates`;"""
