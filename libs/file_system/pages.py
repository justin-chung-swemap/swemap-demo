import os
import json

class Page:
    def __init__(self, page_id, content, author):
        self.id = page_id
        self.content = content
        self.author = author
        self.created_at = "now"
        self.updated_at = "now"
        self.is_published = False
        self.tags = []

    def update_content(self, new_content):
        self.content = new_content
        self.updated_at = "now_updated"

    def publish(self):
        self.is_published = True

    def unpublish(self):
        self.is_published = False

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)

class PageDirectory:
    def __init__(self, name):
        self.name = name
        self.pages = {}
        self.sub_directories = {}

    def add_page(self, page):
        self.pages[page.id] = page

    def get_page(self, page_id):
        return self.pages.get(page_id)

    def remove_page(self, page_id):
        if page_id in self.pages:
            del self.pages[page_id]

    def create_sub_directory(self, name):
        if name not in self.sub_directories:
            self.sub_directories[name] = PageDirectory(name)
        return self.sub_directories[name]

    def get_all_pages(self):
        all_pages = list(self.pages.values())
        for subdir in self.sub_directories.values():
            all_pages.extend(subdir.get_all_pages())
        return all_pages

    def find_pages_by_author(self, author):
        return [p for p in self.get_all_pages() if p.author == author]

    def find_pages_by_tag(self, tag):
        return [p for p in self.get_all_pages() if tag in p.tags]

    def get_published_pages(self):
        return [p for p in self.get_all_pages() if p.is_published]

    def count_pages(self):
        return len(self.get_all_pages())

def analyze_page_directory(directory):
    total = directory.count_pages()
    published = len(directory.get_published_pages())
    return {
        "total": total,
        "published": published,
        "drafts": total - published
    }

def serialize_page(page):
    return {
        "id": page.id,
        "content": page.content,
        "author": page.author,
        "is_published": page.is_published,
        "tags": page.tags
    }
