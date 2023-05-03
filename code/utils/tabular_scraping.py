# Author: Brenton Graham
# Description: Functions to perform MLB tabular data web scraping from baseball savant
# Last updated: 03/08/23

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import random


def get_savant_tabular_data(player_id, season: int, runners_on_base: bool, output_dir):
    
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
    
    # Make output directory
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"Opening webpage for player ID {player_id}...")
    
    # Driver options 
    options = webdriver.ChromeOptions()
    
    ## --headless prevents browser from showing
    #options.add_argument('--headless')
    
    # Open driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get(url)
    
    # Click "Graphs" button on page for player
    driver.implicitly_wait(20) # Wait for up to 20sec
    driver.find_element(By.ID, f"graph_name_{player_id}_").click()
    
    # Click "Download as CSV" file to download tabular data in output_dir
    print("Downloading tabular file...")
    download_path = os.path.expanduser('~/Downloads') # Where file is going to be stored
    assert f"{player_id}_data.csv" not in os.listdir(download_path), "File to download already exists"
    driver.implicitly_wait(20) # Wait for up to 20sec
    driver.find_element(By.ID, f"csv_name_{player_id}_").click()
    
    # Get play IDs to add to tabular data
    ## Expand page at player ID
    print("Getting play IDs...")
    driver.implicitly_wait(20) # Wait for up to 20sec
    driver.find_element(By.ID, f"id_{player_id}").click()
    
    ## Scrape html for play IDs
    time.sleep(10)
    html_from_page = driver.page_source
    soup = BeautifulSoup(html_from_page, 'html.parser')
    video_specs = [str(link).split('"')[1] for link in soup.findAll("a") if "/sporty-videos?" in str(link)]
    savant_urls = [f"https://baseballsavant.mlb.com{vid_spec}" for vid_spec in video_specs]
    play_ids = [url.split("playId=")[-1] for url in savant_urls]
    
    # Open downloaded CSV to add in play IDs
    tabular_df = pd.read_csv(f"{download_path}/{player_id}_data.csv")
    assert len(tabular_df) == len(play_ids), f"# IDs ({len(play_ids)}) != # plays in CSV file ({len(tabular_df)})"
    tabular_df["play_ids"] = play_ids
    
    # Output updated CSV
    print("Successfully added play IDs. Outputting updated CSV file...")
    tabular_df.to_csv(f"{output_dir}/{player_id}_data.csv", index=False)
    
    # Delete original download file
    os.remove(f"{download_path}/{player_id}_data.csv")
    
    