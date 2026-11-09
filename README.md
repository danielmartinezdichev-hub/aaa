# PortMediterránea — monitor de jugadores

Esta web muestra jugadores conectados, visitas, favoritos y la fecha de última actualización publicada por Roblox.

## Cómo publicarla con GitHub Pages

1. Entra en https://github.com y crea un repositorio nuevo, por ejemplo `portmediterranea-monitor`.
2. Sube **todo el contenido** de esta carpeta al repositorio, incluida la carpeta `.github`.
3. En el repositorio abre **Settings → Pages**.
4. En **Build and deployment**, elige **Deploy from a branch**; selecciona `main` y `/ (root)`, y guarda.
5. Abre **Actions**, selecciona el workflow “Actualizar estadísticas de PortMediterránea” y pulsa **Run workflow** una vez.
6. Cuando termine correctamente, abre la web de GitHub Pages. La URL tendrá esta forma:
   `https://TU-USUARIO.github.io/portmediterranea-monitor/`

## Actualización

GitHub Actions intenta consultar Roblox cada 5 minutos. La programación puede retrasarse por la cola de GitHub. La primera ejecución manual es necesaria para crear los primeros datos.

## Importante

- El ID `137253701602745` de la URL es el **Place ID**. El script lo convierte al **Universe ID** antes de pedir las estadísticas.
- El navegador del instituto solo necesita cargar la página de GitHub Pages y sus archivos JSON; no consulta directamente los dominios de Roblox.
- Esto no garantiza que funcione si el cortafuegos del centro bloquea GitHub Pages o los archivos del repositorio.
- La fecha `updated` es la última actualización publicada que Roblox informa; `capturedAt` es cuándo se consultaron las estadísticas.
- No contiene contraseñas, cookies ni datos privados.
