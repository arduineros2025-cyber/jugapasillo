---
name: project-memory
description: Registrar decisiones de producto, arquitectura, diseño y aprendizajes persistentes de un repositorio. Usar cuando el usuario fija una decisión, aprueba una dirección de diseño, cambia un principio del producto o finaliza una implementación relevante. No usar para transcribir conversaciones triviales.
---
# Memoria versionada del proyecto

1. Revisá si el repo tiene `docs/DECISIONS.md`, `docs/PRODUCT.md`, `docs/DESIGN_SYSTEM.md`, ADRs, changelog o bitácora. Reutilizá la convención existente.
2. Separá decisión explícita del usuario, inferencia y tema pendiente. No conviertas una hipótesis en requisito definitivo.
3. Registrá solo decisiones duraderas en `docs/DECISIONS.md` (fecha, decisión, contexto, impacto y estado) y actualizá el documento canónico si corresponde.
4. Si una feature quedó implementada, actualizá el estado de la hoja de ruta sin afirmar que está desplegada o probada si no lo verificaste.
5. Si hay contradicción con una decisión previa, destacala; no borres silenciosamente el historial.
6. No guardes credenciales, datos personales innecesarios, conversaciones privadas ni material no relacionado con el proyecto.
7. No crees un segundo sistema de memoria que duplique el existente sin necesidad.
