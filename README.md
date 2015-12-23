# Remover.py
Remove completed uTorrent downloads automatically.

Follow steps below:
Enable Web UI - Preferences > Advanced > Web UI > check Enable Web UI.
Disable Web Token Auth - Preferences > Advanced > webui.token.auth *false.
Set authentication to use: admin / admin.
Run program with pythonw.exe to hide console window. (example: c:\program files\python\pythonw.exe)
Set program to run - Advanced > Run Program > Run this program when a torrent finishes. (example: c:\pythonw.exe remover.py)

Tested and works on uTorrentPro 3.4.5 (build 41372).
