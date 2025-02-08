import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data():
    print("Veri giriş yöntemi seçin: \n1. CSV Yükle \n2. Manuel Giriş")
    choice = input("Seçiminiz (1/2): ")
    if choice == "1":
        file_path = input("CSV dosyasının yolunu girin: ")
        try:
            data = pd.read_excel(file_path)
            print("Veri başarıyla yüklendi! İşte ilk 5 satır:")
            print(data.head())
            return data
        except Exception as e:
            print(f"Hata oluştu: {e}")
            return None
    elif choice == "2":
        print("Manuel veri girişi şu an için desteklenmiyor.")
        return None
    else:
        print("Geçersiz seçim!")
        return None

def suggest_analysis(data):
    print("Seçenekler: \n1. Tanımlayıcı İstatistikler \n2. Korelasyon Analizi \n3. Veri Dağılımı \n4. Histogram \n5. Kutu Grafiği")
    analysis_choice = input("Yapmak istediğiniz analiz türünü seçin (1-5): ")
    return analysis_choice

def perform_analysis(data, choice):
    if choice == "1":
        print("Tanımlayıcı İstatistikler:")
        print(data.describe())
    elif choice == "2":
        print("Korelasyon Matrisi:")
        print(data.corr())
        sns.heatmap(data.corr(), annot=True, cmap="coolwarm")
        plt.show()
    elif choice == "3":
        data.plot(kind='density', subplots=True, layout=(3, 3), sharex=False)
        plt.show()
    elif choice == "4":
        data.hist(figsize=(10, 6))
        plt.show()
    elif choice == "5":
        data.plot(kind='box', subplots=True, layout=(3, 3), sharex=False, sharey=False)
        plt.show()
    else:
        print("Geçersiz seçim!")

if __name__ == "__main__":
    df = load_data()
    if df is not None:
        analysis_type = suggest_analysis(df)
        perform_analysis(df, analysis_type)
