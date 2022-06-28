def domain_name(url: str) -> str:
    """
    Return domain from url.
    :param url: url to parse
    :return: domain name
    """
    url_splitted = url.split('//')
    if len(url_splitted) == 1:
        if 'www' in url_splitted[0]:
            return url_splitted[0].split('.')[1]  # case for www.url.com
        else:
            return url_splitted[0].split('.')[0]  # case for url.com

    if 'www' in url_splitted[1]:
        return url_splitted[1].split('.')[1]  # case for http://www.url.com
    return url_splitted[1].split('.')[0]  # case for http://url.com


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("https://www.youtube.com") == "youtube"
assert domain_name("http://www.youtube.com") == "youtube"
assert domain_name("www.youtube.com") == "youtube"
assert domain_name("youtube.com") == "youtube"
assert domain_name("google.co.jp") == "google"
assert domain_name("https://google.co.jp") == "google"
assert domain_name("http://www.google.co.jp") == "google"
assert domain_name("https://www.google.co.jp") == "google"
assert domain_name("www.google.co.jp") == "google"
assert domain_name("google.co.jp") == "google"
