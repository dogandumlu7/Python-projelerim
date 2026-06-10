from fpdf import FPDF

# Initialize PDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()
pdf.set_font("Arial", size=12)

# Title
pdf.set_font("Arial", style="B", size=16)
pdf.cell(200, 10, txt="Zorlu Matematik ve Algoritma Soruları", ln=True, align='C')
pdf.ln(10)

# Add Questions
pdf.set_font("Arial", size=12)

questions = [
    "1) Bir çemberin denklemi x^2 + y^2 = r^2 olarak verilmektedir. "
    "Bu çember üzerindeki P(x1, y1) noktasına ait teğetin denklemini bulunuz. "
    "Ayrıca, verilen (x1, y1) noktası çemberin üzerinde değilse, çemberle kesişimini analiz edin.",

    "2) Bir dizinin en büyük ortak bölenlerini bulan bir algoritma yazın. "
    "Dizinin tüm elemanlarının ortak bölenlerini bulup bu değeri döndürmesi beklenmektedir. "
    "Hem algoritmayı açıklayın hem de Python kodunu yazın.",

    "3) Eğer bir string'in düzden ve tersten yazılışları aynı ise ona palindrome denir. "
    "Bir string içindeki tüm palindrome alt dizeleri bulan bir Python fonksiyonu yazın. (İpucu: Alt dizeler için çift döngü kullanabilirsiniz.)",

    "4) Limit hesaplama: \n"
    "   a) lim (x -> 0) (sin(2x) / tan(3x))\n"
    "   b) lim (x -> 1) ((x^x - x) / (ln(x))).\n"
    "Bu limitleri adım adım çözünüz.",

    "5) Bir çember sınıfı oluşturun. Çember sınıfı, merkezi (x, y) koordinatları ile yarıçapı içerir. "
    "Bu sınıfa, iki çemberin kesişip kesişmediğini belirleyen bir metot ekleyin. Kesim durumunda, kesişim noktalarını döndürün.",

    "6) Aşağıdaki Python kodunun çıktısını tahmin ediniz:\n"
    "   n = 4\n"
    "   for i in range(n):\n"
    "       for j in range(i, n):\n"
    "           print(i * j, end=' ')\n"
    "       print('')",

    "7) Bir asal sayı kontrol algoritması yazın. Ancak bu algoritma, kontrol ettiği sayıların 2'lik veya 3'lük tabandaki "
    "görünümlerine göre özelleştirilebilir olmalıdır. Örneğin, bir sayının sadece 2'lik tabanda belirli özelliklere sahip "
    "olması durumunda asal olduğunu belirleyebilmelidir.",

    "8) Bir doğru (ax + by + c = 0) ve bir çember (x^2 + y^2 + dx + ey + f = 0) arasında ilişkiyi analiz eden bir program yazın. "
    "Doğru ve çemberin kesişip kesişmediğini bulun ve kesişim noktalarını döndürün."
]

# Add questions to the PDF
for i, question in enumerate(questions, 1):
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, f"Soru {i}:", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, question)
    pdf.ln(5)

# Save the PDF
output_path = "/mnt/data/Advanced_Math_Questions.pdf"
pdf.output(output_path)
output_path
