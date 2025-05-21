# 📦 Desarrollo por MVPs (Producto Mínimo Viable)

Para asegurar un desarrollo ordenado, funcional y documentado, Gloop se construirá en etapas MVP (Producto Mínimo Viable). Cada MVP es una versión utilizable, estable y documentada, que agrega valor incrementalmente. **Cada etapa debe actualizar la documentación y pasar controles de calidad antes de avanzar.**

---

## 🏗️ Etapas sugeridas de MVP para Gloop

### MVP 0: Bootstrap del Proyecto
- **Objetivo:** Fundamentos para desarrollo y colaboración.
- **Incluye:**
  - Estructura de proyecto, control de versiones y README inicial.
  - Documentación básica: instalación, contribución, código de conducta.
  - Linting, formateo y CI.
- **Checklist:**
  - [ ] Estructura y CI funcionando
  - [ ] Documentación inicial

### MVP 1: Funcionalidad Central
- **Objetivo:** Entregar la propuesta de valor esencial.
- **Incluye:**
  - Detección y visualización del usuario global de Git.
  - Cambio entre perfiles almacenados.
  - Almacenamiento local de perfiles.
  - UI mínima en la bandeja del sistema.
- **Checklist:**
  - [ ] Cambio de usuario funcional
  - [ ] Persistencia de perfiles
  - [ ] UI básica
  - [ ] Documentación y capturas

### MVP 2: Experiencia de Usuario y Soporte Multiplataforma
- **Objetivo:** Mejorar UX y compatibilidad.
- **Incluye:**
  - Icono dinámico (avatar).
  - Soporte Windows/macOS/Linux.
  - Manejo de errores y feedback al usuario.
- **Checklist:**
  - [ ] Icono/avatar multiplataforma
  - [ ] Mensajes de error claros
  - [ ] Documentación por plataforma

### MVP 3: Funciones Avanzadas e Integraciones
- **Objetivo:** Agregar características para usuarios avanzados.
- **Incluye:**
  - Copia rápida de `git clone` con usuario activo.
  - Detección de proveedor Git (GitHub, GitLab).
  - Configuración por repo.
  - Integración con llaves SSH.
- **Checklist:**
  - [ ] Funciones avanzadas probadas
  - [ ] Guías de integración

### MVP 4: Comunidad y Extensibilidad
- **Objetivo:** Fomentar contribuciones y extensibilidad.
- **Incluye:**
  - Sistema de plugins/hooks (si aplica).
  - Soporte multilenguaje.
  - Roadmap y issues abiertos para la comunidad.
- **Checklist:**
  - [ ] Puntos de extensión documentados
  - [ ] Guía de traducción y contribución

---

## 📚 Protocolo de actualización de documentación (por cada MVP)
- Actualizar README con nuevas funciones y capturas.
- Ampliar `docs/` con guías técnicas y de usuario.
- Mantener changelog claro (CHANGELOG.md).
- Agregar/actualizar ADRs para decisiones clave.
- Cruzar referencias en los archivos relevantes.
- Marcar funciones obsoletas con notas de migración.

---

## 🛡️ Puertas de calidad y consistencia
- Todas las funciones deben tener tests (unitarios/integración).
- Linting y CI deben pasar antes de mergear.
- Checklist de regresión manual por MVP.
- Revisión de PRs (o simulación LLM).
- Revisión de textos de UI por claridad y consistencia.

---

## 🔄 Seguimiento y feedback
- Tras cada MVP, recopilar feedback y actualizar el roadmap.
- Usar la tabla de progreso para visualizar avances y pendientes.

| MVP | Features | Docs | Tests | Feedback |
|-----|----------|------|-------|----------|
| 0   | ☐        | ☐    | ☐     | N/A      |
| 1   | ☐        | ☐    | ☐     | ☐        |
| ... | ...      | ...  | ...   | ...      |

---

> **Referencia:** Las fases de lanzamiento, difusión y comunidad descritas abajo pueden solaparse con los MVPs, pero cada MVP debe ser funcional, integral y documentado antes de avanzar.

## 🚀 **FASE 1: Preparación del lanzamiento**

### 1.1. **Crea el repositorio oficial**

* Nombre: `gloop` (o `gloop-git-switcher`)
* Descripción clara: *"Tray app to easily switch between global Git users"*
* Usa un buen README (ya lo tienes) con capturas, GIFs y badges de estado.

### 1.2. **Agrega documentación**

* Cómo instalar en cada SO
* Cómo contribuir (CONTRIBUTING.md)
* Cómo compilar
* Cómo reportar bugs
* Crea un `docs/` con guía extendida (opcional)

### 1.3. **Primera release estable**

* Usa GitHub Releases
* Sube artefactos `.exe`, `.app`, `.bin`, `.deb`
* Agrega changelog y notas destacando funcionalidades clave

---

## 📢 **FASE 2: Difusión orgánica y técnica**

### 2.1. **Promoción en comunidades de desarrollo**

* Publica en:

  * [Reddit](https://www.reddit.com/r/git), [r/opensource](https://www.reddit.com/r/opensource), [r/linux](https://www.reddit.com/r/linux), [r/devtools](https://www.reddit.com/r/devtools)
  * Grupos de Telegram/Discord sobre Git, PyQt, Linux, etc.
  * Hacker News (`news.ycombinator.com`)
  * Twitter/X con los hashtags `#git`, `#opensource`, `#devtools`, `#python`

> Ejemplo de post:
> *"¿Usas múltiples cuentas de Git y siempre te equivocas? Yo también. Por eso creé **Gloop**, una app de bandeja para cambiar entre usuarios globales de Git en un clic."*

### 2.2. **Publica en plataformas de código**

* GitHub Trending (consíguelo con estrellas orgánicas)
* Dev.to, Hashnode, Medium (escribe un post estilo "por qué lo hice")
* Publica un artículo en español en Platzi, Hackernoon o blogs veganos-tech

### 2.3. **Agrega a directorios de software**

* [Product Hunt](https://www.producthunt.com/)
* [AlternativeTo.net](https://alternativeto.net/)
* [AppImageHub](https://appimage.github.io/) (si usas AppImage)
* [Snapcraft](https://snapcraft.io/) o [Flathub](https://flathub.org/)

---

## 💖 **FASE 3: Fomentar comunidad y contribuciones**

### 3.1. **Crea un sitio sencillo**

* Con GitHub Pages o Astro/Netlify/Vercel
* Incluye capturas, badges, botón de "Star", instalación por sistema, changelog
* Añade sección "Contribuye" y "Agradecimientos"

### 3.2. **Activa GitHub Discussions**

* Para que usuarios puedan sugerir, preguntar y debatir sin abrir issues

### 3.3. **Agrega badges en el README con enlaces a donativos.**

Agrega badges en el README con enlaces a donativos.

### 3.4. **Publica un roadmap abierto**

* Usa issues y etiquetas como `good first issue` o `help wanted`
* Responde rápido a PRs y agradece públicamente las contribuciones

---

## 🌱 **FASE 4: Ampliar impacto**

### 4.1. **Incluye principios éticos**

* Explica que es libre de rastreadores, sin telemetría, sin APIs privativas
* Si deseas, menciona que busca apoyar la descentralización y el software ético

### 4.2. **Invita a forks y adaptaciones**

* Anima a que lo usen en VS Code, como extensión CLI, o integrado en IDEs
* Ofrece ganchos para integrarlo con plataformas como GitLab

### 4.3. **Conecta con el veganismo si lo deseas**

* Si abres donaciones, puedes decir que una parte irá a causas éticas (ej. refugios animales, desarrollo sustentable)
* Puedes dar charlas técnicas donde introduzcas tus herramientas open source y su ética

---

## ✅ Check rápido de lo esencial

| Elemento                     | ¿Listo? |
| ---------------------------- | ------- |
| README completo              | ✅       |
| Capturas y GIFs              | ☐       |
| Release con ejecutables      | ✅       |
| Logo o ícono del proyecto    | ✅       |
| Funding activado             | ☐       |
| Post en Reddit/HN/Twitter    | ☐       |
| Blog explicando el proyecto  | ☐       |
| Publicación en Product Hunt  | ☐       |
| Archivo CONTRIBUTING.md      | ☐       |
| Roadmap o proyectos abiertos | ☐       |

