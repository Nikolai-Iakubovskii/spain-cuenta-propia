# Revisión de documentos

La revisión tiene dos capas. La herramienta cubre integridad técnica; una persona o agente competente deja constancia de la lectura sustantiva.

| Control | Evidencia en el caso |
| --- | --- |
| Archivo exacto | ruta privada, SHA-256 y tamaño |
| Vigencia | fecha de emisión/caducidad y regla/fuente usada |
| Identidad | nombre, NIE/pasaporte, fecha de nacimiento y coincidencias |
| Integridad material | documento completo, páginas legibles, sin sustitución o recorte |
| Requisitos formales | firma, emisor, apostilla/legalización y traducción si aplican |
| Relación con requisito | requisito, fuente, `status` de aplicabilidad y explicación |
| Revisión | `reviewed_on`, revisor, estado y nota de contenido |

No declares que una firma, sello, traducción, documento escaneado u OCR son válidos solo porque el archivo abre. Un certificado antiguo, una tasa de otro expediente o un extracto de un período diferente deben quedar como conflicto hasta resolverlos.

Para documentos financieros, separar dato histórico de previsión y anotar fuente, período y cálculo. Para documentos repetidos, asignar cada copia a su finalidad; si la asignación es ambigua, bloquear el bundle.
