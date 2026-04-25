# https://www.codewars.com/kata/515bb423de843ea99400000a


class PaginationHelper:
    def __init__(self, collection, items_per_page):
        self.collection = collection
        self.items_per_page = items_per_page

    def item_count(self):
        return len(self.collection)

    def page_count(self):
        return -(-self.item_count() // self.items_per_page)

    def page_item_count(self, page_index):
        last_page = self.page_count() - 1
        return (
            -1
            if page_index < 0 or page_index > last_page
            else self.items_per_page
            if page_index < last_page
            else self.item_count() % self.items_per_page or self.items_per_page
        )

    def page_index(self, item_index):
        return (
            -1
            if item_index < 0 or item_index >= self.item_count()
            else item_index // self.items_per_page
        )
