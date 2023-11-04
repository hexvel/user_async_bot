from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `account` (
    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `name` LONGTEXT NOT NULL,
    `surname` LONGTEXT NOT NULL,
    `number` INT NOT NULL,
    `password` LONGTEXT NOT NULL,
    `ref_link` LONGTEXT NOT NULL,
    `username` LONGTEXT NOT NULL,
    `profile_photo_link` LONGTEXT NOT NULL,
    `is_private` BOOL NOT NULL  DEFAULT 0,
    `default_lang` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `account`;"""
