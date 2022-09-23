cd bin
py -m PyInstaller lightsheets.pyw --onefile --icon ../resources/icon.ico --clean --collect-binaries clr_loader
cd ..