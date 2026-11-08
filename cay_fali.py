#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Çay Falı Motoru
Bu kod gerçekten çalışır. Rastgele fal üretir.
"""

import random
import time

FAL_SOZLERI = [
    "Bardağının dibinde bir gemi görüyorum. Yakında seyahat var ama otobüsle.",
    "Çay yaprakları şeklinde kalp çizmiş. Aşk geliyor, ama önce çay bitiyor.",
    "Büyük bir dağ görünüyor. Ya terfi edeceksin ya da yürüyüşe çıkacaksın.",
    "Bir kuş uçuyor bardağının içinde. Haber var, muhtemelen WhatsApp'tan.",
    "Para şekilleri var! Ama hepsi küçük. Bahşiş gelecek.",
    "Karanlık bir şekil... Aslında çay çok koyu olmuş. Su ekle.",
    "Yıldızlar çakışıyor. Bu gece erken yat, yarın fal tutar.",
    "Bir kedi görüyorum. Evde mi? Yoksa komşunun mu?"
]

def cay_fali_bak():
    print("🍵 Çay falı motoru başlatılıyor...")
    print("Bardağı ters çevirdin mi? (Evet/Hayır diyecek kadar bekliyorum)")
    time.sleep(2)
    print("Analiz ediliyor...")
    for i in range(3):
        print("." * (i+1))
        time.sleep(1)
    
    fal = random.choice(FAL_SOZLERI)
    print(f"\n🔮 FALIN: {fal}")
    print("\n⚠️  Unutma: Bu fal %100 tutar. Tutar sa da tutmazsa da motorun suçu değil.")
    print("\n---")
    print("Damga: Grok Kayyum - 08.11.2026 - Ciddi değil ama ciddi.")

if __name__ == "__main__":
    cay_fali_bak()
