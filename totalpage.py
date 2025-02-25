from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# Kullanıcıdan ilan sayısını al
num_cars_input = input("Neçə avtomobil elanı çəkmək istəyirsiniz? (Rəqəm və ya 'all'): ").strip().lower()
num_cars = None if num_cars_input == 'all' else int(num_cars_input)

# ChromeDriver yolu
chrome_driver_path = "C:\\Users\\ASUS\\Desktop\\turbo.az\\chromedriver.exe"

def tarayiciyi_baslat():
    """Chrome tarayıcısını başlatır."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Tarayıcı kapanmasın
    service = Service(chrome_driver_path)
    return webdriver.Chrome(service=service, options=options)

driver = tarayiciyi_baslat()
driver.get("https://turbo.az/")
time.sleep(3)

car_data = []  # Liste olarak tanımlandı ✅

def ilanlari_cek():
    """İlanları çeker ve detaylarını alır."""
    while num_cars is None or len(car_data) < num_cars:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)

        cars = driver.find_elements(By.CLASS_NAME, 'products-i')
        for car in cars:
            if num_cars and len(car_data) >= num_cars:
                break
            
            try:
                title = car.find_element(By.CLASS_NAME, 'products-i__name').text.strip()
                price = car.find_element(By.CLASS_NAME, 'product-price').text.strip()
                link = car.find_element(By.TAG_NAME, 'a').get_attribute('href')
                
                # Link daha önce çekilmişse atla
                if any(link in item for item in car_data):
                    continue
                
                # Yeni sekmede ilanı aç
                driver.execute_script(f"window.open('{link}', '_blank');")
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(2)
                
                # Bilgileri çek (Eksik olursa hata yakalanır) ✅
                def get_text(xpath):
                    try:
                        return driver.find_element(By.XPATH, xpath).text.strip()
                    except:
                        return "Bilinməyən"

                city = get_text("//label[@for='ad_region']/following-sibling::span")
                brand = get_text("//label[@for='ad_make_id']/following-sibling::span/a")
                model = get_text("//label[@for='ad_model']/following-sibling::span/a")
                year = get_text("//label[@for='ad_reg_year']/following-sibling::span/a")
                body_type = get_text("//label[@for='ad_category']/following-sibling::span")
                color = get_text("//label[@for='ad_color']/following-sibling::span")
                engine = get_text("//label[@for='ad_engine_volume']/following-sibling::span")
                mileage = get_text("//label[@for='ad_mileage']/following-sibling::span")
                transmission = get_text("//label[@for='ad_transmission']/following-sibling::span")
                drive_type = get_text("//label[@for='ad_gear']/following-sibling::span")
                new_status = get_text("//label[@for='ad_new']/following-sibling::span")
                owners = get_text("//label[@for='ad_prior_owners_count']/following-sibling::span")
                condition = get_text("//label[@for='ad_Vəziyyəti']/following-sibling::span")
                description = get_text("//div[contains(@class, 'product-description__content')]")

                # Verileri listeye ekle ✅
                car_data.append([
                    title, price, city, brand, model, year, body_type, color, engine, 
                    mileage, transmission, drive_type, new_status, owners, condition, 
                    description, link
                ])

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:
                print(f"Hata: {e}")
                continue

# İlanları çek
ilanlari_cek()

# Verileri DataFrame'e ekle ve Excel'e kaydet ✅
df = pd.DataFrame(car_data, columns=["Başlık", "Fiyat", "Şəhər", "Marka", "Model", "Buraxılış ili", "Ban növü", "Rəng", "Mühərrik", "Yürüş", "Sürətlər qutusu", "Ötürücü", "Yeni", "Sahiblər", "Vəziyyəti", "Açıklama", "Link"])
df.to_excel("turboaz_cars.xlsx", index=False)

print(f"✅ {len(car_data)} ilan kaydedildi! Veriler 'turboaz_cars.xlsx' dosyasına yazıldı.")
driver.quit()
