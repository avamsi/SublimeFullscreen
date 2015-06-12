import sublime, sublime_plugin

auto_toggle = False

class CustomFullScreenCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command('toggle_full_screen')
        self.window.run_command('toggle_menu')

class QuitCommand(sublime_plugin.WindowCommand):
    def run(self):
        if auto_toggle:
            self.window.run_command('toggle_full_screen')
            self.window.run_command('toggle_menu')
        self.window.run_command('close_window')


def plugin_loaded():
    global auto_toggle
    settings = sublime.load_settings('Fullscreen.sublime-settings')
    auto_toggle = settings.get('fullscreen_on_start', False)
    if auto_toggle:
        window = sublime.active_window()
        window.run_command('toggle_full_screen')
        window.run_command('toggle_menu')
