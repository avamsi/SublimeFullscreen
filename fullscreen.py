import sublime, sublime_plugin

class CustomFullScreenCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('toggle_full_screen')
        self.window.run_command('toggle_menu')

class QuitCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('toggle_full_screen')
        self.window.run_command('toggle_menu')
        self.window.run_command('close_window')


def plugin_loaded():
    settings = sublime.load_settings('Fullscreen.sublime-settings')
    if settings.get('fullscreen_on_start', False):
        window = sublime.active_window()
        window.run_command('toggle_full_screen')
        window.run_command('toggle_menu')
