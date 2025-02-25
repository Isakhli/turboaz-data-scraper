# turboaz-data-scraper
 Turbo.az saytından avtomobil elanlarını avtomatik çəkmək üçün Python + Selenium skripti. Bu layihə Turbo.az üzərindən avtomobil elanlarını çəkərək başlıq, qiymət, şəhər, marka, model, buraxılış ili, mühərrik həcmi və digər məlumatları toplayır. Məlumatlar Excel faylına yazılır.
 
1)Kodu işə salmaq:
Proyekt qovluğunda terminalı açın və aşağıdakı əmri daxil edin: python turboaz_scraper.py

2)Elan sayını daxil etmək:
Proqram sizdən neçə elan çıxarmaq istədiyinizi soruşacaq. Ya rəqəm daxil edin (məsələn, 10), ya da bütün elanları çıxarmaq üçün all yazın.

3)Nəticələrin yazılması:
Proqram avtomobil elanlarını çıxardıqdan sonra məlumatları turboaz_avtomobiller.xlsx adlı Excel faylına yazacaq. Bu fayl proyekt qovluğunda yaradılacaq.

Excel faylında aşağıdakı sütunlar mövcuddur:
Sütun Adı:	Təsvir
Başlıq:	Elanın başlığı
Qiymət:	Avtomobilin qiyməti
Şəhər:	Avtomobilin yerləşdiyi şəhər
Marka:	Avtomobilin markası
Model:	Avtomobilin modeli
Buraxılış ili:	Avtomobilin buraxılış ili
Ban növü:	Avtomobilin ban növü
Rəng:	Avtomobilin rəngi
Mühərrik:	Mühərrikin həcmi və gücü
Yürüş:	Avtomobilin yürüşü (km)
Sürətlər qutusu:	Sürətlər qutusunun növü
Ötürücü:	Ötürücü növü
Yeni	Avtomobilin yeni olub-olmaması
Sahiblər:	Sahiblərin sayı
Vəziyyəti:	Avtomobilin vəziyyəti
Açıqlama:	Elan haqqında əlavə məlumat
Link:	Elanın linki



Proqram işləyərkən Chrome brauzeri avtomatik açılacaq və bağlanmayacaq. Bu, Selenium-un detach seçimi ilə idarə olunur.

Əgər elanların sayı çoxdursa, proqramın işləməsi bir qədər vaxt ala bilər.

Xətaların qarşısını almaq üçün proqramda müəyyən sərhədlər tətbiq edilmişdir (məsələn, eyni elanın təkrar çıxarılmasının qarşısı alınır).

1. Kitabxanaların İdxalı
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import pandas as pd
Selenium: Brauzer avtomatlaşdırma üçün istifadə olunur.
Pandas: Məlumatları Excel faylına yazmaq üçün istifadə olunur.
Time: Kodun müəyyən hissələrində gözləmə üçün istifadə olunur.

2. İstifadəçi Girişi
elan_sayi_input = input("Neçə avtomobil elanı çəkmək istəyirsiniz? (Rəqəm və ya 'all'): ").strip().lower()
elan_sayi = None if elan_sayi_input == 'all' else int(elan_sayi_input)
İstifadəçidən neçə elan çıxarmaq istədiyini soruşur.
Əgər istifadəçi all yazsa, bütün elanlar çıxarılır. Əks halda, daxil edilən rəqəm qədər elan çıxarılır.

3. ChromeDriver-in Konfiqurasiyası
chrome_driver_yolu = "C:\\Users\\ASUS\\Desktop\\turbo.az\\chromedriver.exe"
def brauzeri_baslat():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)  # Brauzer bağlanmasın
    service = Service(chrome_driver_yolu)
    return webdriver.Chrome(service=service, options=options)
   
ChromeDriver yolu təyin edilir.
brauzeri_baslat() funksiyası Chrome brauzerini başladır və brauzerin avtomatik bağlanmasının qarşısını alır.

4. Brauzerin Başladılması və Sayta Giriş
driver = brauzeri_baslat()
driver.get("https://turbo.az/")
time.sleep(3)

Brauzer başladılır və Turbo.az saytına daxil olunur.
Saytın tam yüklənməsi üçün 3 saniyə gözlənilir.

5. Elanların Çıxarılması
avtomobil_melumatlari = []  # Məlumatların saxlanacağı siyahı

def elanlari_cek():
    while elan_sayi is None or len(avtomobil_melumatlari) < elan_sayi:
        driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        time.sleep(2)
        
avtomobil_melumatlari siyahısı, çıxarılan məlumatların saxlanacağı yerdir.
elanlari_cek() funksiyası, səhifəni aşağıya sürüşdürərək yeni elanların yüklənməsini təmin edir.

6. Elan Detallarının Alınması
elanlar = driver.find_elements(By.CLASS_NAME, 'products-i')
for elan in elanlar:
    if elan_sayi and len(avtomobil_melumatlari) >= elan_sayi:
        break
products-i sinfi ilə elanlar tapılır.

Əgər istifadəçi tərəfindən təyin edilən elan sayına çatılıbsa, döngü dayandırılır.

7. Elan Məlumatlarının Çıxarılması
basliq = elan.find_element(By.CLASS_NAME, 'products-i__name').text.strip()
qiymet = elan.find_element(By.CLASS_NAME, 'product-price').text.strip()
link = elan.find_element(By.TAG_NAME, 'a').get_attribute('href')
Hər bir elanın başlıq, qiymət və link məlumatları çıxarılır.
