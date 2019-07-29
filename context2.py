import sys
import xbmc

if __name__ == '__main__':

	item = sys.listitem
	path = item.getPath().replace('True', 'False')
	xbmc.executebuiltin('RunPlugin(%s)' % path)
