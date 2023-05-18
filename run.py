import time
import discord
import requests
import threading
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

bot_token = "MTEwODIwMzAxODY2ODc0ODg4MA.GAZAwc.rSA6oMXfM2tR1F6Mt_lH_VjbL3rLv6j2Dvu6xY"


def send_message(seaifdeez, message):
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel(seaifdeez)
        role_id = 965410891682185226
        role_mention = f"<@&{role_id}>"
        await channel.send(f"{role_mention} {message}")
        await client.close()

    client.run(bot_token)

def minute(minutes):
    return 44 <= minutes <= 51

while True:
    # Specify the URL
    url = "https://www.merfolkslullaby.com/map?&tab=weather"

    # Set up the Selenium webdriver
    options = Options()
    options.add_argument("--headless")  # Run in headless mode, without opening a browser window
    options.add_argument("--log-level=3")  # Disable logging output
    service = Service('path/to/chromedriver')  # Replace 'path/to/chromedriver' with the actual path to the ChromeDriver executable
    driver = webdriver.Chrome(service=service, options=options)


    # Navigate to the webpage
    driver.get(url)

    # Wait for the data to load
    time.sleep(8)  # Adjust the delay as needed

    # Extract the desired data
    content = driver.page_source

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(content, "html.parser")

    # Find elements with the specified CSS class, excluding image elements
    elements = soup.find_all(class_="sc-c76a0318-2 iSTIet", img=False)

    # Extract the text from the elements
    data = [element.get_text() for element in elements if element.get_text().startswith("The Glorious Sea Dog Tavern")] 

    # Join the extracted text with newlines
    # output_data = "\n".join(data)

    output_data = ""
    for item in data:
        if len(item.split()) >= 4:
            try:
                minutes = int(item.split()[5])
                if minute(minutes):
                    output_data += item
                    seaifdeez = 938260679306129408
                    send_message(seaifdeez, output_data)
            except ValueError:
                pass
        else:
            output_data += item + "\n"

    os.system('cls' if os.name == 'nt' else 'clear')

    print(output_data)

    # Close the browser
    driver.quit()

    time.sleep(300)
