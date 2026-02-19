import psutil
import time
import firebase_admin
from firebase_admin import credentials, db

# Firebase yapılandırması
cred = credentials.Certificate("firebase-service-account.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'YOUR_DATABASE_URL'
})

# Firebase referansı
ref = db.reference('system_metrics')

# Sistem metriklerini al ve Firebase'e gönder
while True:
    cpu_percent = psutil.cpu_percent(interval=1)
    ram_percent = psutil.virtual_memory().percent
    
    data = {
        'timestamp': int(time.time()),
        'cpu': cpu_percent,
        'ram': ram_percent
    }
    
    ref.push(data)
    print(f"Veriler Firebase'e gönderildi: CPU={cpu_percent}%, RAM={ram_percent}%")
    time.sleep(1)