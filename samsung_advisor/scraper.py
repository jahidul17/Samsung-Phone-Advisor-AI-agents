import requests
from bs4 import BeautifulSoup
import time
import random
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models


models.Base.metadata.create_all(bind=engine)


phone_urls = [
"https://www.gsmarena.com/samsung_galaxy_z_trifold_5g-14292.php",
"https://www.gsmarena.com/samsung_galaxy_m17_5g-14221.php",
"https://www.gsmarena.com/samsung_galaxy_f07-14205.php",
"https://www.gsmarena.com/samsung_galaxy_m07-14100.php",
"https://www.gsmarena.com/samsung_galaxy_a17-14157.php",
"https://www.gsmarena.com/samsung_galaxy_tab_a11+-14192.php",
"https://www.gsmarena.com/samsung_galaxy_tab_a11-14141.php",
"https://www.gsmarena.com/samsung_galaxy_f17_5g-14107.php",
"https://www.gsmarena.com/samsung_galaxy_s25_fe_5g-14042.php",
"https://www.gsmarena.com/samsung_galaxy_tab_s11_ultra_5g-14057.php",
"https://www.gsmarena.com/samsung_galaxy_tab_s11_5g-14058.php",
"https://www.gsmarena.com/samsung_galaxy_tab_s10_lite_5g-14059.php",
"https://www.gsmarena.com/samsung_galaxy_a07-14066.php",
"https://www.gsmarena.com/samsung_galaxy_a17_5g-14041.php",
"https://www.gsmarena.com/samsung_galaxy_f36_5g-14009.php",
"https://www.gsmarena.com/samsung_galaxy_m36_5g-13967.php",
"https://www.gsmarena.com/samsung_galaxy_s25_edge-13506.php",
"https://www.gsmarena.com/samsung_galaxy_f56_5g-13855.php",
"https://www.gsmarena.com/samsung_galaxy_m56_5g-13801.php",
"https://www.gsmarena.com/samsung_galaxy_xcover7_pro-13780.php",
"https://www.gsmarena.com/samsung_galaxy_tab_active5_pro-13790.php",
"https://www.gsmarena.com/samsung_galaxy_tab_s10_fe+-13760.php",
"https://www.gsmarena.com/samsung_galaxy_tab_s10_fe-13761.php",
"https://www.gsmarena.com/samsung_galaxy_f16-13721.php",
"https://www.gsmarena.com/samsung_galaxy_a56-13603.php",
]

def scrape_and_save():
    db = SessionLocal()
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    for index, url in enumerate(phone_urls):
        print(f"[{index+1}/25] Scraping: {url}")
        
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')

                name = soup.find('h1', {'data-spec': 'modelname'}).text.strip()
                display = soup.find('span', {'data-spec': 'displaysize-hl'}).text.strip()
                camera = soup.find('span', {'data-spec': 'camerapixels-hl'}).text.strip() + "MP"
                ram = soup.find('span', {'data-spec': 'ramsize-hl'}).text.strip() + "GB RAM"
                storage = soup.find('span', {'data-spec': 'storage-hl'}).text.strip()
                battery = soup.find('span', {'data-spec': 'batsize-hl'}).text.strip() + "mAh"
                price = soup.find('td', {'data-spec': 'price'}).text.strip()

                new_phone = models.Phone(
                    model_name=name,
                    display=display,
                    camera=camera,
                    ram=ram,
                    storage=storage,
                    battery=battery,
                    price=price
                )

                db.add(new_phone)
                db.commit()
                print(f"Success: {name} saved to PostgreSQL.")

            else:
                print(f"Failed to fetch {url}. Status code: {response.status_code}")

        except Exception as e:
            print(f"Error scraping {url}: {e}")
            db.rollback()


        if index < len(phone_urls) - 1:
            wait_time = random.uniform(5, 15)
            print(f"Sleeping for {wait_time:.2f} seconds...\n")
            time.sleep(wait_time)

    db.close()
    print("All 25 links processed!")

if __name__ == "__main__":
    scrape_and_save()
    
    