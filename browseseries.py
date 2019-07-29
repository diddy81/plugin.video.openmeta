import sys, xbmc

if __name__ == '__main__':

	item = sys.listitem

	plugin = 'plugin://plugin.video.openmeta'
	path = item.getPath().replace(plugin, '')
	tvdb = path.split('/')[3]
	url = '%s/tv/tvdb/%s/' % (plugin, tvdb)
	xbmc.executebuiltin('ActivateWindow(Videos,%s)' % url)
