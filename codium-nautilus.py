# VSCodium Nautilus Extension
#
# Place me in ~/.local/share/nautilus-python/extensions/,
# ensure you have python-nautilus package, restart Nautilus, and enjoy :)
#
# This script was written by cra0zy and is released to the public domain
# Adaptation pour le SEDOO (source: https://github.com/harry-cpp/code-nautilus)

from gi import require_version
require_version('Gtk', '3.0')
require_version('Nautilus', '3.0')
from gi.repository import Nautilus, GObject
from subprocess import call
import os

# path to vscodium
VSCODIUM = 'codium'

# what name do you want to see in the context menu?
VSCODIUMNAME = 'Codium'

# always create new window?
NEWWINDOW = False


class VSCodiumExtension(GObject.GObject, Nautilus.MenuProvider):

    def launch_vscodium(self, menu, files):
        safepaths = ''
        args = ''

        for file in files:
            filepath = file.get_location().get_path()
            safepaths += '"' + filepath + '" '

            # If one of the files we are trying to open is a folder
            # create a new instance of vscodium
            if os.path.isdir(filepath) and os.path.exists(filepath):
                args = '--new-window '

        if NEWWINDOW:
            args = '--new-window '

        call(VSCODIUM + ' ' + args + safepaths + '&', shell=True)

    def get_file_items(self, window, files):
        item = Nautilus.MenuItem(
            name='VSCodiumOpen',
            label='Ouvrir avec ' + VSCODIUMNAME,
            tip='Ouvrir les fichiers sélectionnés avec VSCodium'
        )
        item.connect('activate', self.launch_vscodium, files)

        return [item]

    def get_background_items(self, window, file_):
        item = Nautilus.MenuItem(
            name='VSCodiumOpenBackground',
            label='Ouvrir dans ' + VSCODIUMNAME,
            tip='Ouvrir le dossier actuel avec VSCodium'
        )
        item.connect('activate', self.launch_vscodium, [file_])

        return [item]
