# -*- mode: python ; coding: utf-8 -*-
import os
import sys
import streamlit
import pdf2docx
from PyInstaller.utils.hooks import copy_metadata, collect_all, get_package_paths

hiddenimports = []
datas = [
    ("app.py", "."),      # O seu script Streamlit do conversor Word
    ("run_app.py", "."),  # O seu script de arranque universal
]

# 🔥 Incluir fisicamente as pastas do Streamlit e do pdf2docx
streamlit_dir = os.path.dirname(streamlit.__file__)
pdf2docx_dir = os.path.dirname(pdf2docx.__file__)

# Descobrir dinamicamente as pastas do pymupdf (fitz) e docx sem fazer import direto no topo
import importlib
fitz_dir = os.path.dirname(importlib.import_module("pymupdf").__file__)
docx_dir = os.path.dirname(importlib.import_module("docx").__file__)

datas.append((streamlit_dir, "streamlit"))
datas.append((pdf2docx_dir, "pdf2docx"))
datas.append((fitz_dir, "fitz"))  # Mapeia para "fitz" porque o pdf2docx procura por este nome
datas.append((docx_dir, "docx"))

# 🔥 Tentar extrair caminhos adicionais do Streamlit
try:
    streamlit_paths = get_package_paths("streamlit")
    if streamlit_paths and isinstance(streamlit_paths, tuple):
        for path in streamlit_paths:
            if path and isinstance(path, str):
                datas.append((path, "streamlit"))
    elif streamlit_paths and isinstance(streamlit_paths, str):
        datas.append((streamlit_paths, "streamlit"))
except Exception:
    pass

# Pacotes necessários para a conversão de PDF para Word e interface
packages_to_collect = ["streamlit", "pdf2docx", "pymupdf", "docx", "cv2", "jinja2", "requests", "markupsafe"]

for pkg in packages_to_collect:
    try:
        hi, d, b = collect_all(pkg)
        
        for item in hi:
            if isinstance(item, str) and not item.endswith('.py') and '\\' not in item and '/' not in item:
                hiddenimports.append(item)
                
        datas.extend(d)
        datas.extend(copy_metadata(pkg))
    except Exception:
        pass

# Submódulos ocultos do Streamlit e dependências gráficas internas
hiddenimports.extend([
    "streamlit.web",
    "streamlit.web.cli",
    "streamlit.runtime",
    "streamlit.runtime.scriptrunner",
    "streamlit.runtime.runtime",
    "streamlit.config",
    "jinja2.meta",
    "pymupdf",          # <-- ADICIONE ESTA LINHA
    "pymupdf.mupdf",    # <-- ADICIONE ESTA LINHA
    "fitz",
    "cv2",  
])

# Limpar duplicados
hiddenimports = list(set([str(h) for h in hiddenimports if h]))

a = Analysis(
    ["run_app.py"],  
    pathex=["."],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)

pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name="ConvertPDFWordApp",
    debug=False,
    strip=False,
    upx=True,
    console=True,  # Mantido True para monitorizar o progresso da conversão
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="ConvertPDFWordApp",
)