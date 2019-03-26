from multiprocessing import Pool
import bs4 as bs
import random
import requests
import string

def random_stanting_url():
    start = ''.join(random.SystemRandom().choice(string.ascii_lowercase)for _ in range(3))
    url = ''.join(['http://', start, '.com'])
    return url

def handle_local_links(url, link):
    if link.startswith('/'):
        return ''.join([url, link])
    else:
        return link

def get_links(url):
    try:
        print('Trying: {}'.format(url))
        r = requests.get(url)
        soup = bs.BeautifulSoup(r.text, 'lxml')
        body = soup.body
        links = [link.get('href') for link in body.find_all('a')]
        links = [handle_local_links(url, link) for link in links]
        #links = [str(link.encode('ascii')) for link in links]
        # ...Anything more to get from the body
        return links
    except TypeError as e:
        print(e)
        return []
    except IndexError as e:
        print(e)
        return []
    except AttributeError as e:
        print(e)
        return []
    except Exception as e:
        print(str(e))
        # Log this to improve the script
        return []

def main():
    spawns = 20
    p = Pool(processes=spawns)
    urls = [random_stanting_url() for _ in range(spawns)]
    print('URLs to Parse:', urls, '\n\n\n')
    data = p.map(get_links, [link for link in urls])
    print('All Found URLs', data, '\n\n\n')
    data = [url for url_list in data for url in url_list]
    print('New URL list', data, '\n\n\n')
    p.close()

    with open('urls.txt', 'w') as f:
        for url in data:
            f.write(str(url) + '\n')

if __name__ == "__main__":
    main()