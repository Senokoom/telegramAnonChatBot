import tomllib
import os


with open("config.toml", "rb") as f:
    config_data = tomllib.load(f)

local_user_save_path = config_data["path"]["local_user_save_path"]
local_report_save_path = config_data["path"]["local_report_save_path"]
local_ban_save_path = config_data["path"]["local_ban_save_path"]
local_backup_path = config_data["path"]["local_backup_path"]
local_backup_time = config_data["timestamps"]["local_backup_time"]
