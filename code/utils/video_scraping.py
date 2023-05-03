# Author: Brenton Graham
# Description: Functions to perform MLB video web scraping from baseball savant
# Last updated: 02/27/23

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


def get_savant_video_urls(player_id, season: int, runners_on_base: bool):
    
    # runners_on_base = True: Pitching from stretch
    from_stretch = ''
    if runners_on_base:
        from_stretch = '4%7C'

    url = f'https://baseballsavant.mlb.com/statcast_search' \
          f'?hfPTM=&hfPT=&hfAB=&hfGT=R%7C&hfPR=&hfZ=&hfStadium=&hfBBL=&hfNewZones=&hfPull=&hfC=&hf' \
          f'Sea={season}%7C&hfSit=&player_type=pitcher&hfOuts=&hfOpponent=&pitcher_throws=&batter_stands=&' \
          f'hfSA=&game_date_gt=&game_date_lt=&hfMo=&hfTeam=&home_road=&hfRO={from_stretch}&position=&hfInfield=&' \
          f'hfOutfield=&hfInn=&hfBBT=&hfFlag=&metric_1=&group_by=name&min_pitches=0&min_results=0&min_pas=0&' \
          f'sort_col=pitches&player_event_sort=api_p_release_speed&sort_order=desc#results'
    
    # Set driver
    print("Opening webpage...")
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    time.sleep(10)
    
    # Expand page at player ID
    print("\nGetting player information...")
    driver.find_element(By.ID, f"id_{player_id}").click()
    time.sleep(10)
    
    # Get all video URLs for the player
    print("Extracting video urls...")
    html_from_page = driver.page_source
    soup = BeautifulSoup(html_from_page, 'html.parser')
    video_specs = [str(link).split('"')[1] for link in soup.findAll("a") if "/sporty-videos?" in str(link)]
    video_urls = [f"https://baseballsavant.mlb.com{vid_spec}" for vid_spec in video_specs]
    
    # Return list of video URLs
    return video_urls


def get_video_link(savant_url):
    r = requests.get(savant_url)
    soup = BeautifulSoup(r.content, 'html5lib')
    link = soup.findAll("source")
    assert len(link) == 1
    video_link = str(link[0]).split("src")[1].split('"')[1]
    return video_link


def download_mp4(video_link, path):
    chunk_size = 256
    r = requests.get(video_link, stream=True)
    output_name = f'{video_link.split(".com/")[1]}'
    with open(f"{path}/{output_name}", "wb") as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            f.write(chunk)

            
def download_mp4_from_savant(savant_url, path):
    video_link = get_video_link(savant_url)
    download_mp4(video_link, path)
    print(f'{video_link} downloaded')
    
    

    