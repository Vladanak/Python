"""from cx_Freeze import setup, Executable

setup(
    name = "National Instruments",
    version = "0.1",
    description = "Blackjack",
    executables = [Executable("National Instrument.py")]
)
"""
from distutils.core import setup
import py2exe
setup(console=['National Instrument.py'])
