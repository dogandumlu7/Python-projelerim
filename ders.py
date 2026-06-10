import cv2
from ultralytics import YOLO

# YOLOv8 modelini yükle (COCO veri kümesiyle eğitilmiş önceden eğitilmiş model)
model = YOLO("yolo.pt")  # Nano model, hızlı çalışması için ideal

# Video kaynağı (0 = Web Kamera, dosya yolu = Video dosyası)
video_kaynagi =  0  # Webcam için 0, video dosyası için "video.mp4" gibi bir yol kullanabilirsiniz
kamera = cv2.VideoCapture(video_kaynagi)

# Görüntü boyutlarını ayarla (genişlik ve yükseklik)
genislik, yukseklik = 1920 , 1080
kamera.set(cv2.CAP_PROP_FRAME_WIDTH, genislik)
kamera.set(cv2.CAP_PROP_FRAME_HEIGHT, yukseklik)

# Video kaydetmek için (isteğe bağlı)
"""dortcc = cv2.VideoWriter_fourcc(*"XVID")
cikti_video = cv2.VideoWriter("cikti_video.avi", dortcc, 20.0, (genislik, yukseklik))"""

while kamera.isOpened():
    okundu, kare = kamera.read()
    if not okundu:
        break

    # YOLO modeliyle tespit yap
    sonuc = model(kare, conf=0.1)  # Güven eşiği: 0.5
    tespitler = sonuc[0].boxes.data  # Tespit edilen nesnelerin verisi

    # Tespit edilen nesneler üzerinde işlem yap
    for tespit in tespitler:
        x1, y1, x2, y2, guven, sinif_id = tespit.tolist()
        sinif_id = int(sinif_id)
        sinif_adi = model.names[sinif_id]

        # Tespit edilen nesne için dikdörtgen çiz
        cv2.rectangle(kare, (int(x1), int(y1)), (int(x2), int(y2)), (255, 0, 0), 6)
        cv2.putText(kare, f"{sinif_adi} {guven:.2f}", (int(x1), int(y1) - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # İşlenmiş görüntüyü göster
    cv2.imshow("yuz tanıma", kare)

    # İşlenmiş kareyi videoya kaydet
"""    cikti_video.write(kare)"""

    # # Çıkış için 'q' tuşuna basın
    # if cv2.waitKey(1) & 0xFF == ord("q"):
    #     break

# Kaynakları serbest bırak
kamera.release()
"""cikti_video.release()"""
cv2.destroyAllWindows()
