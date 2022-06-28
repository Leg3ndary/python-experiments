"""
Automatically plays some cards for you
"""

import asyncio
import pyautogui as pag
import random


loop = asyncio.get_event_loop()


async def end_match(match) -> None:
    """
    End the match
    """
    match = False
    pag.press("2")
    await asyncio.sleep("5")


async def place_card() -> None:
    """
    Attempts to place a card
    """
    pag.press(str(random.randint(1, 4)))
    await asyncio.sleep(0.3)
    pag.click(random.randint(500, 830), random.randint(363, 570))


async def check_match(match) -> None:
    found = pag.locateOnScreen(
        "ClashRoyalePlayer/images/ok.png", region=(610, 650, 110, 60)
    )

    if found:
        await end_match(match)


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
        while True:
            pag.click(748, 508)
            await asyncio.sleep(random.randint(1, 3))
            pag.click(761, 551)
            match = True
            while match:
                await asyncio.sleep(random.randint(1, 14))
                loop.create_task(check_match(match))
                await asyncio.sleep(1)
                await match.player.play_card()


if __name__ == "__main__":
    asyncio.run(main())
