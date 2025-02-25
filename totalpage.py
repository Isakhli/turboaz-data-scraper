from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd

# İstifadəçidən elan sayını al
elan_sayi_input = input("Neçə avtomobil elanı çəkmək istəyirsiniz? (Rəqəm və ya 'all'): ").strip().lower()
elan_sayi = None if elan_sayi_input == 'all' else int(elan_sayi_input)

# ChromeDriver yolu
chrome_driver_yolu = "C:\\Users\\ASUS\\Desktop\\turbo.az\\chromedriver.exe"

def brauzeri_baslat():
    """Chrome brauzerini başladır."""
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Brauzer bağlanmasın
    service = Service(chrome_driver_yolu)
    return webdriver.Chrome(service=service, options=options)

driver = brauzeri_baslat()
driver.get("https://turbo.az/")
time.sleep(3)

avtomobil_melumatlari = []  # Siyahı kimi təyin edildi 

def elanlari_cek():
    """Elanları çəkir və detalları alır."""
    while elan_sayi is None or len(avtomobil_melumatlari) < elan_sayi:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)

        elanlar = driver.find_elements(By.CLASS_NAME, 'products-i')
        for elan in elanlar:
            if elan_sayi and len(avtomobil_melumatlari) >= elan_sayi:
                break
            
            try:
                basliq = elan.find_element(By.CLASS_NAME, 'products-i__name').text.strip()
                qiymet = elan.find_element(By.CLASS_NAME, 'product-price').text.strip()
                link = elan.find_element(By.TAG_NAME, 'a').get_attribute('href')
                
                # Əgər link artıq çəkilibsə, keç
                if any(link in item for item in avtomobil_melumatlari):
                    continue
                
                # Yeni pəncərədə elanı aç
                driver.execute_script(f"window.open('{link}', '_blank');")
                driver.switch_to.window(driver.window_handles[1])
                time.sleep(2)
                
                # Məlumatları çək (Əgər yoxdursa, xəta tutulur) 
                def melumat_al(xpath):
                    try:
                        return driver.find_element(By.XPATH, xpath).text.strip()
                    except:
                        return "Bilinməyən"

                seher = melumat_al("//label[@for='ad_region']/following-sibling::span")
                marka = melumat_al("//label[@for='ad_make_id']/following-sibling::span/a")
                model = melumat_al("//label[@for='ad_model']/following-sibling::span/a")
                buraxilis_ili = melumat_al("//label[@for='ad_reg_year']/following-sibling::span/a")
                ban_novu = melumat_al("//label[@for='ad_category']/following-sibling::span")
                reng = melumat_al("//label[@for='ad_color']/following-sibling::span")
                muherik = melumat_al("//label[@for='ad_engine_volume']/following-sibling::span")
                yurush = melumat_al("//label[@for='ad_mileage']/following-sibling::span")
                suretler_qutusu = melumat_al("//label[@for='ad_transmission']/following-sibling::span")
                oturucu = melumat_al("//label[@for='ad_gear']/following-sibling::span")
                yeni = melumat_al("//label[@for='ad_new']/following-sibling::span")
                sahibler = melumat_al("//label[@for='ad_prior_owners_count']/following-sibling::span")
                veziyyet = melumat_al("//label[@for='ad_Vəziyyəti']/following-sibling::span")
                aciqlama = melumat_al("//div[contains(@class, 'product-description__content')]")

                # Məlumatları siyahıya əlavə et 
                avtomobil_melumatlari.append([
                    basliq, qiymet, seher, marka, model, buraxilis_ili, ban_novu, reng, muherik, 
                    yurush, suretler_qutusu, oturucu, yeni, sahibler, veziyyet, 
                    aciqlama, link
                ])

                driver.close()
                driver.switch_to.window(driver.window_handles[0])

            except Exception as e:
                print(f"Xəta: {e}")
                continue

# Elanları çək
elanlari_cek()

# Məlumatları DataFrame-ə əlavə et və Excel-ə yaz 
df = pd.DataFrame(avtomobil_melumatlari, columns=["Başlıq", "Qiymət", "Şəhər", "Marka", "Model", "Buraxılış ili", "Ban növü", "Rəng", "Mühərrik", "Yürüş", "Sürətlər qutusu", "Ötürücü", "Yeni", "Sahiblər", "Vəziyyəti", "Açıqlama", "Link"])
df.to_excel("turboaz_avtomobiller.xlsx", index=False)

print(f"✅ {len(avtomobil_melumatlari)} elan qeydə alındı! Məlumatlar 'turboaz_avtomobiller.xlsx' faylına yazıldı.")
driver.quit()
