# -*- coding: utf-8 -*-
import io
import tqdm
import requests
from PIL import Image

BASE_URL = 'https://api.nosconecta.com.ar/'
PATH = 'eform/thumbnail/{}'
BASE_PARAMS = {
    'resize': 'full',
    'page': '0',
}
FOLDER_URL = 'https://ar.turecibo.com/bandeja.php?apiendpoint=/folders/{}/documents/available'
MAX_FAILED_REQUESTS = 3


class DocumentDownloader:
    def __init__(self, doc_hash, filename=None):
        self.doc_hash = doc_hash
        self.filename = filename if filename is not None else '{}.pdf'.format(doc_hash)
        self.url = BASE_URL + PATH.format(self.doc_hash)

    def download(self):
        pages = self.get_pages()
        self.save_as_pdf(pages)

    def get_pages(self):
        """
        Downloads all the pages and returns them as an ordered list of images
        loaded in memory
        """

        session = requests.session()
        params = BASE_PARAMS.copy()
        pages = []
        page = 0
        req_failed = 0
        bar = tqdm.tqdm(desc=self.filename, unit='pages')
        while req_failed < MAX_FAILED_REQUESTS:
            page += 1
            params.update({'page': '{}'.format(page)})
            req = session.get(self.url, params=params)

            if req.headers.get('Content-Type').startswith('application/json'):
                # This is probably an error message, we are most likely
                # out of bounds. Continue trying to get pages though
                req_failed += 1
                continue

            bar.update(1)
            img = Image.open(io.BytesIO(req.content))
            pages.append(img)

        bar.close()
        return pages

    def save_as_pdf(self, pages):
        first_page, pages = pages[0], pages[1:]
        first_page.save(
            self.filename, 'PDF', resolution=100.0,
            save_all=True, append_images=pages
        )


class FolderDownloader:
    def __init__(self, cookie, folder):
        self.cookie = cookie
        self.folder = folder

    def download(self):
        url = FOLDER_URL.format(self.folder)
        data = dict(reload='1')
        headers = dict(cookie=self.cookie)
        req = requests.post(url, data=data, headers=headers)

        try:
            response = req.json()
        except:
            print('Error, invalid cookie?')
            return -1

        categories = response.get('categorias', {})
        for document in categories.get('documentos', []):
            doc_hash = document.get('archivo')
            DocumentDownloader(doc_hash=doc_hash).download()
