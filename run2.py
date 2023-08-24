import discord
import threading
import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
import time

bot_token = "Your Discord Bot Token" #Replace with actual token



#printing to discord
def send_message(seaifdeez, message):
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        channel = client.get_channel(seaifdeez)
        role_id = 965410891682185226 #replace with desired role to ping"
        role_mention = f"<@&{role_id}>"
        await channel.send(f"{role_mention} Storm at {message}")
        await client.close()

    client.run(bot_token)

#checks if time is between 44 and 51 minutes: enough time to enter game and reach destination
def minute(minutes):
    return 44 <= minutes <= 51

while True:
    url = "https://www.merfolkslullaby.com/map?&tab=weather"
    # Specify paths to Chrome and ChromeDriver
    chrome_path = '/usr/lib/chromium-browser/chromium-browser'  # Path to Chrome binary
    chromedriver_path = '/usr/lib/chromium-browser/chromedriver'  # Path to ChromeDriver binary 
    # Set up Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--log-level=3")
    chrome_options.binary_location = chrome_path
    # Set up the Selenium webdriver with explicit paths
    chrome_service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
    
    #Access website
    driver.get(url)
    
    #Wait for it to load
    time.sleep(15)
    
    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")
    
    #filter by CSS class. Subject to change over time. Change accordingly here.
    elements = soup.find_all(class_="sc-c76a0318-2 cmQris", img=False)
    
    #Print all the extracted data to the terminal
    for element in elements:
        element_text = element.get_text()
        print(element_text)
    print("====================================================")
    
    # Filter and send a specific message to Discord
    for element in elements:
        if "The Glorious Sea Dog Tavern" in element.get_text():
            element_parts = element.get_text().split()
            minutes = int(element_parts[5])
            if minute(minutes):
                output_data = " ".join(element_parts)
                print("Output: ", output_data)
                seaifdeez = 1108687600232955974 #replace with channel id of channel to message
                send_message(seaifdeez, output_data)
    
    #Clears terminal
    #os.system('cls' if os.name == 'nt' else 'clear')
    
    #Run again every 5 minutes
    driver.quit()
    time.sleep(300)
