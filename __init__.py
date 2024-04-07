# Copyright (c) 2019-2020 Elie Michel
#
# This file is part of LilySurfaceScraper, a Blender add-on to import
# materials from a single URL. It is released under the terms of the GPLv3
# license. See the LICENSE.md file for the full text.

bl_info = {
    "name": "Lily Surface Scraper",
    "author": "Élie Michel <elie.michel@exppad.com>",
    "version": (1, 9, 0),
    "blender": (4, 1, 0),
    "location": "Properties > Material",
    "description": "Import material from a single URL",
    "warning": "",
    "wiki_url": "",
    "tracker_url": "https://github.com/eliemichel/LilySurfaceScraper/issues",
    "support": "COMMUNITY",
    "category": "Import",
}

# A bit of boilerplate because this add-on is intended to be zipped with only
# the blender/LilySurfaceScraper directory, not the root of the repo
# (preferably don't use the "Download as zip" button from GitHub, but rather
# download zip files from the release pages.
import os
import sys
module_root = os.path.join(os.path.dirname(os.path.realpath(__file__)), "blender")
if module_root not in sys.path:
    sys.path.append(module_root)

from .blender.LilySurfaceScraper import register, unregister, register_callback

if __name__ == "__main__":
    register()
