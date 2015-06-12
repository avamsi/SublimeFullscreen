import sublime, sublime_plugin

fullscreen = False

class CustomFullScreenCommand(sublime_plugin.WindowCommand):
    def run(self):
        global fullscreen
        self.window.run_command('toggle_full_screen')
        self.window.run_command('toggle_menu')
        fullscreen = not fullscreen

class QuitCommand(sublime_plugin.WindowCommand):
    def run(self):
        if fullscreen:
            self.window.run_command('toggle_full_screen')
            self.window.run_command('toggle_menu')
        self.window.run_command('close_window')


def plugin_loaded():
    global fullscreen
    settings = sublime.load_settings('Fullscreen.sublime-settings')
    if settings.get('fullscreen_on_start', False):
        window = sublime.active_window()
        window.run_command('toggle_full_screen')
        window.run_command('toggle_menu')
        fullscreen = not fullscreen
