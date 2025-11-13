# -*- mode: python ; coding: utf-8 -*-

import sys
from pathlib import Path

block_cipher = None

# Collect all files from strix/prompts directory
datas = []
datas.append(('strix/prompts', 'strix/prompts'))

# Collect litellm data files (JSON tokenizers and cost data)
import site
site_packages = Path(site.getsitepackages()[0])
litellm_dir = site_packages / 'litellm'
if litellm_dir.exists():
    for json_file in litellm_dir.rglob('*.json'):
        rel_path = json_file.relative_to(site_packages)
        dest_dir = str(rel_path.parent)
        datas.append((str(json_file), dest_dir))

# Hidden imports for packages that PyInstaller might miss
hiddenimports = [
    'litellm',
    'docker',
    'playwright',
    'textual',
    'rich',
    'aiohttp',
    'pydantic',
    'fastapi',
    'starlette',
    'tiktoken',
    'tiktoken_ext',
    'tiktoken_ext.openai_public',
    'openai',
    'anthropic',
    # LiteLLM providers
    'litellm.llms',
    'litellm.llms.openai',
    'litellm.llms.anthropic',
    'litellm.llms.azure',
    'litellm.llms.cohere',
    # Strix modules
    'strix',
    'strix.interface',
    'strix.interface.main',
    'strix.interface.cli',
    'strix.interface.tui',
    'strix.agents',
    'strix.tools',
    'strix.runtime',
    'strix.llm',
    'strix.telemetry',
]

a = Analysis(
    ['strix/interface/main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='strix-agent',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
