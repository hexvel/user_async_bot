from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `users` (
    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `prefix_commands` LONGTEXT NOT NULL,
    `prefix_scripts` LONGTEXT NOT NULL,
    `prefix_admin` LONGTEXT NOT NULL,
    `token` LONGTEXT NOT NULL,
    `token_vkme` LONGTEXT NOT NULL,
    `nickname` LONGTEXT NOT NULL,
    `rank` INT NOT NULL  DEFAULT 0,
    `balance` INT NOT NULL  DEFAULT 0,
    `ignore_list` JSON NOT NULL,
    `trust_list` JSON NOT NULL,
    `trust_prefix` LONGTEXT NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS `users`;"""
