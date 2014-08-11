from setuptools import setup

setup(
    name = "neo2osd",
    version = "0.14",
    packages = [ 'neo2osd' ],
    package_data = {
        'neo2osd': ['images/*', 'po/*' ]
    },
    entry_points = {
        'gui_scripts': [ 'neo2osd = neo2osd.App:main' ]
    }
)
