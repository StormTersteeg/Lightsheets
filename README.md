<img align="left" width="80" height="80" src="https://github.com/StormTersteeg/Lightsheets/blob/main/resources/icon.png" alt="icon">

# Lightsheets
Lightsheets, a desktop widget engine to easily add HTML/JS widgets to your desktop.
Programmed with [Glide](https://github.com/StormTersteeg/Python-Glide-Framework).<br><br>
![image](https://user-images.githubusercontent.com/42808385/191917214-87106d42-603e-4321-a73b-20df477a0e65.png)


# Summary
Add new widgets by adding .html files to the `apps` directory.
Press `shift_right` to toggle widget visibility.

# Javascript API
You can call several functions from the default API to activate scripts.

### openUrl(url)
To open a webpage url in your default browser.
`pywebview.api.openUrl("https://dontdalon.com")`

### startApp(path)
To open/start a local file.
`pywebview.api.startApp("C:\Users\storm\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")`

### doCommand(command)
`pywebview.api.doCommand("Rundll32.exe user32.dll,LockWorkStation")`

### openChild(url)
To open a webpage url in a new lightsheet window.
`pywebview.api.openChild("https://www.google.nl/maps")`

### show()
To show all widgets.
`pywebview.api.show()`

### hide()
To hide all widgets.
`pywebview.api.hide()`

### minimize()
To minimize all widgets.
``pywebview.api.minimize()``

### close()
To turn lightsheets off.
`pywebview.api.close()`

### reload()
To reload lightsheets. Useful to quickly restart lightsheets after adding new widgets.
`pywebview.api.reload()`
