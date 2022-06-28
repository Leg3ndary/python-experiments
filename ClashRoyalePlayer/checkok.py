import asyncio
import pyautogui as pag

loop = asyncio.get_event_loop()

async def check_match() -> None:
    """
    Check if the match is still going
    """
    found = await loop.run_in_executor(None, pag.locate, "images/ok.png")
    
    if found:
        print("FOUND")
    else:
        print("NOT FOUND")


async def main():
    while True:
        await asyncio.sleep(5)
        await check_match()

loop.run_until_complete(main())