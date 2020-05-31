class Search(object):
    url = ""
    soup = None
    title = ""
    artist = ""

    def __init__(self, query):
        self.query = query

    def create_soup(self):
        page = requests.get(self.search_web())
        self.soup = BeautifulSoup(page.content, 'html.parser')
        return self.soup
