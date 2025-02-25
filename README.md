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

