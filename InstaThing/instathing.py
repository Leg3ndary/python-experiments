"""
Made for learning python, I don't use this.
"""

import json
import logging
import logging.handlers
import os
import random
import time

import colorama
import instagrapi
from dotenv import load_dotenv

load_dotenv()


class Insta:
    """
    Insta client for accessing main methods
    """

    def __init__(self) -> None:
        self.insta = instagrapi.Client()
        self.insta.load_settings("hidden/insta_settings.json")
        self.insta.login(os.getenv("user"), os.getenv("pass"))
        print(f"Logged in as {self.insta.username}")
        # self.log = logging.basicConfig(filename="insta.log", filemode="w", level=logging.INFO)

        handler = logging.handlers.WatchedFileHandler(
            os.environ.get("LOGFILE", "hidden/insta.log")
        )
        formatter = logging.Formatter(logging.BASIC_FORMAT)
        handler.setFormatter(formatter)
        self.log = logging.getLogger()
        self.log.setLevel(os.environ.get("LOGLEVEL", "INFO"))
        self.log.addHandler(handler)
        # self.insta.dump_settings("hidden/insta_settings.json")
        print("Saved latest settings")

    def sleep_random(self) -> None:
        """
        Sleep for a random amount of time
        """
        time.sleep(random.randint(1, 6))
        return

    def follow_check(self, userid: str) -> None:
        """
        Check if we should follow a user based on things in their bio
        """

    def save_account(self, username: str) -> None:
        with open(f"hidden/{username}.json", "w") as file:
            userid = self.insta.user_id_from_username(username)
            data = self.insta.user_followers(userid, True, 0)
            new_dict = {}
            for key, value in data.items():
                if not isinstance(value, str):
                    # Found a user short
                    new_dict[key] = {
                        "pk": value.pk,
                        "username": value.username,
                        "is_private": value.is_private,
                    }
                else:
                    new_dict[key] = value
            json.dump(new_dict, file, indent=4, sort_keys=True)

    def should_i_follow(self, data: dict) -> None:
        """
        Should I follow lmao
        """
        for key, value in data.items():
            ignore = [
                "07",
                "08",
                "vote",
                "2025",
                "2026",
                "exec",
                "aphs",
                "hdsb",
                "burlington",
                "oakville",
                "halton",
            ]
            follow = ["06", "05", "04"]

            if not value["is_private"]:
                print(
                    f"[ {colorama.Fore.RED}Avoided{colorama.Style.RESET_ALL} ]  {colorama.Fore.CYAN}{value['username']}{colorama.Style.RESET_ALL} | Reason: PUBLIC ACCOUNT"
                )
                self.log.info(f"Avoided : {value['username']} | Reason: PUBLIC ACCOUNT")

            elif any(kw in value["username"] for kw in ignore):
                print(
                    f"[ {colorama.Fore.RED}Avoided{colorama.Style.RESET_ALL} ]  {colorama.Fore.CYAN}{value['username']}{colorama.Style.RESET_ALL} | Reason: USERNAME"
                )
                self.log.info(f"Avoided : {value['username']} | Reason: USERNAME")

            elif any(kw in value["username"] for kw in follow):
                followed = self.insta.user_follow(key)
                if followed:
                    print(
                        f"[ {colorama.Fore.GREEN}Followed{colorama.Style.RESET_ALL} ] {colorama.Fore.CYAN}{value['username']}{colorama.Style.RESET_ALL} | Reason: USERNAME"
                    )
                    self.log.info(f"Followed: {value['username']} | Reason: USERNAME")
                else:
                    print(
                        f"[ {colorama.Fore.RED}Failed{colorama.Style.RESET_ALL} ]   {colorama.Fore.CYAN}{value['username']}{colorama.Style.RESET_ALL} | Reason: FOLLOW FAIL"
                    )
                    self.log.info(
                        f"Failed:   {value['username']} | Reason: FOLLOW FAIL"
                    )
                self.sleep_random()
            else:
                user_data = self.insta.user_info_by_username(value["username"])
                if (
                    "06" in user_data.biography
                    or "05" in user_data.biography
                    or "04" in user_data.biography
                    or "2024" in user_data.biography
                    or "2023" in user_data.biography
                    or "2022" in user_data.biography
                ):
                    followed = self.insta.user_follow(key)
                    if followed:
                        print(
                            f"[ {colorama.Fore.GREEN}Followed{colorama.Style.RESET_ALL} ] {colorama.Fore.CYAN}{value['username']}{colorama.Style.RESET_ALL} | Reason: BIO"
                        )
                        self.log.info(f"Followed: {value['username']} | Reason: BIO")
                    else:
                        print(
                            f"[ {colorama.Fore.RED}Failed{colorama.Style.RESET_ALL} ]   {colorama.Fore.CYAN}{value['username']}{colorama.Style.RESET_ALL} | Reason: FOLLOW FAIL"
                        )
                        self.log.info(
                            f"Failed:   {value['username']} | Reason: FOLLOW FAIL"
                        )
                    self.sleep_random()
                else:
                    print(
                        f"[ {colorama.Fore.MAGENTA}Skipped{colorama.Style.RESET_ALL} ]  {colorama.Fore.CYAN}{value['username']}{colorama.Style.RESET_ALL} | Reason: No matches"
                    )
                    self.log.info(f"Skipped:  {value['username']}| Reason: No matches")

    def start(self) -> None:
        """
        Start the bot
        """
        print("Starting...")
        self.sleep_random()
        account = "hdsbschools"
        # print("Starting account scrape")
        # self.save_account(account)
        # print("Finished account scrape")

        with open(f"hidden/{account}.json", "r") as file:
            data = json.loads(file.read())
            self.should_i_follow(data)


def main():
    """
    Main func
    """
    client = Insta()
    client.start()


if __name__ == "__main__":
    main()
