@AGENTS.md
@.claude/BASELINE.md

# Claude Code — este repositorio

- Leé `docs/PRODUCT.md` como índice de las fuentes existentes. Esas fuentes y las instrucciones específicas del proyecto tienen prioridad sobre los valores genéricos del kit.
- La identidad y componentes existentes tienen prioridad sobre las preferencias globales; consultá `docs/DESIGN_SYSTEM.md` antes de diseñar.
- Invocá las skills pertinentes automáticamente: `design-discovery` cuando hay decisiones abiertas, `app-architecture` para apps nuevas, `ui-design` para UI, `feature-development` para features, `asset-sourcing` cuando hacen falta fotos, `visual-qa` al terminar cambios visuales, `project-memory` al consolidar decisiones duraderas.
- No es necesario que el usuario escriba prompts detallados, pero los permisos externos, compras, despliegues y acciones irreversibles requieren confirmación.
- No asumir que una skill o tool existe hasta comprobarlo en la sesión actual.
