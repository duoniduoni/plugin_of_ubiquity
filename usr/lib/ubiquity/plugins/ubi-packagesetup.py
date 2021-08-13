import os
import re
import debconf
from ubiquity import misc, plugin, validation

NAME = 'packagesetup'
WEIGHT = 13
AFTER = 'language'


class PageBase(plugin.PluginUI):
    def __init__(self):
        plugin.PluginUI.__init__(self)

    def get_deb_path(self):
        """Set the user's full name."""
        raise NotImplementedError('get_deb_path')


class PageGtk(PageBase):
    plugin_title = 'ubiquity/text/packagesetup_heading_label'

    def __init__(self, controller, *args, **kwargs):
        from gi.repository import Gio, Gtk

        self.controller = controller

        builder = Gtk.Builder()
        self.controller.add_builder(builder)
        builder.add_from_file(os.path.join(
            os.environ['UBIQUITY_GLADE'], 'stepPackageSetup.ui'))
        builder.connect_signals(self)
        self.page = builder.get_object('stepPackageSetup')
        self.deb_path = builder.get_object('entry_packagePath')

        self.plugin_widgets = self.page

    def get_deb_path(self):
        return self.deb_path.get_text()

    def on_btn_packagePath_clicked(self, button):
        from gi.repository import Gio, Gtk
        dialog = Gtk.FileChooserDialog(
            title="Please choose a folder",
            #parent=self,
            action=Gtk.FileChooserAction.SELECT_FOLDER,
        )
        dialog.add_buttons(
            Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL, "Select", Gtk.ResponseType.OK
        )
        dialog.set_default_size(800, 400)

        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Select clicked")
            print("Folder selected: " + dialog.get_filename())
            self.deb_path.set_text(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")

        dialog.destroy()



class PageKde(PageBase):
    plugin_breadcrumb = 'ubiquity/text/breadcrumb_packagesetup'

    def __init__(self, controller, *args, **kwargs):
        pass


class Page(plugin.Plugin):
    def prepare(self, unfiltered=False):
        questions = ['^package-setup/package-path',]
        command = [
                'sh', '-c',
                '/usr/lib/ubiquity/packagesetup/package-setup-ask /target',
            ]

        self.preseed('package-setup/package-path', '/tmp/')

        return command, questions

    def run(self, priority, question):
        return plugin.Plugin.run(self, priority, question)

    def ok_handler(self):
        deb_path = self.ui.get_deb_path()
        self.preseed('package-setup/package-path', deb_path)

        plugin.Plugin.ok_handler(self)

    
class Install(plugin.InstallPlugin):
    def prepare(self, unfiltered=False):
        command = [
                'sh', '-c',
                '/usr/lib/ubiquity/packagesetup/package-setup-apply /target',
            ]
        return command, [], []    

    def install(self, target, progress, *args, **kwargs):
        return plugin.InstallPlugin.install(
            self, target, progress, *args, **kwargs)   