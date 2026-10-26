# Workflow de caso

## 1. Intake y límite de autoridad

Registrar en el caso privado: persona y representación, provincia de residencia efectiva, autorización/TIE y fecha de caducidad, tiempo de residencia, derecho previo a trabajar, actividad, familia, plazos y `mode`. Cuando exista DNV/Ley 14/2013, añadir autorización y actividad de origen, naturaleza y fecha del cambio acreditado, continuidad frente a cambio de negocio y coordinación/UGE pendiente o resuelta.

- `prepare`: recopilar, analizar, redactar y crear paquete local; no presentar.
- `prepare-and-submit`: permite presentar la ruta verificada en la sede oficial. No implica abrir cuentas, pagar, enviar emails o solicitar documentos a terceros salvo que el usuario lo haya incluido.

## 2. Fuente actual y decisión de ruta

Antes de listar documentos, obtener las fuentes oficiales aplicables el día de trabajo. En `case.json`, completar `reviews.sources`, `reviews.route` y `reviews.content` con fecha, revisor y estado. Resolver o elevar contradicciones entre BOE, hoja, oficina/provincia y portal.

 Elegir una sola ruta principal. Para cada requisito, registrar `basis`, `source_url`, `status`, `reason` y los documentos que lo apoyan. `status` es la decisión de aplicabilidad: `applicable`, `conditional` o `inapplicable`. Los dos últimos requieren razón; `conditional` bloquea el paquete hasta convertirse en aplicable o inaplicable. `applicable` no se considera listo sin evidencia revisada.

## 3. Recogida y revisión

Copiar o enlazar únicamente originales que el usuario autorizó. Revisar de forma sustantiva:

- pasaporte completo, TIE/resoluciones, nombres, NIE, fechas, provincia y coherencia entre formularios;
- vigencia, originalidad, firma, apostilla/traducción jurada cuando sean aplicables;
- alta/actividad, obligaciones tributarias y Seguridad Social para la ruta invocada;
- extractos, facturas y declaraciones: período, moneda, titularidad, conciliación de cifras reales frente a pronósticos;
- business plan y escrito explicativo: hechos trazables, supuestos etiquetados y ninguna cifra o afirmación inventada.

Registra una `content_review` fechada con revisor, estado y nota por documento. OCR, hash o una vista previa no sustituyen esa revisión.

## 4. Auditoría y paquete

Usa `inventory` para registrar hashes y `audit` para detectar metadatos, vigencias, ruta y limitaciones técnicas. `reviews.sources` y `reviews.route` necesitan estado completo, fecha, revisor, nota y evidencia URL/sección/fecha; `reviews.content` necesita también nota. El resultado verde solo declara preflight técnico. `bundle` copia bytes sin alterar; no altera firmas ni marca una presentación y exige `submission.status: not_submitted`.

El paquete debe incluir un índice de adjuntos que se concilie con la selección final del portal. Revisa el archivo de origen una segunda vez si fue modificado desde el inventario.

## 5. Presentación y cierre

Accede solamente a la sede oficial vigente con la identidad y representación adecuadas. La persona interviene cuando sea necesario para certificado electrónico, AutoFirma, MFA, CAPTCHA o firma física.

Después de firmar, guarda inmediatamente el `resguardo` original y su hash. Solo se declara registrada cuando contiene REGAGE, fecha/hora, sujeto, formulario, provincia y adjuntos conciliados. Si aparece WAF, error o timeout, anota `unknown`, consulta expediente/notificaciones y no vuelve a firmar hasta resolverlo.

Las tasas siguen el requerimiento y modelo actuales. Conservar, por separado, la prueba de pago/NRC y el `resguardo` de aportación al expediente. Luego vigilar DEHú/notificaciones, estado, resolución y trámite de TIE; no inferir aprobación por un estado intermedio.
