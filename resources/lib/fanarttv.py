# -*- coding: utf-8 -*-

from resources.lib.xswift2 import plugin
import requests, xbmc

client_key = plugin.get_setting('fanart.apikey', str)
base_url = "http://webservice.fanart.tv/v3/%s/%s"
api_key = "de2514186c9e2778800f9fdb6b32c47a"
language = xbmc.getLanguage(xbmc.ISO_639_1)

def get_query_lang(art, lang, season=False):
    if art is None: return ''
    if not any(i['lang'] == lang for i in art):
        lang = 'en'
    try:
        if season:
            temp = []
            for i in art:
                if i['season'] == str(season):
                    temp.append(i)
                    art = temp
        result = [(x['url'], x['likes']) for x in art if x.get('lang') == lang]
        result = [(x[0], x[1]) for x in result]
        result = sorted(result, key=lambda x: int(x[1]), reverse=True)
        result = [x[0] for x in result][0]
        result = result

    except:
        result = ''
    if not 'http' in result: result = ''

    return result

def get_query(art):
    if art is None: return ''
    try:
        result = [(x['url'], x['likes']) for x in art]
        result = [(x[0], x[1]) for x in result]
        result = sorted(result, key=lambda x: int(x[1]), reverse=True)
        result = [x[0] for x in result][0]
        result = result.encode('utf-8')

    except:
        result = ''
    if not 'http' in result: result = ''

    return result

@plugin.cached(TTL=60*24*7, cache='Fanart')
def get(remote_id, query, season):

    art = base_url % (query, remote_id)
    headers = {'client-key': client_key, 'api-key': api_key}

    art = requests.get(art, headers=headers).json()

    if query == 'movies':

        meta = {'poster': get_query_lang(art.get('movieposter'), language),
                'fanart': get_query_lang(art.get('moviebackground'), ''),
                'banner': get_query_lang(art.get('moviebanner'), language),
                'clearlogo': get_query_lang(art.get('movielogo', []) + art.get('hdmovielogo', []), language),
                'landscape': get_query_lang(art.get('moviethumb'), language)}
    elif season:
        meta = {'poster': get_query_lang(art.get('seasonposter'), language, season),
                'fanart': get_query_lang(art.get('showbackground'), ''),
                'banner': get_query_lang(art.get('seasonbanner'), language, season),
                'clearart': get_query_lang(art.get('clearart', []) + art.get('hdclearart', []), language),
                'clearlogo': get_query_lang(art.get('hdtvlogo', []) + art.get('clearlogo', []), language),
                'landscape': get_query_lang(art.get('tvthumb'), language)}
    else:
        meta = {'poster': get_query_lang(art.get('tvposter'), language),
                'fanart': get_query_lang(art.get('showbackground'), ''),
                'banner': get_query_lang(art.get('tvbanner'), language),
                'clearart': get_query_lang(art.get('clearart', []) + art.get('hdclearart', []), language),
                'clearlogo': get_query_lang(art.get('hdtvlogo', []) + art.get('clearlogo', []), language),
                'landscape': get_query_lang(art.get('tvthumb'), language)}

    return meta
