# Rutas y fuentes oficiales

Comprobado el 2026-10-27 contra el [texto consolidado del RD 1155/2024](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099) (última actualización publicada el 22/09/2026; incluye la reforma del [RD 316/2026](https://www.boe.es/buscar/doc.php?id=BOE-A-2026-8284)), el [criterio DGGM 1/2025](https://www.inclusion.gob.es/documents/d/migraciones/criterio-de-gestion-dggm-1-2025_rloex_modificaciones-estancias-y-residencias-y-prorrogas-arraigos) y las hojas informativas del Ministerio de Inclusión. Las hojas son orientativas; la norma y la sede vigentes el día de presentar prevalecen. Lista completa de artículos y enlaces: [normativa](legal-basis.md). Documentos por ruta: [checklists](checklists.md). Situaciones particulares: [casos especiales](special-cases.md).

## Elegir la ruta

| Situación actual | Ruta (`route` del CLI) | Base | Formulario | Dónde | Resultado |
| --- | --- | --- | --- | --- | --- |
| Residencia de al menos un año que ya habilita a trabajar (cuenta ajena, cuenta propia, arraigo, DNV u otra de Ley 14/2013…) | Modificación `modification-191-3` | [art. 191.3](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a1-103) → requisitos del [art. 86](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a8-8); [Hoja 55](https://www.inclusion.gob.es/web/migraciones/w/55.-modificacion-desde-situaciones-de-autorizaciones-de-residencia-temporal-que-habilitan-a-trabajar) | EX-26 | Mercurio u Oficina de Extranjería de la provincia | 4 años |
| Residencia de al menos un año que no habilita a trabajar (p. ej., no lucrativa) | Modificación `modification-191-4` | [art. 191.4](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a1-103) → [art. 84](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a8-6); [Hoja 55 bis](https://www.inclusion.gob.es/web/migraciones/w/55-bis.-modificaciones-desde-situaciones-de-residencia-que-no-habilitaban-a-trabajar) | EX-26 | Mercurio u oficina | 1 año |
| Estancia por estudios o formación, con título o certificado obtenido | Modificación `modification-190-3` | [art. 190.3](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a1-102) → art. 84; [Hoja 58](https://www.inclusion.gob.es/web/migraciones/w/58.-modificaciones-desde-autorizaciones-de-estancia-por-estudios-superiores-ensenanza-secundaria-actividades-formativas-o-formacion-sanitaria-especializada) | EX-26 | Mercurio u oficina, personalmente | 1 año |
| Cuenta ajena inicial, durante su primer año | Modificación `modification-192-2` | [art. 192.2](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a1-104); criterio 1/2025 | confirmar en la sede: no hay hoja específica en el [listado](https://www.inclusion.gob.es/web/migraciones/listado-completo) | Mercurio u oficina | No amplía la vigencia de la autorización modificada |
| Ya titular de cuenta propia que caduca | Renovación `renewal-ex07` | [arts. 86–87](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a8-8); [Hoja 15](https://www.inclusion.gob.es/web/migraciones/w/15.-renovacion-de-la-autorizacion-de-residencia-temporal-y-trabajo-por-cuenta-propia) | EX-07 | Mercurio | 4 años |
| No residente en España | Inicial `initial-ex07` | [arts. 38–39](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a3-10) y [82–85](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a8-4); [Hoja 14](https://www.inclusion.gob.es/web/migraciones/w/autorizacion-inicial-de-residencia-temporal-y-trabajo-por-cuenta-propia) | EX-07 | Consulado de su residencia, personalmente | 1 año, una comunidad autónoma y un sector |
| Familiar del titular | Expediente propio `family-ex02` | [arts. 65–66](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a6-7); Hojas [8](https://www.inclusion.gob.es/web/migraciones/w/autorizacion-de-residencia-temporal-por-reagrupacion-familiar), [10](https://www.inclusion.gob.es/web/migraciones/w/renovacion-de-la-autorizacion-de-residencia-por-reagrupacion-familiar.), [11](https://www.inclusion.gob.es/web/migraciones/w/autorizacion-de-residencia-independiente-de-familiares-reagrupados.) | EX-02 u otro según la vía | Según la hoja | Según la vía |

Antes de elegir, comprueba si ya puedes trabajar por cuenta propia sin trámite: la autorización renovada de cuenta ajena o propia habilita a ambas ([art. 81.1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a8-3), [art. 87.1](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a8-9)) y la reagrupación familiar del cónyuge, pareja o hijo también ([art. 65.2](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a6-7)). Formularios vigentes: [modelos generales](https://www.inclusion.gob.es/es/web/migraciones/modelos-generales).

## 1. Modificación art. 191.3: residencia que ya habilitaba a trabajar

Ruta principal del repositorio. Requisitos: al menos un año en España en situación de residencia y una autorización que ya habilitaba a trabajar por cuenta ajena o propia. Para pasar a cuenta propia se acredita uno de los supuestos del art. 86.2, igual que en una renovación:

- continuidad de la actividad que dio lugar a la autorización, con obligaciones tributarias y de Seguridad Social cumplidas (la oficina lo comprueba de oficio; conviene conservar la evidencia);
- un familiar del art. 66 con medios para reagrupar a la persona;
- protección por cese de actividad reconocida;
- TRADE cuyo contrato se interrumpe o extingue por causas ajenas;
- prestación contributiva por desempleo o prestación asistencial de inserción ([LOEX art. 38.6 b) y c)](https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#a38)).

Además, informe de escolarización de los menores a cargo en edad obligatoria (art. 86.3). Si falta algún requisito, puede valorarse el informe de esfuerzo de integración de la comunidad autónoma (art. 86.6).

- **Cuándo presentar** (criterio 1/2025, apartado 1.b): en los dos meses previos o los tres posteriores a la caducidad; si la autorización dura más de un año y ya pasó el primero, en cualquier momento y hasta tres meses después de caducar. Presentar en plazo prorroga la autorización actual hasta la resolución y así consta en el acuerdo de admisión a trámite.
- **Tasas**: 790-052 epígrafe 2.5.2 y 790-062 "autorización de trabajo para autorizaciones renovadas de residencia temporal de trabajo por cuenta propia" (epígrafe 3.3.2 en la numeración de las hojas; 3.2 en el impreso), devengadas al admitirse a trámite y pagaderas en diez días hábiles. La Hoja 55 solo cita el 790-062 de cuenta ajena; en un caso real de octubre de 2026 (191.3 desde DNV) la oficina pidió estas dos tasas por requerimiento, con los impresos ya emitidos (10,94 € y 81,54 €), y dio quince días desde el pago para aportar los justificantes por la sede.
- **Plazo y silencio**: tres meses; sin notificación se entiende **desestimada** ([DA 8.ª](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#da-8); criterio 1/2025, apartado 4).
- **Después de conceder**: la Hoja 55 pide el alta en Seguridad Social en el mes siguiente a la notificación (la eficacia queda condicionada a ella) y la TIE, personalmente, en el mes siguiente al alta. Si ya estás de alta en RETA, guarda la vida laboral que lo prueba y confirma con la oficina que basta. Vigencia: cuatro años; la eficacia se retrotrae al día siguiente a la caducidad anterior si ya se produjo.

La lista de la Hoja 55 no incluye plan de empresa, informe de ATA, padrón, informe de vivienda ni una cifra fija de ingresos para este supuesto. Si la actividad nueva no es continuación de la anterior, la "continuidad" del art. 86.2.a deja de ser evidente: el agente lo documenta y valora preparar también la prueba del art. 84 (licencias, cualificación, inversión) como respaldo, sin presentarla como requisito de la hoja.

Errata conocida: en el apartado "más de un año", la Hoja 55 (agosto de 2025) repite "menos de un año" entre los requisitos. Manda el art. 191.3: al menos un año.

### Desde Ley 14/2013 (DNV, teletrabajo internacional y demás)

El apartado 3 del criterio 1/2025 dice que estas autorizaciones se rigen por la Ley 14/2013 para obtenerlas, conservarlas y renovarlas, y que el sistema de modificaciones del RD 1155/2024 se aplica cuando se producen cambios que impiden mantenerlas ([DF 13.ª Ley 14/2013](https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#dfdecimotercera)):

- la modificación se pide ante la Delegación o Subdelegación del Gobierno **en los tres meses siguientes** a la fecha en que se produce el cambio;
- con al menos un año de residencia se acreditan los requisitos del art. 80 o del art. 86 y la nueva autorización dura cuatro años desde la resolución; no hace falta visado;
- la Oficina de Extranjería comunica el resultado a la Unidad de Grandes Empresas y Colectivos Estratégicos (UGE) y ambas coordinan la extinción de la autorización de Ley 14/2013.

Para la DNV, un cambio típico es dejar de cumplir el [art. 74 bis.1](https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a7-2): como profesional, el trabajo para empresas en España no puede superar el 20 % de la actividad; como empleado, solo se trabaja para empresas fuera de España. Que el cambio exista y cuándo se produjo es un hecho a probar (contrato terminado, baja, nuevos clientes, alta de la nueva actividad…), no una fecha que se deduce de una factura suelta.

Antes de presentar, dejar en el expediente privado: autorización original y régimen, actividad que la sustentó, naturaleza y fecha acreditada del cambio, continuidad o cambio de negocio, requisitos aplicados, provincia y coordinación con la UGE. Si la fecha del cambio o la aplicación del criterio es dudosa, el agente para y lo eleva a la persona; no presenta por inferencia. Esperar también consume el plazo de tres meses. Con menos de un año de residencia, el criterio solo regula expresamente el paso a cuenta ajena: ver [casos especiales](special-cases.md).

Contraste adicional: [FAQ oficial de teletrabajo internacional](https://ciudadaniaexterior.inclusion.gob.es/documents/d/unidadgrandesempresas/nomadas-digitales-faqs-espanol). No asumir que la renovación de Ley 14/2013, la modificación al régimen general y la actividad real comparten requisitos.

## 2. Modificación art. 191.4: residencia que no habilitaba a trabajar

Al menos un año de residencia (por ejemplo, no lucrativa). Se acreditan los requisitos del art. 84: los que se exigen a los nacionales para abrir y ejercer la actividad, cualificación o experiencia y colegiación cuando proceda, suficiencia de la inversión e incidencia en el empleo (incluido el autoempleo), no estar en plazo de compromiso de no retorno, orden público y tasa.

- Formulario EX-26; tasa 790-052 epígrafe 2.5.2 y 790-062 epígrafe 3.3.1 (Hoja 55 bis); silencio negativo a los tres meses.
- No se puede trabajar ni darse de alta hasta la concesión (criterio 1/2025, apartado 1). Después, alta en el mes siguiente a la notificación; vigencia de un año.
- La inversión y el empleo pueden acreditarse, por ejemplo, con un informe de valoración de ATA, UPTA, CIAE, OPA o UATAE; la hoja admite otros medios de prueba.

## 3. Modificación art. 190.3: desde estancia por estudios

Requiere haber obtenido el título o certificado y no haber sido becado o subvencionado dentro de programas de cooperación al desarrollo o acción humanitaria. Se acreditan los requisitos del art. 84; la Hoja 58 pide también el certificado de antecedentes penales de los países de residencia de los cinco años anteriores a la entrada.

- Plazo (art. 190.6): dos meses antes o tres meses después de que termine la estancia o de obtener el título. Admitida a trámite, la estancia pasa a ser autorización provisional de residencia y trabajo (art. 190.7).
- Formulario EX-26, presentado personalmente o por Mercurio; tasa 790-052 epígrafe 2.5. La Hoja 58 añade un 790-062 epígrafe 3.2.1, que es de cuenta ajena: confirmarlo antes de pagar.
- Eficacia condicionada al alta en Seguridad Social; TIE en el mes siguiente a su entrada en vigor; vigencia de un año (art. 190.8–9).

## 4. Renovación de cuenta propia

Para quien ya tiene una autorización de cuenta propia, por ejemplo la inicial de un año.

- Plazo (art. 86.1): dos meses antes de caducar; hasta tres meses después se admite, pero puede abrirse un expediente sancionador ([LOEX art. 52.b](https://www.boe.es/buscar/act.php?id=BOE-A-2000-544)). Presentar en plazo prorroga la autorización hasta la resolución.
- Supuestos del art. 86.2 (los mismos de la ruta 1), informe de escolarización y, si falta algún requisito, informe de integración.
- EX-07 por Mercurio; tasa 790-052 epígrafe 2.2.3 y 790-062 epígrafe 3.3.2.
- Silencio **positivo** a los tres meses (art. 87.2; [LOEX DA 1.ª.2](https://www.boe.es/buscar/act.php?id=BOE-A-2000-544#daprimera)). Vigencia de cuatro años, con trabajo por cuenta ajena y propia en todo el territorio. TIE en el mes siguiente a la notificación.

## 5. Inicial para no residente

La [Hoja 14](https://www.inclusion.gob.es/web/migraciones/w/autorizacion-inicial-de-residencia-temporal-y-trabajo-por-cuenta-propia) describe la autorización para quien vive fuera de España. Revisa la demarcación consular actual antes de preparar el caso.

- La persona presenta EX-07 personalmente en la oficina consular de su lugar de residencia. La fuente enumera pasaporte, antecedentes penales de los últimos cinco años, licencias o declaración responsable, cualificación, homologación y colegiación, e inversión con su incidencia en el empleo. El informe de ATA, UPTA, CIAE, OPA o UATAE es un ejemplo de prueba de los dos últimos, no el único documento posible.
- Tasas: 790-052 epígrafe 2.1.3 y 790-062 epígrafe 3.3.1 si la autorización de trabajo dura seis meses o más. Resolución en tres meses; silencio negativo.
- Si se concede: un mes para pedir el visado personalmente (pasaporte con un año de vigencia mínima, antecedentes de cinco años y certificado médico, [art. 38](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a3-10)); un mes para recogerlo; entrada durante su vigencia de tres meses; alta en Seguridad Social en los tres meses siguientes a la entrada, que da eficacia a la autorización ([art. 85.7](https://www.boe.es/buscar/act.php?id=BOE-A-2024-24099#a8-7)); TIE en el mes siguiente al alta.
- No trasladar plazos, documentos ni tasas de las modificaciones sin comprobarlos.

## 6. Familiar

No usar un expediente principal como sustituto de la solicitud familiar. Determina primero la concesión original y su régimen jurídico, el criterio aplicable, la guía provincial, la legitimación, la oficina y el formulario actual; conserva autorización, firma y resguardo de cada persona. Para una persona adulta, el certificado de acceso o firma normalmente debe corresponder a quien presenta o a una representación acreditada ([Hoja 60](https://www.inclusion.gob.es/web/migraciones/w/60.-sujetos-legitimados)); para un menor, confirmar la representación legal.

EX-02 no se selecciona solo porque exista TIE. Puede ser correcto en una reagrupación o su renovación tras comparar la [Hoja 8](https://www.inclusion.gob.es/web/migraciones/w/autorizacion-de-residencia-temporal-por-reagrupacion-familiar) o la [Hoja 10](https://www.inclusion.gob.es/web/migraciones/w/renovacion-de-la-autorizacion-de-residencia-por-reagrupacion-familiar.) con el caso real. Vivienda, medios, padrón o tasas se deciden por la vía familiar realmente aplicable y su fuente actual. Los familiares con autorización de Ley 14/2013 ([art. 62.4](https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a62)) no tienen regla propia en el criterio 1/2025: su situación se decide aparte antes de presentar la modificación del titular.

## No es esta ruta

- Emprendedor con actividad innovadora o de especial interés económico e informe de ENISA: residencia para emprendedores de la Ley 14/2013 ([arts. 69–70](https://www.boe.es/buscar/act.php?id=BOE-A-2013-10074#a69)).
- Graduado que busca empleo o quiere emprender tras estudios superiores: [Hoja 20](https://www.inclusion.gob.es/web/migraciones/w/20.-autorizacion-de-residencia-para-busqueda-de-empleo-o-inicio-de-proyecto-empresarial) (DA 17.ª de la Ley 14/2013).
- Ciudadanos de la UE, el EEE, Suiza y sus familiares en régimen comunitario: no necesitan esta autorización.

## Operación electrónica

El [manual Mercurio](https://sede.administracionespublicas.gob.es/mercurio/manualUsuario.pdf) describe adjuntar, comprobar datos, firmar/registrar y fin de presentación. El preflight parte de `.pdf`, `.doc`, `.jpg`, `.tif`, `.gif`; reconfirma en la interfaz actual extensiones, nombre de archivo, tamaño, identificación admitida y provincia. El límite técnico almacenado por el script debe llevar fecha de confirmación; no es una regla jurídica del repositorio.

Los documentos extranjeros van con traducción jurada y legalización o apostilla salvo convenio que lo exima ([Hoja 61](https://www.inclusion.gob.es/web/migraciones/w/61.-legalizacion-y-traduccion-de-documentos-para-la-tramitacion-de-procedimientos-en-materia-de-extranjeria-e-inmigracion)). Tasas: [impresos 790](https://sede.administracionespublicas.gob.es/procedimientos/index/categoria/33). TIE: [documentación](https://sede.administracionespublicas.gob.es/procedimientos/index/categoria/34), [tasa 790-012](https://sede.policia.gob.es/Tasa790_012/) y [cita previa](https://icp.administracionelectronica.gob.es/icpplus/index.html).
