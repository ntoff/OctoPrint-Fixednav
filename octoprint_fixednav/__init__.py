# coding=utf-8
from __future__ import absolute_import

import octoprint.plugin

class FixednavPlugin(octoprint.plugin.AssetPlugin):

	def get_assets(self):
		return dict(
			js=["js/fixednav.js"]
		)

	def get_update_information(self):
		return dict(
			fixednav=dict(
				displayName="FixedNav",
				displayVersion=self._plugin_version,

				type="github_release",
				user="ntoff",
				repo="OctoPrint-Fixednav",
				current=self._plugin_version,

				pip="https://github.com/ntoff/OctoPrint-Fixednav/archive/{target_version}.zip"
			)
		)

__plugin_name__ = "FixedNav"

def __plugin_load__():
	global __plugin_implementation__
	__plugin_implementation__ = FixednavPlugin()

	global __plugin_hooks__
	__plugin_hooks__ = {
		"octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
	}

