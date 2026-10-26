# Presentación práctica

Este procedimiento aplica a una modificación que la revisión ya ha situado en Mercurio. Una inicial EX-07 desde fuera de España sigue la autoridad/consulado competente y no debe fingirse como la misma secuencia electrónica.

1. Abrir la sede oficial actual, seleccionar provincia, formulario y rama tras contrastarlos con la ruta.
2. Confirmar la identidad del certificado o representación antes de rellenar. Un agente puede operar con la autorización existente; la persona interviene cuando lo exija la plataforma o el entorno.
3. Rellenar solo desde intake y documentos revisados. Mantener el mapa requisito → adjunto.
4. Cargar cada archivo final, comprobar SHA-256, categoría portal, número de adjuntos, tamaño y previsualización/resumen.
5. Revisar el resumen antes de firmar. AutoFirma se completa con la identidad correcta y los controles que imponga la sede.
6. Descargar de inmediato el resguardo y registrar REGAGE, fecha/hora, sujeto, formulario, provincia, lista de adjuntos, ruta privada y hash. Conciliar su lista con el mapa de carga.
7. Si hay WAF, timeout o pantalla incompleta después de firmar, marcar `submission.status` como `unknown`. Consultar expediente, notificaciones y resguardos antes de otro intento.
8. Si la oficina pide tasa, usar modelo, importe y plazo actuales. Registrar pago/NRC y aportación al expediente como eventos distintos; el segundo requiere su propio resguardo.
9. Monitorizar DEHú/notificaciones y expediente. Tras resolución, revisar contenido efectivo y el trámite de TIE aplicable; ningún estado intermedio equivale a aprobación.

No se debe sobrescribir `case.json` con `submitted` hasta conservar el resguardo oficial. Un paquete ya creado conserva `not_submitted`; registrar la entrega real en el ledger privado.
