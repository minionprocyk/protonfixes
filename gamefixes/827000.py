""" Game fix for Celtic Kings: Rage of War
"""
#pylint: disable=C0103

from protonfixes import util

def main():
    # Fixes no sound
    util.protontricks('dsdmo')
    util.protontricks('dsound')
