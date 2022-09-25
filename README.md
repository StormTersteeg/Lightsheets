<p align="center">
  <img src="https://github.com/StormTersteeg/Lightsheets/blob/main/resources/icon.png" width="100" style="image-rendering:pixelated">
</p>
<h1 align="center">Lightsheets</h1>

A desktop widget engine to easily add HTML/JS widgets to your desktop.
Programmed with [Glide](https://github.com/StormTersteeg/Python-Glide-Framework).<br><br>
![image](https://user-images.githubusercontent.com/42808385/191917214-87106d42-603e-4321-a73b-20df477a0e65.png)

Add new widgets by adding .html files to the `apps` directory.
![image](https://user-images.githubusercontent.com/42808385/192152106-f1cbf78c-8866-4b54-97d6-510abfeebc1d.png)

Press `shift_right` to toggle widget visibility.

<br><br>

# Resources
Lightsheets is precompiled with resources like Bootstrap, these resources can be used in widgets.
| Resource            | Type |  |
|----------------------------|--------|-----------------------------------------------------------------|
| Bootstrap 4.1.1            | CSS/JS | https://getbootstrap.com/docs/4.1/getting-started/introduction/ |
| JQuery 3.5.1               | JS     | https://jquery.com/                                             |
| Daemonite's Material 4.1.1 | CSS    | https://daemonite.github.io/material/                           |
| Material Icons             | Font   | https://fonts.google.com/icons?selected=Material+Icons          |
| Popper 1.14.3              | JS     | https://popper.js.org/                                          |
| Roboto                     | Font   | https://fonts.google.com/specimen/Roboto                        |

<br><br>

# Examples
Lightsheets comes with 4 example widgets that can be found [here](https://github.com/StormTersteeg/Lightsheets/tree/main/resources/apps).

<br><br>

# Javascript API
You can call several functions from the default API to activate scripts.

### openUrl(url)
To open a webpage url in your default browser.<br>
`pywebview.api.openUrl("https://dontdalon.com")`

### startApp(path)
To open/start a local file.<br>
`pywebview.api.startApp("C:\Users\storm\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Discord Inc\Discord.lnk")`

### doCommand(command)
`pywebview.api.doCommand("Rundll32.exe user32.dll,LockWorkStation")`

### openChild(url)
To open a webpage url in a new lightsheet window.<br>
`pywebview.api.openChild("https://www.google.nl/maps")`

### show()
To show all widgets.<br>
`pywebview.api.show()`

### hide()
To hide all widgets.<br>
`pywebview.api.hide()`

### minimize()
To minimize all widgets.<br>
``pywebview.api.minimize()``

### close()
To turn lightsheets off.<br>
`pywebview.api.close()`

### reload()
To reload lightsheets. Useful to quickly restart lightsheets after adding new widgets.<br>
`pywebview.api.reload()`
