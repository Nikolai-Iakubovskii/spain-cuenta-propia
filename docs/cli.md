# Caso privado y preflight CLI

El caso vive fuera del repositorio. Inicialízalo con `init`; el archivo `case.json` y `PRIVATE.md` creados son deliberadamente incompletos.

```bash
python3 scripts/cuenta_propia.py init /private/cuenta-case --route modification-191-3
# añadir originales a /private/cuenta-case/documents/
python3 scripts/cuenta_propia.py inventory /private/cuenta-case --json
# copiar los SHA-256 del inventario a case.json y completar revisiones
python3 scripts/cuenta_propia.py audit /private/cuenta-case --json
python3 scripts/cuenta_propia.py bundle /private/cuenta-case
```

`inventory` puede ejecutarse antes de terminar revisiones. Descubre archivos regulares bajo `documents/` sin modificar el manifiesto, y devuelve `registered` y `unregistered` con ruta, bytes y hash. Tras inventariar, el agente registra en `documents[]` solo los archivos pertinentes y deja la revisión sustantiva. `audit` devuelve distinto de cero hasta que todo esté completo. `bundle` exige auditoría verde, que `submission.status` sea `not_submitted`, y vuelve a comprobar los bytes antes de copiar. No use el bundle para reempaquetar una solicitud ya enviada.

## Esquema mínimo completo

Los valores siguientes son estructura, no hechos que deban copiarse en una solicitud:

```json
{
  "schema_version": 1,
  "route": "modification-191-3",
  "applicant": {"name": "Privado", "nationality": "Privado", "province": "Provincia"},
  "reviews": {
    "sources": {
      "status": "complete", "reviewed_on": "2026-10-26", "reviewer": "agent",
      "notes": "Norma, sede y provincia contrastadas.",
      "evidence": [{"url": "https://example.invalid/official", "section": "Artículo/sección", "checked_on": "2026-10-26", "notes": "Qué prueba para el caso."}]
    },
    "route": {
      "status": "complete", "reviewed_on": "2026-10-26", "reviewer": "agent",
      "notes": "Ruta y legitimación explicadas.",
      "evidence": [{"url": "https://example.invalid/official", "section": "Artículo/sección", "checked_on": "2026-10-26", "notes": "Por qué aplica."}]
    },
    "content": {"status": "complete", "reviewed_on": "2026-10-26", "reviewer": "agent", "notes": "Documentos revisados sustantivamente."}
  },
  "requirements": [{"id": "identity", "title": "Identidad", "basis": "Base actual", "source_url": "https://example.invalid/official", "status": "applicable", "documents": ["passport"]}],
  "documents": [{"id": "passport", "path": "documents/passport.pdf", "sha256": "SHA256_DEL_INVENTORY", "content_review": {"status": "complete", "reviewed_on": "2026-10-26", "reviewer": "agent", "notes": "Completo, identidad y vigencia revisadas."}, "expires_on": ""}],
  "portal": {"confirmed_on": "2026-10-26", "max_file_bytes": 6000000, "extensions": [".pdf", ".doc", ".jpg", ".tif", ".gif"]},
  "submission": {"status": "not_submitted"}
}
```

`reviews.sources` y `reviews.route` exigen al menos una evidencia con `url`, `section`, `checked_on` y `notes`. Las fechas de revisión y comprobación no pueden ser futuras; `expires_on` de un documento sí puede ser una fecha futura. `content_review` exige fecha, revisor, estado completo y nota. Un requisito `conditional` bloquea: resolverlo como `applicable` o `inapplicable`, con `reason` para este último. Los IDs son minúsculos, únicos y los requisitos aplicables deben referenciar documento.

El portal se confirma para el caso actual. El valor inicial de 6 MB y `.pdf`, `.doc`, `.jpg`, `.tif`, `.gif` procede del manual Mercurio histórico: revisar interfaz actual antes de usarlo. Las extensiones adicionales solo se aceptan si quedan registradas con esa confirmación.
