"""Prepara la edición para compartir desde el expediente local revisado."""
import argparse, json, re, hashlib, html, shutil
from pathlib import Path

def preparar(origen, repo):
    out=repo/'docs/observatorio';out.mkdir(parents=True,exist_ok=True)
    d=json.loads((origen/'datos.json').read_text())
    # El expediente íntegro permanece local. No publicar notas privadas ni proveedores naturales.
    d['notas']={}
    txt=json.dumps(d,ensure_ascii=False)
    for c in d['investigacion']['contratos']:
        nombre=c['proveedor']
        if 'S.A.S.' not in nombre:
            txt=txt.replace(nombre,'Proveedor persona natural · identidad disponible en el registro oficial')
    d=json.loads(txt)
    fuentes={s['id']:s for s in d['fuentes']}
    for s in d['fuentes']:s.pop('local',None)
    d['publicacion']={'fecha':d['corte'],'edicion':d['version']+' · Consultas y veeduría','alcance':'Edición para compartir: análisis y fuentes públicas; originales, OCR bruto y respaldos permanecen localmente. Proveedores personas naturales anonimizados. Las notas son locales y no se sincronizan con GitHub.'}
    t=(origen/'plantilla.html').read_text()
    # En la web, las fuentes se consultan en su origen, no en copias locales ausentes.
    t=t.replace("KEY='montufar-analisis-andres-v1'","KEY='montufar-observatorio-web-v1'")
    t=t.replace('data.fuentes.filter(f=>localurl(f.local)).map','data.fuentes.map')
    t=t.replace('<a href="${esc(localurl(f.local))}" target="_blank" rel="noopener">Abrir copia archivada</a> · ','')
    t=t.replace('<div id="notice"','<div class="callout small noprint"><strong>Edición para compartir · 24-XI-2026</strong><p>Incluye los seis planes aportados, preguntas sobre áreas verdes y adoquinado, la tasa de residuos y el estado de búsqueda del informe de comisión sobre el PDOT. Las fuentes originales se abren en su sitio de publicación. Las notas y ediciones se guardan solo en este navegador: exportarlas no actualiza GitHub.</p><p><a href="datos.json" download>Descargar versión publicada de los datos</a> · <a href="https://github.com/marcoguiaecuador-design/politica-andres-2026">Repositorio e historial de revisiones</a></p></div><div id="notice"')
    t=re.sub(r'<p class="small muted space">Se archiva la copia local aportada del informe DPC-0001-2026.*?</p><p>.*?</p>', '<p class="small muted space">La copia íntegra aportada del informe DPC-0001-2026 y el OCR se conservan en el expediente local; no se redistribuyen en esta edición. La identificación se contrasta con LOTAIP. No se certifican aquí firma digital ni hallazgos completos.</p>',t,flags=re.S)
    t=t.replace('Conserve el HTML junto a sus carpetas: las copias archivadas son enlaces relativos. Guardar HTML actualizado integra datos y notas, pero no incorpora los PDF dentro del archivo. Las fuentes originales siguen enlazadas para cotejo.','Esta edición enlaza las fuentes públicas originales. Los PDF, respaldos y OCR bruto se conservan en el expediente local. Guardar HTML actualizado integra datos y notas, pero no publica una revisión en GitHub.')
    planes={'fabian_robles':'PF','javier_proano':'PJ','ruben_castillo':'PC','raul_lucero_actual':'PNL','gabriel_jacome':'PG'}
    for carpeta,sid in planes.items():
        prefix='candidatos/'+carpeta+'/'
        t=re.sub(r'<a href="'+re.escape(prefix)+r'fuentes/[^" ]+(?:ocr|texto)[^" ]*\.txt">.*?</a>',lambda m:'<a href="'+fuentes[sid]['url']+'" target="_blank" rel="noopener">Consultar plan original</a>',t)
    # Todo inventario enlaza al registro de esta publicación; los originales no se copian.
    t=re.sub(r'href="(?:candidatos/[^/]+/inventario.json|contratacion_cooperacion/inventario.json|veeduria/inventario_archivos.json)"','href="fuentes_publicacion.json"',t)
    t=t.replace('Ver inventario y huellas SHA-256','Ver registro de fuentes de publicación').replace('Inventario de descargas y SHA-256','Registro de fuentes de publicación')
    t=t.replace('Ver OCR bruto, con errores','Consultar plan original').replace('Leer transcripción OCR','Consultar plan original').replace('Leer OCR de apoyo','Consultar plan original')
    payload=json.dumps(d,ensure_ascii=False).replace('<','\\u003c')
    assert t.count('/*__DATA__*/')==1
    (out/'informe.html').write_text(t.replace('/*__DATA__*/',payload))
    (out/'datos.json').write_text(json.dumps(d,ensure_ascii=False,indent=2))
    # Documentos derivados expresamente revisados, sin datos de contacto o archivos originales.
    allow=['investigacion_adoquinado_2026-11-24/informe_adoquinado.html','investigacion_adoquinado_2026-11-24/resultado.json','investigacion_adoquinado_2026-11-24/precios_verificados.json','investigacion_adoquinado_2026-11-24/matriz_montufar_2019_2023.json','investigacion_adoquinado_2026-11-24/inventario.json','pdot_revision/solicitud_documental.txt','pdot_revision/registro_revision.json','preguntas_tecnicas/solicitud_aclaracion_residuos.txt','vialidad_rural/resultado.json','candidatos/gabriel_jacome/lectura_revisada.html','candidatos/gabriel_jacome/fuentes/lectura_operativa_revisada.txt','veeduria/solicitud_informacion.txt','veeduria/calculos_verificados.json','contratacion_cooperacion/matriz_evidencia.json','contratacion_cooperacion/solicitud_complementaria.txt']
    (out/'vialidad_rural').mkdir(exist_ok=True)
    shutil.copy2(origen/'vialidad_rural/extracto_tabla76.pdf',out/'vialidad_rural/extracto_tabla76.pdf')
    for rel in allow:
        p=out/rel;p.parent.mkdir(parents=True,exist_ok=True);content=(origen/rel).read_text()
        if rel.endswith('lectura_revisada.html'):
            content=content.replace('href="fuentes/plan_gabriel_jacome.pdf"','href="'+fuentes['PG']['url']+'"')
            content=re.sub(r' · <a href="fuentes/plan_gabriel_jacome_ocr.txt">[^<]*</a>','',content)
            content=content.replace('../../informe.html','../../informe.html')
        # Revisión de los derivados con los mismos criterios de anonimización.
        for c in json.loads((origen/'datos.json').read_text())['investigacion']['contratos']:
            if 'S.A.S.' not in c['proveedor']:content=content.replace(c['proveedor'],'Proveedor persona natural · consultar registro oficial')
        p.write_text(content)
    manifest={'fecha':d['corte'],'version':d['version'],'alcance':d['publicacion']['alcance'],'fuentes':d['fuentes']}
    (out/'fuentes_publicacion.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2))
    (repo/'docs/index.html').write_text('<!doctype html><html lang="es"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Observatorio de Montúfar</title><meta http-equiv="refresh" content="0;url=observatorio/informe.html"><p><a href="observatorio/informe.html">Abrir observatorio de Montúfar</a></p></html>')
    (repo/'docs/.nojekyll').touch()
    print('Preparados',sum(p.is_file() for p in out.rglob('*')),'archivos de publicación. No se copian PDF íntegros, OCR bruto ni respaldos; se publica el extracto vial revisado.')

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('expediente',type=Path);parser.add_argument('--repositorio',type=Path,default=Path(__file__).resolve().parents[1]);a=parser.parse_args();preparar(a.expediente,a.repositorio)
