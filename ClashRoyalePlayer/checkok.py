import asyncio

import pyautogui as pag

loop = asyncio.get_event_loop()


async def check_match() -> bool:
    """
    Check if the match is still going
    """
    found = pag.locateOnScreen(
        "ClashRoyalePlayer/images/ok.png", region=(610, 650, 110, 60)
    )

    if found:
        print("FOUND")
    else:
        print("NOT FOUND")


async def main():
    while True:
        await asyncio.sleep(5)
        loop.create_task(check_match())


loop.run_until_complete(main())
