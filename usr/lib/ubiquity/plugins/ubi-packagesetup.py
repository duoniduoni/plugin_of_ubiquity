import os
import re
import debconf
from ubiquity import misc, plugin, validation

NAME = 'packagesetup'
WEIGHT = 12
AFTER = 'welcome'


class PageBase(plugin.PluginUI):
    def __init__(self):
        pass


class PageGtk(PageBase):
    plugin_title = 'ubiquity/text/packagesetup_heading_label'

    def __init__(self, controller, *args, **kwargs):
        pass


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

        return questions, command

    def run(self, priority, question):
        return plugin.Plugin.run(self, priority, question)

    def ok_handler(self):
        pass

    
class Install(plugin.InstallPlugin):
    def prepare(self, unfiltered=False):
        command = [
                'sh', '-c',
                '/usr/lib/ubiquity/packagesetup/package-setup-apply /target',
            ]
        return command, [], []       