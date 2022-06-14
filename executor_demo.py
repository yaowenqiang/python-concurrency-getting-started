from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen


def load_url(url, timeout):
    with urlopen(url, timeout=timeout) as conn:
        return conn.read()


with ThreadPoolExecutor(max_workers=2) as executor:
    url1 = 'https://www.baidu.com'
    url2 = 'https://www.163.com'

    f1 = executor.submit(load_url, url1, 60)
    f2 = executor.submit(load_url, url2, 60)

    try:
        data1 = f1.result()
        print('{} page is {} bytes'.format(url1,len(data1)))
        data2 = f2.result()
        print('{} page is {} bytes'.format(url2,len(data2)))
    except Exception as ex:
        print('Exception downloading page' + str(ex))


