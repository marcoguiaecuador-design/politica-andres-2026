# Publicación y mantenimiento

## Edición revisada del 23-XI-2026

La publicación del observatorio fue solicitada expresamente por el propietario del proyecto en este repositorio. Su configuración actual es pública. Las referencias antiguas a un repositorio estrictamente privado describían el estado inicial, no el acceso actual.

Se publica una edición acotada: seis planes analizados, normativa y explicaciones, síntesis de gestión y contratación pública y sus fuentes. Se conservan los nombres de candidatos y autoridades necesarios para identificar los planes públicos. Los proveedores personas naturales se identifican por el proceso contractual, con su nombre sustituido en esta edición; el registro oficial sigue enlazado. Se mantienen los resultados agregados del presupuesto público necesarios para el control ciudadano, sin subir cédulas originales, bases o archivos financieros personales.

No se suben PDF originales, respaldos, OCR bruto, encuestas, bases de contactos, credenciales ni notas privadas. El expediente local permanece íntegro. Los documentos originales se consultan en las fuentes enlazadas; algunos enlaces pueden depender de la disponibilidad y permisos del sitio de origen.

Los archivos derivados incluidos son la lectura revisada de Gabriel Jácome, dos borradores vacíos de solicitud pública, el cálculo agregado verificado y la matriz de evidencia revisada. Ningún borrador se ha enviado a terceros.

## Actualizar

1. Modificar y contrastar el expediente local, conservando su respaldo y referencias.
2. En una copia actualizada del repositorio, ejecutar:

   ```bash
   python3 scripts/preparar_observatorio.py '/ruta/al/observatorio_municipal'
   ```

3. Revisar el diff y la edición resultante. Comprobar que no se incorporaron notas privadas, identificadores o fuentes que requieran permisos distintos. Actualizar la fecha del script y de los avisos si corresponde.
4. Guardar los cambios con un commit o PR y subirlos a `main`. GitHub Pages publica `/docs` en la misma dirección; comprobar la ejecución y el resultado.
5. Quienes tengan datos guardados en su navegador deben exportar sus notas antes de importar el nuevo `datos.json`; esta importación sustituye su copia de trabajo. La página no sincroniza cambios entre usuarios.

La publicación inicial conserva versión 1.10 y la corrección del Eje 1, sin una nueva revisión sustantiva de los hallazgos ni de la vigencia jurídica. Las cantidades de fichas no representan calidad o cumplimiento.

## Revisión 24-XI-2026 · versión 1.11

Se incorpora una cuarta categoría de Preguntas técnicas para debates, con PT01 sobre áreas verdes. Se conservan los seis análisis y la veeduría. Las nuevas fuentes externas se enlazan en su origen: el anexo ministerial es una copia externa cotejada y su alcance se identifica expresamente. El catastro institucional 2026 y un expediente de EPMMOP sirven para contraste, sin certificación exhaustiva de vigencia. Se preservan notas al migrar y se añade un ejemplo ficticio de m²/hab; no se publica un déficit real de Montúfar.


## Revisión 24-XI-2026 · versión 1.12

Se incorporan resultados y matriz de la investigación de adoquinado (4 rubros asociados a contratos y 43 procesos históricos), junto con enlaces a registros oficiales. El rango no es tarifa ni promedio nacional y no se certifica un total de km 2019–2023. Los JSON originales de SERCOP permanecen archivados localmente; sus huellas se consultan en el inventario publicado.

La ordenanza de tasa de residuos de Montúfar está publicada en RO EE 969 de 19-I-2026. Se incluye texto para lectura y tabla explicada, diferenciando valores anuales publicados de los porcentajes del SBU. No se resuelve de oficio su discrepancia ni se certifica el valor liquidado por Rentas. No se ha localizado reforma posterior en esta búsqueda, sin afirmar exhaustividad.

La revisión del PDOT distingue el informe solicitado de comisión, todavía no obtenido, de los reportes SIGAD y del antecedente SOT 2022–2023. No se atribuye una deficiencia al documento faltante. Se publica una solicitud documental preparada, sin envío.

Pruebas: navegación, tablas de precios y procesos, búsqueda, lector de ordenanza, notas, migración desde 1.11, conservación de los seis planes y vista móvil.

PT05: longitud de la red vial provincial inventariada en Montúfar, 386,68 km, base 2024. Se incorpora un extracto visual de la tabla oficial (p. impresa 216 / PDF 212), enlazado al documento provincial íntegro. No representa todos los caminos eventualmente no inventariados ni kilómetros construidos por una gestión.
