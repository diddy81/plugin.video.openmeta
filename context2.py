import sys
import xbmc

if __name__ == '__main__':

	item = sys.listitem
	path = item.getPath().replace('?usedefault=True', '/False')
	if 'tv/play/' in path:
		path = path.replace('tv/play','tv/play_choose_player')
	elif 'movies/play/' in path:
		path = path.replace('movies/play','movies/play_choose_player')
	xbmc.executebuiltin('RunPlugin(%s)' % path)
	