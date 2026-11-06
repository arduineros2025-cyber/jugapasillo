# Usar el sistema Claude Code v2

Se integra el contenido de repo-template del ZIP claude-code-sistema-v2.zip, sin carpeta envolvente. CLAUDE.md importa AGENTS.md y .claude/BASELINE.md. Las siete skills están en .claude/skills/<nombre>/SKILL.md.

1. Revisar e incorporar este PR, o abrir una sesión con su rama.
2. En Claude Code web seleccionar este repositorio y abrir una sesión nueva.
3. Pedir: «Leé CLAUDE.md, verificá las siete skills y resumí las reglas del proyecto. No cambies la app ni hagas deploy».
4. Probar /ui-design, /design-discovery, /app-architecture, /feature-development, /asset-sourcing, /visual-qa y /project-memory cuando corresponda; no hace falta activarlas todas para una tarea.

## Cloud y Projects
Las rutas siguen el formato de [skills de proyecto](https://code.claude.com/docs/en/skills). Los hilos cloud dentro de un Project no cargan las skills del repositorio: habilitarlas en la cuenta, Customize/Skills. Las skills locales de ~/.claude/skills no se trasladan solas a cloud. Comprobar qué cargó la sesión; esta instalación no modifica la cuenta de Claude.

## Herramientas opcionales
El helper de Pexels requiere Python 3, PEXELS_API_KEY en el entorno y acceso de red. Desde la raíz: python .claude/skills/asset-sourcing/scripts/fetch_pexels.py --help. No almacenar claves en Git. La skill no instala navegador, MCP ni credenciales. Fotos, pruebas visuales y red solo se declaran verificadas después de ejecutarlas.

## Verificación de instalación
Comprobar imports, nombres y descripciones de SKILL.md, y que el helper existe. Los checks de aplicación y la carga real en Claude se informan por separado en el PR.
