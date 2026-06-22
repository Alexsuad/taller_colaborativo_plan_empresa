# ADVERTENCIA DE MIGRACIÓN
# Script adaptado para taller_colaborativo_plan_empresa.
# Estado: ADAPTADO - Distingue PASS, PENDIENTE y FAIL de forma determinista.

import os
import re
import sys

def audit_plan():
    respuestas_dir = 'respuestas_plan_empresa/'
    gates_file = 'docs_control/03_gates_documentales.md'
    build_file = '_build/plan_empresa_taller_colaborativo_completo.md'
    entrega_anexos_dir = '_build/entrega/anexos/'

    if not os.path.exists(respuestas_dir):
        print(f"FAIL: Directorio {respuestas_dir} no existe.")
        return "FAIL"

    has_fail = False
    has_pending = False
    pending_files = []
    
    # Patrones que indican placeholders legítimos de trabajo (PENDIENTE)
    placeholder_patterns = [
        r'Pendiente de completar', 
        r'\[PENDIENTE\]', 
        r'\[CIFRA\]', 
        r'\[NÚMERO\]',
        r'Estado: pendiente de respuesta\.',
        r'_Pendiente\._',
        r'pendiente de respuesta',
        r'Vacíos / decisiones pendientes'
    ]

    # Patrones que indican datos de prueba o contaminación (FAIL directo)
    fail_patterns = [
        r'TEST_01',
        r'TEST_02',
        r'test_externo'
    ]

    files = [f for f in os.listdir(respuestas_dir) if f.endswith('.md')]
    
    if len(files) == 0:
        print("FAIL: No hay archivos en respuestas_plan_empresa/")
        return "FAIL"

    # 1. Check for patterns in answers files
    for f in files:
        filepath = os.path.join(respuestas_dir, f)
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            
            # Check for direct fails first
            for pat in fail_patterns:
                if re.search(pat, content, re.IGNORECASE):
                    print(f"FAIL: Archivo {f} contiene patrón prohibido: {pat}")
                    has_fail = True
            
            # Check for placeholders (pending work)
            for pat in placeholder_patterns:
                if re.search(pat, content, re.IGNORECASE):
                    pending_files.append(f)
                    has_pending = True
                    break # Stop checking this file once we know it is pending
    
    pending_files = list(set(pending_files))

    # 2. Check gates for false advances
    if os.path.exists(gates_file):
        with open(gates_file, 'r', encoding='utf-8') as gf:
            gates_content = gf.read()
        
        blocks = re.split(r'## Gate', gates_content)[1:]
        for block in blocks:
            lines = block.strip().split('\n')
            gate_name = lines[0].strip()
            
            estado = None
            files_in_gate = []
            
            for line in lines:
                if line.startswith('**Estado:**'):
                    estado = line.replace('**Estado:**', '').strip()
                # Extrae cualquier archivo listado en backticks de respuestas_plan_empresa
                match = re.search(r'`respuestas_plan_empresa/([^`]+)`', line)
                if match:
                    files_in_gate.append(match.group(1))
            
            if estado and 'Completado' in estado:
                for f in files_in_gate:
                    if f in pending_files:
                        print(f"FAIL: Avance falso detectado en Gate {gate_name}. El archivo {f} está marcado como Completado pero contiene marcadores pendientes.")
                        has_fail = True

    # 3. Check for premature build files if we are not clean
    if os.path.exists(build_file) and has_pending:
        print(f"FAIL: El archivo {build_file} existe pero hay apartados pendientes ({len(pending_files)} archivos con marcadores).")
        has_fail = True

    # 4. Check for test files in entrega
    if os.path.exists(entrega_anexos_dir):
        test_files = [f for f in os.listdir(entrega_anexos_dir) if 'test' in f.lower() or f == 'test_externo.txt']
        if test_files:
            print(f"FAIL: Archivos de prueba detectados en salida final: {test_files}")
            has_fail = True

    # Determinar resultado final
    if has_fail:
        print("VERDICT: FAIL")
        return "FAIL"
    elif has_pending:
        print(f"INFO: Hay {len(pending_files)} archivos con placeholders pendientes de completar: {', '.join(pending_files)}")
        print("VERDICT: PENDIENTE")
        return "PENDIENTE"
    
    print("PASS: El plan de empresa está completo, limpio de pruebas y no hay inconsistencias en los gates.")
    print("VERDICT: PASS")
    return "PASS"

if __name__ == '__main__':
    verdict = audit_plan()
    if verdict == "FAIL":
        sys.exit(1)
    elif verdict == "PENDIENTE":
        sys.exit(0) # Salida limpia para estado pendiente de trabajo
    else:
        sys.exit(0)
