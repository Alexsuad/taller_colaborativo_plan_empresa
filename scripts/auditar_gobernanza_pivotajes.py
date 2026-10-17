import os
import re
import sys

def auditar():
    print("=== AUDITORÍA DE GOBERNANZA Y PIVOTAJES ===")
    
    # 1. Existencia de archivos
    notas_path = "docs_fuentes/drive_taller/00_notas_aclaratorias_vigentes.md"
    pivotajes_path = "docs_control/05_registro_pivotajes_y_cambios_relevantes.md"
    
    ok = True
    
    if not os.path.exists(notas_path):
        print(f"[FAIL] No existe el archivo de notas: {notas_path}")
        ok = False
    else:
        print(f"[PASS] Archivo de notas detectado: {notas_path}")
        
    if not os.path.exists(pivotajes_path):
        print(f"[FAIL] No existe el archivo de pivotajes: {pivotajes_path}")
        ok = False
    else:
        print(f"[PASS] Archivo de pivotajes detectado: {pivotajes_path}")
        
    if not ok:
        sys.exit(1)
        
    # Leer contenidos
    with open(notas_path, "r", encoding="utf-8") as f:
        notas_content = f.read()
        
    with open(pivotajes_path, "r", encoding="utf-8") as f:
        pivotajes_content = f.read()
        
    # 2. Validar campos mínimos y estados en Notas
    # Extraer bloques de notas
    nota_blocks = re.findall(r"### NOTA-\d+:.*?(?=### NOTA-\d+:|$)", notas_content, re.DOTALL)
    if not nota_blocks:
        print("[FAIL] No se encontraron bloques de notas con formato '### NOTA-XXX:'")
        ok = False
    else:
        print(f"[PASS] Se encontraron {len(nota_blocks)} notas aclaratorias.")
        for block in nota_blocks:
            # Buscar campos
            id_match = re.search(r"-\s*\*\*ID:\*\*\s*(NOTA-\d+)", block)
            fecha_match = re.search(r"-\s*\*\*Fecha:\*\*\s*\d{4}-\d{2}-\d{2}", block)
            tema_match = re.search(r"-\s*\*\*Tema:\*\*\s*\w+", block)
            aclaracion_match = re.search(r"-\s*\*\*Aclaración Vigente:\*\*", block)
            fuentes_match = re.search(r"-\s*\*\*Fuentes o Documentos Afectados:\*\*", block)
            uso_match = re.search(r"-\s*\*\*Uso Permitido:\*\*", block)
            sustituye_match = re.search(r"-\s*\*\*Información que Sustituye:\*\*", block)
            estado_match = re.search(r"-\s*\*\*Estado:\*\*\s*(\w+)", block)
            
            nota_id = id_match.group(1) if id_match else "Desconocida"
            
            campos = {
                "ID": id_match, "Fecha": fecha_match, "Tema": tema_match, 
                "Aclaración Vigente": aclaracion_match, "Fuentes Afectadas": fuentes_match,
                "Uso Permitido": uso_match, "Información que Sustituye": sustituye_match, 
                "Estado": estado_match
            }
            
            missing = [k for k, v in campos.items() if not v]
            if missing:
                print(f"[FAIL] Nota {nota_id} carece de campos: {', '.join(missing)}")
                ok = False
            else:
                # Validar estado
                estado = estado_match.group(1)
                if estado not in ["vigente", "sustituida"]:
                    print(f"[FAIL] Nota {nota_id} tiene un estado no permitido: '{estado}'")
                    ok = False
                    
    # 3. Validar plantilla y estados de pivotajes
    # Buscar ejemplos o bloques de pivotajes
    piv_blocks = re.findall(r"### PIV-.*?(?=### PIV-|$)", pivotajes_content, re.DOTALL)
    if not piv_blocks:
        print("[FAIL] No se encontraron bloques de pivotajes con formato '### PIV-XXX:'")
        ok = False
    else:
        print(f"[PASS] Se encontraron {len(piv_blocks)} bloques de pivotajes (incluyendo ejemplos).")
        for block in piv_blocks:
            id_match = re.search(r"-\s*\*\*ID:\*\*\s*(PIV-\w+)", block)
            estado_match = re.search(r"-\s*\*\*Estado:\*\*\s*(\w+)", block)
            piv_id = id_match.group(1) if id_match else "Desconocido"
            
            campos_piv = {
                "ID": id_match,
                "Fecha": re.search(r"-\s*\*\*Fecha:\*\*", block),
                "Estado": estado_match,
                "Cambio": re.search(r"-\s*\*\*Cambio:\*\*", block),
                "Motivo": re.search(r"-\s*\*\*Motivo:\*\*", block),
                "Validado por": re.search(r"-\s*\*\*Validado por:\*\*", block),
                "Decisión anterior sustituida": re.search(r"-\s*\*\*Decisión anterior sustituida:\*\*", block),
                "Áreas afectadas": re.search(r"-\s*\*\*Áreas afectadas:\*\*", block),
                "Documentos potencialmente afectados": re.search(r"-\s*\*\*Documentos potencialmente afectados:\*\*", block),
                "Impacto Legal": re.search(r"-\s*\*\*Impacto Legal:\*\*", block),
                "Impacto Financiero": re.search(r"-\s*\*\*Impacto Financiero:\*\*", block),
                "Impacto Operativo": re.search(r"-\s*\*\*Impacto Operativo:\*\*", block),
                "Impacto Comercial": re.search(r"-\s*\*\*Impacto Comercial:\*\*", block),
                "Acciones requeridas": re.search(r"-\s*\*\*Acciones requeridas:\*\*", block),
                "Verificación final": re.search(r"-\s*\*\*Verificación final:\*\*", block),
            }
            
            missing_piv = [k for k, v in campos_piv.items() if not v]
            if missing_piv:
                print(f"[FAIL] Pivotaje {piv_id} carece de campos: {', '.join(missing_piv)}")
                ok = False
            else:
                estado = estado_match.group(1)
                if estado not in ["propuesto", "aprobado", "descartado", "sustituido"]:
                    print(f"[FAIL] Pivotaje {piv_id} tiene un estado no permitido: '{estado}'")
                    ok = False

    # 4. Validar referencias en AGENTS.md y workflows
    agents_path = "AGENTS.md"
    workflow_path = ".agents/workflows/resolucion-preguntas-por-capitulo.md"
    
    for doc_path in [agents_path, workflow_path]:
        if not os.path.exists(doc_path):
            print(f"[FAIL] No existe el documento de gobernanza: {doc_path}")
            ok = False
            continue
            
        with open(doc_path, "r", encoding="utf-8") as f:
            doc_content = f.read()
            
        if "00_notas_aclaratorias_vigentes.md" not in doc_content:
            print(f"[FAIL] {doc_path} no referencia '00_notas_aclaratorias_vigentes.md'")
            ok = False
        else:
            print(f"[PASS] {doc_path} referencia las notas aclaratorias correctamente.")
            
        if "05_registro_pivotajes_y_cambios_relevantes.md" not in doc_content:
            print(f"[FAIL] {doc_path} no referencia '05_registro_pivotajes_y_cambios_relevantes.md'")
            ok = False
        else:
            print(f"[PASS] {doc_path} referencia el registro de pivotajes correctamente.")

    # 5. Ausencia de contradicciones básicas en notas
    if "Alexander Suárez" not in notas_content or "Juan Felipe Suárez" not in notas_content:
        print("[FAIL] Las notas no listan al equipo promotor vigente.")
        ok = False
    else:
        print("[PASS] Equipo promotor vigente listado correctamente en las notas.")
        
    if "Claudia Bautista" not in notas_content or "no forma parte" not in notas_content:
        print("[FAIL] Las notas no declaran la exclusión de Claudia Bautista.")
        ok = False
    else:
        print("[PASS] Exclusión de Claudia Bautista correctamente declarada en las notas.")
        
    if "no está definida" not in notas_content and "relación jurídica" not in notas_content:
        print("[FAIL] Las notas no declaran que la relación jurídica está pendiente o no definida.")
        ok = False
    else:
        print("[PASS] Relación jurídica pendiente correctamente declarada en las notas.")

    if ok:
        print("\n[VERDICT] PASS: Todo el sistema de gobernanza y pivotajes es conforme.")
        sys.exit(0)
    else:
        print("\n[VERDICT] FAIL: Se detectaron fallas de gobernanza.")
        sys.exit(1)

if __name__ == "__main__":
    auditar()
