# coding=utf-8
import setuptools
import octoprint_setuptools

setuptools.setup(**octoprint_setuptools.create_plugin_setup_parameters(
	identifier="netconnectdEXO",
	name="OctoPrint-NetconnectdEXO",
	version="0.1",
	description="Client for netconnectd that allows configuration of netconnectd through OctoPrint's settings dialog. It's only available for Linux right now.",
	author="Mariano Ronchi",
	mail="osd@foosel.net",
	url="http://github.com/marianoronchi/OctoPrint-Netconnectd",
	requires=[
		"OctoPrint"
	]
))
