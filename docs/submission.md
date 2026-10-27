# Presentación práctica

Este procedimiento aplica a una modificación o renovación que la revisión ya ha situado en [Mercurio](https://sede.administracionespublicas.gob.es/mercurio/inicioMercurio.html). Una inicial EX-07 desde fuera de España se presenta personalmente en el consulado y no debe fingirse como la misma secuencia electrónica.

1. Abrir la sede oficial actual, seleccionar provincia, formulario y rama tras contrastarlos con la ruta. Confirmar que hoy está dentro de la ventana de presentación de la ruta.
2. Confirmar la identidad del certificado o representación antes de rellenar. Un agente puede operar con la autorización existente; la persona interviene cuando lo exija la plataforma o el entorno.
3. Rellenar solo desde intake y documentos revisados. Mantener el mapa requisito → adjunto.
4. Cargar cada archivo final, comprobar SHA-256, categoría portal, número de adjuntos, tamaño y previsualización/resumen.
5. Revisar el resumen antes de firmar. AutoFirma se completa con la identidad correcta y los controles que imponga la sede.
6. Descargar de inmediato el resguardo y registrar REGAGE, fecha/hora, sujeto, formulario, provincia, lista de adjuntos, ruta privada y hash. Conciliar su lista con el mapa de carga.
7. Si hay WAF, timeout o pantalla incompleta después de firmar, marcar `submission.status` como `unknown`. Consultar expediente, notificaciones y resguardos antes de otro intento.
8. Tasa: usar el impreso 790 y el epígrafe de la ruta ([rutas](routes-and-sources.md)); en modificaciones se paga en los diez días hábiles siguientes a la admisión a trámite. Registrar pago/NRC y aportación al expediente como eventos distintos; el segundo requiere su propio resguardo.
9. Monitorizar DEHú/notificaciones y expediente cada pocos días: diez días naturales sin abrir una notificación electrónica equivalen a rechazarla. Un requerimiento se contesta en diez días hábiles por "aportación de documentación", con su propio resguardo.
10. Tras la resolución, revisar su contenido efectivo; si es favorable, alta en Seguridad Social y TIE en los plazos de la ruta; si es desfavorable, anotar el pie de recurso y elevarlo. Ningún estado intermedio equivale a aprobación.

No se debe sobrescribir `case.json` con `submitted` hasta conservar el resguardo oficial. Un paquete ya creado conserva `not_submitted`; registrar la entrega real en el ledger privado.
