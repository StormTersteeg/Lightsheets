import webview, os, sys
from pynput.keyboard import Key, Listener, Controller
from os import listdir
from os.path import isfile, join
import webbrowser

class Api:
  def __init__(self):
    self.windows = []
    self.visible = True

  def openUrl(self, url):
    self.hide()
    webbrowser.open((url if ("http" in url) else "".join(["http://", url])).replace(' ', '%20'))

  def startApp(self, path):
    self.hide()
    os.startfile(path)

  def doCommand(self, command):
    self.hide()
    os.system(command)

  def openChild(self, url):
    self.hide()
    webview.create_window(url, url)

  def show(self):
    for window in self.windows:
      window.show()

  def hide(self):
    for window in self.windows:
      window.hide()

  def minimize(self):
    for window in self.windows:
      window.minimize()

  def close(self):
    for window in self.windows:
      window.destroy()

  def reload(self):
    os.startfile(sys.argv[0])
    self.close()

def on_press(key):
  try:
    if key==Key.shift_r:
      if api.visible:
        api.hide()
      else:
        api.show()
      api.visible = not api.visible
  except: pass

#!FLAG-HTML
apps = [f for f in listdir('apps') if isfile(join('apps', f))]

if __name__ == '__main__':
  api = Api()
  keyboard = Controller()

  margin = 30
  i = 0
  x = y = margin
  for app in apps:
    pack = default_html + "\n" + open(f"apps/{app}", "r").read()
    
    window = webview.create_window("", html=pack, js_api=api, width={settings.app_proportions[0]}, height={settings.app_proportions[1]}, confirm_close={settings.app_confirm_close}, frameless={settings.app_frameless}, fullscreen={settings.app_fullscreen}, resizable={settings.app_resizable}, on_top=True, x=x, y=y)

    api.windows.append(window)

    x += 480 + margin
    i += 1
    if i%3==0:
      x = margin
      y += 240 + margin

  with Listener(on_press=on_press) as listener:
    webview.start(gui="{settings.app_web_engine}", debug={settings.app_allow_inspect})
    listener.join()