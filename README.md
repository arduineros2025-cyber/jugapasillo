# Pasillo del Conocimiento

Juego de mesa web para 2 jugadores (modo local, se turnan en la misma
computadora). Mezcla estrategia y trivia: movés tu peón o respondés
preguntas para ganar paredes que bloquean el paso del rival.

Hecho con **Vite + React + TypeScript + Tailwind CSS**. Sin backend, sin
base de datos, sin internet: todo corre en el navegador.

## Cómo jugarlo en tu compu

1. Abrí una terminal en esta carpeta.
2. La primera vez, instalá las dependencias:

   ```bash
   npm install
   ```

3. Iniciá el juego:

   ```bash
   npm run dev
   ```

4. Abrí en el navegador la dirección que aparece (normalmente
   `http://localhost:5173`).

Para frenarlo, apretá `Ctrl + C` en la terminal.

## Cómo publicarlo gratis en Vercel (para abrirlo desde cualquier lado)

Esto le da un link público (ej: `pasillo-del-conocimiento.vercel.app`) que
podés abrir desde cualquier computadora con internet y compartir por
WhatsApp o pegar en una presentación.

### 1) Subir el proyecto a GitHub

- Entrá a https://github.com y creá una cuenta gratis (si no tenés).
- Hacé clic en el botón verde **New** (repositorio nuevo).
- Ponele un nombre, por ejemplo `pasillo-del-conocimiento`, y dale **Create repository**.
- GitHub te muestra una página con instrucciones. La forma más simple sin
  saber programar: instalá **GitHub Desktop** (https://desktop.github.com),
  iniciá sesión, elegí **Add** → **Add existing repository**, seleccioná
  esta carpeta y dale **Publish**. Listo, tu código queda en GitHub.

### 2) Importar el proyecto en Vercel

- Entrá a https://vercel.com y hacé clic en **Sign Up**. Elegí
  **Continue with GitHub** (así se conectan solos).
- Una vez adentro, hacé clic en **Add New…** → **Project**.
- Vercel te muestra tus repositorios de GitHub. Buscá
  `pasillo-del-conocimiento` y hacé clic en **Import**.

### 3) Configuración

- **Framework Preset**: Vercel detecta **Vite** solo. Dejalo así.
- El resto de las opciones, dejalas **por defecto** (no toques nada).
- Hacé clic en **Deploy** y esperá un minuto.

### 4) ¡Listo!

Vercel te da un link público. Abrilo, probá el juego, y compartí ese link
con quien quieras. Cada vez que subas cambios a GitHub, Vercel actualiza
la página sola.

> **Nota sobre la red de la escuela:** el juego se sirve desde internet
> (Vercel), así que cada computadora lo abre entrando al link. No hace
> falta conectar las compus entre sí: como es modo local (2 jugadores en
> la misma máquina), alcanza con que cada una tenga internet para abrir
> la página.
