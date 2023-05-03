class ProductListPage:
    HEADER_TEXT = 'Products'

    __HEADER_CONTAINER_LOCATOR = '.header_secondary_container'

    def __init__(self, page):
        self.page = page

    def title_header(self):
        return self.page.locator(f'{self.__HEADER_CONTAINER_LOCATOR} .title')
