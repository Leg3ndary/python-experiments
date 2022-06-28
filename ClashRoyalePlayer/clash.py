"""
Automatically plays some cards for you
"""

import asyncio
import pyautogui as pag
import random


loop = asyncio.get_event_loop()


class Player:
    """
    Player class to play games
    """

    def __init__(self) -> None:
        """
        Construct the player class
        """
        pass

    async def place_card(self) -> None:
        """
        Attempts to place a card
        """
        pag.press(str(random.randint(1, 4)))
        pag.click(random.randint(500, 830), random.randint(363, 570))


class Match:
    """
    Represents a Match and its related info
    """

    def __init__(self, player: Player) -> None:
        """
        Constructing the match
        """
        print("Created a Match")
        self.match = True
        self.player = player
    
    async def run_match(self) -> None:
        """
        Run a match
        """
        while self.match:
            await asyncio.sleep(random.randint(1, 14))
            loop.create_task(self.check_match())
            await asyncio.sleep(1)
            await self.player.play_card()

    async def check_match(self) -> bool:
        """
        Check if the match is still going
        """
        found = pag.locateOnScreen("ClashRoyalePlayer/images/ok.png", region=(610, 650, 110, 60))
        
        if found:
            self.end_match()

    def end_match(self) -> None:
        """
        End the match
        """
        self.match = False
        pag.press("2")


async def main():
    """
    Main func

    Borders are
    0 BLACK 460 GAME 873 BLACK 1333

    Cards are equally spaced between 460 and 873

    18 TILES

    Tile 1: Bottom Left 500, 570:
    Tile 18: 830, 570:

    TOP 363, BOTTOM 570.
    
    Range for x is 500 to 830
    Range for y is 363 to 570
    """
    size = pag.size()

    if not size.width == 1366 and not size.height == 768:
        raise Exception("Please run this program on a 1366x768 screen")
    else:
        print("Starting.")
        player = Player()
        while True:
            pag.click(748, 508)
            await asyncio.sleep(random.randint(1, 3))
            pag.click(761, 551)
            match = Match(player)
            loop.run_until_complete(match.run_match())


if __name__ == "__main__":
    asyncio.run(main())