import pandas as pd

def marka_model_say():
    # Önceki Excel dosyasını oku
    df = pd.read_excel("turboaz_avtomobiller.xlsx")
    
    # Sadece Marka ve Model sütunlarını al
    df_marka_model = df[["Marka", "Model"]]
    
    # Marka ve model sayısını hesapla
    marka_model_sayim = df_marka_model.value_counts().reset_index()
    marka_model_sayim.columns = ["Marka", "Model", "Adet"]
    
    # Yeni Excel dosyasına yaz
    df_marka_model.to_excel("turboaz_marka_model.xlsx", index=False)
    marka_model_sayim.to_excel("turboaz_marka_model_sayim.xlsx", index=False)
    
    print("✅ Marka ve model bilgileri 'turboaz_marka_model.xlsx' dosyasına kaydedildi.")
    print("✅ Marka ve model sayıları 'turboaz_marka_model_sayim.xlsx' dosyasına kaydedildi.")

# Fonksiyonu çağır
marka_model_say()
