'''
Using python request and splash

'''

import requests

splash_script = f"""
splash:go(args.url)
splash:set_user_agent(args.user_agent)
return splash:png()
"""

def crawl():
    SPLASH_URL = f'http://0.0.0.0:8050/run'
    TARGETED_URL = 'https://www.fiverr.com/categories'
    resp = requests.post(url=SPLASH_URL, json={'lua_source':splash_script,'url':TARGETED_URL,'user_agent':'Mozilla/5.0 (Linux; Android 10) AppleWebKit/537.36 (KHTML, like Gecko)'})
    with open('demo.png','wb') as png_file:
        png_file.write(resp.content)



def main():
    crawl()
if __name__ == "__main__":
    main()