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
