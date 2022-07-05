"""
Automatically plays some cards for you
"""

import asyncio
import random

import pyautogui as pag

loop = asyncio.get_event_loop()


async def end_match(match: bool) -> None:
    """
    End the match
    """
    if match:
        match = False
    pag.press("2")
    print("Match ended.")


async def place_card() -> None:
    """
    Attempts to place a card by selecting a card then waiting a random a random
    amount of time then placing.
    """
    pag.press(str(random.randint(1, 4)))
    await asyncio.sleep(random.randint(1, 5) / 10)
    pag.click(random.randint(500, 830), random.randint(363, 570))


async def check_match(match: bool) -> None:
    """
    Check the match's status
    """
    found = pag.locateOnScreen(
        "ClashRoyalePlayer/images/ok.png", region=(610, 650, 110, 60)
    )
    if found:
        await end_match(match)


async def emote():
    """
    Pick a emote randomly lol
    """
    pag.click(1, 1)
    await asyncio.sleep(random.randint(1, 2) / 5)
    pag.click()


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
        await asyncio.sleep(3)
        print("Starting.")
        while True:
            pag.click(748, 508) # party
            await asyncio.sleep(random.randint(1, 3))
            pag.click(761, 551)
            match = True
            while match:
                if random.randint(0, 1):
                    pag.press(str(random.randint(1, 4)))
                await asyncio.sleep(1)
                await place_card()
                await asyncio.sleep(random.randint(1, 6))
                await check_match(match)
            await asyncio.sleep(6) # network, speed, whatever


if __name__ == "__main__":
    asyncio.run(main())
