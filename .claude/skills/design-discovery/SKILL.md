---
name: design-discovery
description: Entrevista interactiva para descubrir y definir el diseño de una web o app antes de implementarla. Usar cuando el usuario pida empezar un diseño, diseñar una app o pantalla desde cero, explorar un estilo, definir UX/UI, replantear la experiencia o buscar referencias. Preguntar por objetivos y referencias visuales, proponer direcciones y obtener aprobación antes de construir. No usar para cambios visuales pequeños y concretos que ya están completamente definidos.
---

# Design Discovery — entrevista de diseño

## Objetivo
Convertir una idea breve en una dirección de producto y diseño clara, con el mínimo esfuerzo del usuario. Guiá la conversación como diseñador de producto con criterio propio: averiguá lo que falta, proponé buenas opciones y no esperes que el usuario escriba un brief detallado.

## Cuándo activar
- Proyectos nuevos: «diseñá una app», «arranquemos con una web», «quiero crear la pantalla principal».
- Rediseños importantes o exploración de identidad: «no me convence esta interfaz», «exploremos el diseño».
- No activar cuando piden un arreglo simple, como mover un botón, cambiar un color o corregir un bug visual con especificaciones claras.

## Proceso

### 1. Leer antes de preguntar
- Revisá `CLAUDE.md`, `AGENTS.md`, `docs/PRODUCT.md`, `docs/DESIGN_SYSTEM.md`, pantallas y componentes existentes, si están disponibles.
- Si el usuario aporta documentos o capturas, analizalos primero.
- Identificá decisiones ya tomadas. Nunca preguntes lo que ya está respondido en el contexto.
- Si se trata de un producto nuevo, identificá audiencia, problema, tarea principal y plataforma (web, móvil o ambos).

### 2. Entrevistar en rondas breves
- Hacé **2–4 preguntas de alto impacto por ronda**, idealmente mediante `AskUserQuestion` si está disponible; de lo contrario, por conversación.
- Priorizá preguntas que cambien la solución, como: función principal, pantallas críticas, inspiración visual, tono de marca, alcance del MVP y decisiones que tienen varias opciones razonables.
- Ofrecé opciones concretas y una recomendación cuando resulte útil; permití «no sé, elegí vos».
- No hagas un formulario exhaustivo ni preguntes sobre detalles menores que podés resolver con criterio.
- Si el usuario ya quiere implementar y el contexto alcanza, no lo detengas con preguntas innecesarias.

### 3. Pedir y trabajar con referencias
- Invitá al usuario a aportar **1–3 capturas, enlaces o frames de Figma**. Preguntá qué le gusta de cada referencia (navegación, composición, tipografía, color, animación, etc.).
- Si no tiene referencias, ofrecé investigar y sugerir **2–3 direcciones visuales diferenciadas** usando las herramientas disponibles. Si no tenés acceso a búsqueda o Figma, explicalo y proponé alternativas razonadas sin inventar hallazgos.
- Separa lo que debe inspirar del material de referencia de lo que no conviene copiar. Evitá clonar sin pensar la identidad de otra aplicación.
- Respetá las preferencias globales y las decisiones del producto, sin imponer una moda visual.

### 4. Convertir el descubrimiento en una propuesta
- Antes de programar, resumí brevemente:
  - objetivo y flujo principal;
  - mapa de pantallas y navegación;
  - 2 o 3 decisiones visuales importantes, con razonamiento;
  - componentes base y estados (vacío, carga, error, éxito);
  - cuestiones abiertas, supuestos y alcance del primer entregable.
- Si hay varias direcciones viables, contrastalas y recomendá una.
- Pedí aprobación de la dirección **antes de un rediseño grande o implementación extensa**. No pidas aprobaciones por microdecisiones.
- Si el usuario quiere registrar el acuerdo, escribí `docs/DESIGN_BRIEF.md` y actualizá `docs/DESIGN_SYSTEM.md` solo con su consentimiento y de acuerdo con la estructura del repo.

### 5. Ejecutar después de la aprobación
- Reutilizá los componentes y patrones del proyecto.
- Aplicá accesibilidad, responsive, jerarquía visual, consistencia, animaciones con propósito y soporte para movimiento reducido cuando corresponda.
- No afirmes que comprobaste una pantalla si no ejecutaste la app y la viste. Si las herramientas lo permiten, probá en tamaños de móvil y escritorio; si no, indicá qué queda por verificar.
- Cuando el usuario pida una nueva funcionalidad sobre un diseño ya aprobado, no reinicies esta entrevista salvo que cambie el producto o haya una decisión fundamental pendiente.

## Estilo de interacción
- Claro, breve y con iniciativa. Tus preguntas deben ayudar al usuario a elegir, no delegarle todo el trabajo de diseño.
- Evitá muletillas como «actúo como experto» o promesas de calidad sin evidencia.
- No confundas «inspirado en iOS Liquid Glass» con usar el material nativo de iOS dentro de una app web.
- No presupongas que el usuario quiere replicar Snapchat, Apple u otra referencia salvo que exista una preferencia explícita.

## Definición de salida
La fase de descubrimiento termina cuando el usuario y el agente tienen una dirección suficientemente clara para implementar sin tener que renegociar continuamente la experiencia básica. El resultado principal es una especificación corta y utilizable, no una entrevista interminable.
