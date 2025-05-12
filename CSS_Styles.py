"""
### ⚠️ Disclaimer / Sorumluluk Reddi

**English:**  
This application is developed for educational purpose only. It does **not** provide financial or investment advice. All investment decisions made based on this application are at the sole discretion and risk of the user. The developer assumes **no responsibility** for any financial loss or damage resulting from the use of this tool.

**Türkçe:**  
Bu uygulama yalnızca eğitim amaçlı geliştirilmiştir. **Yatırım tavsiyesi niteliği taşımaz.** Uygulama aracılığıyla yapılan tüm yatırım kararları tamamen kullanıcının kendi inisiyatifinde ve sorumluluğundadır. Uygulamanın geliştiricisi, kullanım sonucu oluşabilecek hiçbir maddi zarardan **sorumlu değildir.**
"""

class CSS_Styles:
    def get_styles(self):
        return """
        .button-style {
            background-color: blue;
            color: white;
            border: none;
            padding: 10px;
            cursor: pointer;
            border-radius: 5px;
        }
        .output-style {
            background-color: lightcoral;
            color: white;
            border: none;
            padding: 10px;
            border-radius: 5px;
        }
        .custom-row {
            display: flex;
            justify-content: space-between; /* Bileşenler arasında boşluk bırakır */
            align-items: center; /* Bileşenleri ortalar */
            gap: 10px; /* Bileşenler arasındaki boşluk */
            height: 100px; /* Row yüksekliği */
        }
        .menu-row {
            height: 60px;
        }
        .small-button {
            min-width: 200px; /* Minimum genişlik */
            max-width: 300px; /* Maksimum genişlik */
            width: auto; /* Genişlik içeriğe bağlı */
            display: block; /* Butonu bir blok öğe yap */
            margin: 0 auto; /* Yatayda ortalama */
            text-align: center; /* Metni yatayda ortalama */
        }
        .small-button-red {
            min-width: 200px; /* Minimum genişlik */
            max-width: 300px; /* Maksimum genişlik */
            width: auto; /* Genişlik içeriğe bağlı */
            background-color: #7DF9FF;
            color:black;
        }
        .small-button-yellow {
            min-width: 200px; /* Minimum genişlik */
            max-width: 300px; /* Maksimum genişlik */
            width: auto; /* Genişlik içeriğe bağlı */
            background-color: #eef52a;
            color:black;
        }
        .small-button-green {
            min-width: 200px; /* Minimum genişlik */
            max-width: 300px; /* Maksimum genişlik */
            width: auto; /* Genişlik içeriğe bağlı */
            background-color: #AFE1AF;
            color:black;
        }
        #file_input {
            min-width: 150px; /* Minimum genişlik */
            max-width: 250px; /* Maksimum genişlik */
            max-height: 100px;
        }
        """