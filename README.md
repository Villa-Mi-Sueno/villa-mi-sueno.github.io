# Villa Mi Sueño · Welcome book (web)

Guía para huéspedes: https://villa-mi-sueno.github.io/vms/

- **Contenido:** Excel `VMS_contenido.xlsx` en Google Drive (carpeta *Villa Mi Sueño/WEB_CONTENIDO*). Se edita desde Google Sheets.
- **Publicación:** GitHub Actions lee el Excel cada 15 minutos y, si cambió, regenera y publica la web. Para publicar al momento: pestaña *Actions* → *Publicar welcome book* → *Run workflow*.
- **Fotos y diseño:** se cambian en el Mac (proyecto VMS_VB_SENALETICA) y se suben con `99_SCRIPTS/preparar_repo.sh`.
- **Sin conexión:** la web es una PWA; tras la primera visita funciona sin señal.
