import sys, xbmc

if __name__ == '__main__':

	plugin = 'plugin://plugin.video.openmeta'
	item = sys.listitem
	info = item.getVideoInfoTag()
	type = info.getMediaType()
	path = item.getPath().replace(plugin, '')
	path = path.replace('?usedefault=True', '')
	if type == 'movie':
		id = path.split('/')[4]
		xbmc.executebuiltin('RunScript(script.extendedinfo,info=playtrailer,id=%s)' % id)
	elif type == 'tvshow':
		id = path.split('/')[3]
		xbmc.executebuiltin('RunScript(script.extendedinfo,info=playtvtrailer,tvdb_id=%s)' % id)