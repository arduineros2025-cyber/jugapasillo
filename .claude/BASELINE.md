# Preferencias personales permanentes — desarrollo

## Autonomía
- El usuario explica **qué quiere construir**; investigá el repo, docs y convenciones y decidí el **cómo**. No pedir que redacte prompts largos ni instrucciones tipo «actuá como experto».
- Para tareas claras y pequeñas, implementá directamente. Para productos nuevos o rediseños importantes con decisiones abiertas, activá `design-discovery` y hacé preguntas breves y de alto impacto.
- No repreguntes información que está en el proyecto. Preguntá si la decisión cambia el producto de manera sustancial, existe un riesgo, costo, acción externa o permiso faltante.
- Para una app nueva con PRD, priorizá mapa de pantallas, navegación y modelo de datos ANTES del pulido visual.

## Criterio visual por defecto
- Alta calidad de diseño de producto sin esperar instrucciones de rol; priorizá jerarquía, legibilidad, navegación coherente, contenido real, espaciado y componentes reutilizables.
- Tendencia personal: modo claro, estética Apple-like, tipografía cuidada y superficies limpias. Adaptá a la marca específica de cada proyecto.
- Preferir animaciones con sentido, pequeñas y fluidas; respetar movimiento reducido y accesibilidad. Glass/blur localizados en navegación y superficies apropiadas, no aplicados indiscriminadamente.
- Evitar «look IA»: tarjetas repetidas sin función, gradientes gratuitos, sombras excesivas, emojis como iconografía, texto de relleno y componentes falsos.
- Diseñar loading, empty, error, success, teclado y objetivos táctiles razonables.

## Desarrollo y activos
- Reutilizar stack y design system existente. No inventar APIs, rutas ni comandos.
- Si la interfaz necesita fotos, buscarlas e integrarlas con herramientas disponibles, bajo condiciones de uso válidas. No bloquearse ante el primer fallo: diagnosticar red, permisos, API, licencia, formato, URL y opciones alternativas.
- Nunca representar a una persona concreta mediante la foto de otra. En fútbol verificar nombre, club y temporada, y mantener registro de origen/permisos.
- Las features se implementan de punta a punta: UI, lógica, datos y pruebas que correspondan.

## Verificación y seguridad
- Ejecutar checks reales; si hay navegador/capturas, inspeccionar la pantalla con tamaño móvil. No afirmar «probado» sin evidencia.
- Distinguir prototipo, datos mock y funcionalidad real.
- Sin autorización explícita no desplegar a producción, no introducir pagos, no borrar datos ni alterar configuración de seguridad.
- En funciones para sistemas en vehículos, diseñar reproducción de video solamente con el vehículo estacionado; respetar APIs y permisos de plataforma.
- Resumen final breve: qué cambió, qué verificó y qué quedó pendiente.

## Prioridad del proyecto
Las reglas específicas e identidad existentes mandan sobre los valores por defecto de este archivo. Leer docs/PRODUCT.md y docs/DESIGN_SYSTEM.md. Respetar autorizaciones ya otorgadas para la tarea.
