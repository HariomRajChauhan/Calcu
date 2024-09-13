# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['test1.py'],  # List of files to analyze
    pathex=['.'],  # Paths to search for imports
    binaries=[],  # No additional binaries are needed
    datas=[('assets', 'assets')],  # Include the entire assets folder
    hiddenimports=[],  # Specify any hidden imports not automatically detected
    hookspath=[],  # Paths to any hooks if necessary
    runtime_hooks=[],  # Runtime hooks, if any
    excludes=[],  # Exclude specific modules if necessary
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,  # Set to False to pack files into a single archive
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Calcu',  # Name of the output executable
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,  # Enable UPX compression
    console=False,  # No console window (for GUI application)
    icon='assets/icon.ico'  # Use the icon from the assets folder
)
