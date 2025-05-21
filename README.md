# Gloop

Gloop es una aplicación de escritorio multiplataforma que te permite cambiar fácilmente entre múltiples identidades globales de Git (nombre y correo) desde la bandeja del sistema (system tray). Diseñado para desarrolladores que manejan cuentas personales, laborales y de proyectos open source de forma separada.

---

## ✨ Características

- Detecta el usuario global actual de Git (`user.name` y `user.email`)
- Cambia entre diferentes perfiles desde un menú en el system tray
- Icono dinámico basado en el avatar de GitHub del usuario activo
- Almacena perfiles de forma local en `~/.git_profiles.json`
- Interfaz simple y sin telemetría

---

## 🚀 Instalación

### Requisitos

- Python 3.10 o superior
- `git` instalado
- Conexión a internet (opcional, para descargar avatares)

### Dependencias

```bash
pip install -r requirements.txt
```

---

## ▶️ Ejecución

```bash
python src/main.py
```

---

## 🧱 Estructura del Proyecto

```
gloop/
├── assets/                 # Íconos y gráficos del proyecto
├── src/                    # Código fuente principal
├── .github/                # Workflows de GitHub y funding
├── docs/                   # Documentos adicionales
├── requirements.txt
├── pyproject.toml
├── README.md
├── LICENSE
├── CONTRIBUTING.md
├── .gitignore
```

---

## 🖼️ Íconos disponibles

* PNG: 16x16, 32x32, 64x64, 128x128, 256x256
* Windows: `gittrayapp_icon.ico`
* macOS: `gittrayapp_icon.icns`

Coloca estos íconos en la carpeta `assets/`.

---

## 🖥️ Compilación con PyInstaller

### Windows

```bash
pyinstaller --noconfirm --onefile --windowed src/main.py --icon=assets/gittrayapp_icon.ico --name gloop
```

### macOS

```bash
pyinstaller --noconfirm --onefile --windowed src/main.py --icon=assets/gittrayapp_icon.icns --name gloop
```

---

## 🐧 Integración con Linux (.desktop)

Crea un archivo `~/.local/share/applications/gloop.desktop` con el siguiente contenido:

```desktop
[Desktop Entry]
Type=Application
Name=Gloop
Comment=Switch between global Git identities easily
Exec=python3 /ruta/a/gloop/src/main.py
Icon=/ruta/a/gloop/assets/gittrayapp_icon_128x128.png
Terminal=false
Categories=Development;Utility;
StartupNotify=true
```

Hazlo ejecutable:

```bash
chmod +x ~/.local/share/applications/gloop.desktop
```

---

## ✅ Checklist de funcionalidades futuras

* [ ] Mostrar tooltip o copia rápida de `git clone` con el usuario activo
* [ ] Detectar proveedor Git (GitHub, GitLab) y sugerir comandos
* [ ] Configuración local por carpeta (modo repo-specific)
* [ ] Integración con llaves SSH y `.ssh/config`
* [ ] Historial de cambios y actividad de usuarios
* [ ] Interfaz completa para gestión de perfiles
* [ ] Traducción multilenguaje

---

## 🌍 Difusión y colaboración

Consulta `docs/guia-estrategica.md` para conocer cómo puedes apoyar la difusión del proyecto, contribuir o generar forks para adaptaciones futuras.

---

## ❤️ Contribuciones

Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para conocer cómo puedes colaborar con mejoras, reportes o traducciones.

---

## 💸 Apoya este proyecto

Este proyecto es libre y sin rastreadores. Si te resulta útil, puedes apoyarlo:

* [GitHub Sponsors](https://github.com/sponsors/cripterhack)
* [Ko-fi](https://ko-fi.com/cripterhack)
* [Patreon](https://patreon.com/cripterhack)

(Ver `.github/FUNDING.yml`)

---

## 🧠 Licencia

MIT — Puedes usar, modificar y compartir este proyecto con libertad.
