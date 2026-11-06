---
name: visual-qa
description: Revisar y corregir visualmente interfaces web o mobile tras diseñar pantallas, modificar componentes, aplicar responsive o antes de entregar una UI. Usar automáticamente si la tarea cambia apariencia, navegación o interacción y existe navegador, capturas o tests visuales disponibles.
---
# QA visual y de interacción

1. Revisá los componentes y flujos afectados, y determiná los comandos reales para ejecutar el proyecto; no inventes scripts.
2. Ejecutá la app en el entorno disponible. Si existe navegador/Playwright, abrí las rutas afectadas y verificá tamaños móviles relevantes y escritorio cuando aplique. Si no existe, explicá cómo habilitarlo y verificá al menos render/compilación si es posible.
3. Mirá jerarquía, espaciado, tipografía, overflow, contraste, estado activo, navegación, botones, carga, errores y accesibilidad básica; si hay capturas de referencia compará visualmente.
4. Corregí defectos encontrados dentro del alcance, repetí la comprobación y ejecutá lint/typecheck/tests existentes según el proyecto.
5. Para cambios interactivos, probá al menos el flujo principal y uno de error o vacío cuando aplique.
6. Nunca declares una prueba pasada si no se ejecutó ni uses una captura ficticia como evidencia.
7. Informá rutas y tamaños revisados, comandos y resultados, problemas encontrados y qué quedó sin comprobar.
