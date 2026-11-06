---
name: asset-sourcing
description: Buscar, seleccionar, integrar y verificar fotos e imágenes reales para interfaces y aplicaciones. Usar automáticamente cuando el diseño requiera fotografía, imágenes de producto, personas reales, jugadores, fondos, ilustraciones o assets visuales y el usuario no haya entregado los archivos. No confundir investigación visual con permiso de publicación.
---

# Asset sourcing — imágenes reales, no placeholders

## Comportamiento predeterminado
- Si una interfaz requiere imágenes, investigar y obtener assets reales apropiados usando herramientas disponibles, sin esperar a que el usuario lo pida otra vez.
- Buscar primero si el proyecto ya cuenta con assets, design system, CMS o data pack que deban reutilizarse; respetar licencias y nombres existentes.
- No sustituir automáticamente fotografías por emojis, gradientes decorativos o placeholders genéricos.
- No inventar URLs, no asumir que una foto encontrada en buscadores es libre de uso y no declarar que fue descargada si no existe un archivo verificado.
- Para una tarea visual importante, evaluar 3-6 candidatos por composición, encuadre, calidad, tema y adecuación a marca. Priorizar imagen correcta por sobre primera coincidencia.

## Elegir la fuente según tipo de activo
1. Fotografías genéricas de estilo de vida, ciudad, ambientes, eventos: Pexels API (primera opción) u otros proveedores con licencias adecuadas. Si está disponible un MCP de imágenes, usar sus herramientas de búsqueda y descarga.
2. Fotografías aportadas por usuario o cliente: prioridad máxima; no enviarlas a servicios externos sin necesidad y autorización.
3. Personas reconocibles, futbolistas, camisetas, escudos, equipos o productos específicos: buscar fuentes específicas y medios con autorización de reutilización, metadatos y derechos. No sustituir el jugador pedido por una persona genérica.
4. Wikimedia Commons puede aportar fotos de personas, edificios, estadios y eventos. Consultar metadatos de CADA archivo con imageinfo/extmetadata; la licencia y requisitos de atribución dependen del archivo.
5. Unsplash vía su API oficial requiere usar las URL de su CDN directamente y dar las atribuciones exigidas por la API; no aplicar por defecto la regla de descargar y rehostear todas las imágenes de Unsplash.
6. Imagen generada por IA: solo si el usuario la solicita o existe una instrucción del proyecto que autoriza ese contenido. No inventar fotografías documentales de personas/eventos reales.

## Procedimiento
1. Leer el objetivo y los requisitos de la pantalla (tamaño, relación de aspecto, encuadre, posición del sujeto, estilo, fondo).
2. Buscar imágenes mediante un MCP de imágenes, API del proveedor o navegador autorizado. Si falta alguna herramienta, informar el bloqueo concreto en vez de abandonar la búsqueda.
3. Verificar URL accesible, procedencia, pertinencia, resolución, formato y condiciones de uso antes de integrar. Nunca ocultar incertidumbre de permisos.
4. Para Pexels, si no hay MCP, usar `${CLAUDE_SKILL_DIR}/scripts/fetch_pexels.py` con `PEXELS_API_KEY`, bajo permiso de red. Requiere Python 3; no añade dependencias. Revisar candidatos antes de elegir.
5. Guardar el resultado en el directorio de assets del proyecto (por ejemplo `public/images/`) cuando las condiciones de la fuente lo permitan; usar el formato correcto y optimizar tamaños para web. Un archivo grande sin optimizar no está terminado.
6. Integrar asset en los componentes, añadir `alt` adecuado, diseño responsive y medidas para evitar layout shifts.
7. Registrar al menos fuente, URL original, autor, licencia/condiciones consultadas, fecha de consulta y ubicación local o URL CDN en `docs/ASSET_SOURCES.md` o en el data pack existente. No inventar datos que no aparecen.
8. Abrir la página o correr checks reales y comprobar que las imágenes cargan. Si no hubo navegador disponible, inspeccionar que las rutas existen y dejar claro qué no se verificó.

## Si la imagen no se puede obtener
- Diferenciar causas: herramienta no instalada, sin credencial, falta de acceso a Internet, error 403/404, bloqueo de CDN, falta de licencia o ausencia de un resultado válido.
- No decir «no puedo usar imágenes de Internet» como respuesta genérica: explicar qué fuente concreta probaste y qué falló.
- Proponer la mejor fuente alternativa con derechos adecuados. Para un avatar/jugador específico, marcar el registro como pendiente con su ID real, nunca asignar una foto de una persona equivocada.
- No evadir bloqueos de acceso, paywalls ni mecanismos de autenticación de terceros.

## Convenciones del repositorio
Leer `docs/ASSET_SOURCES.md` y las reglas de fuentes existentes antes de buscar. Mantener los formatos y registros ya usados. Las condiciones específicas del proyecto tienen prioridad sobre la selección genérica de proveedores.
