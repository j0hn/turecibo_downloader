# -*- coding: utf-8 -*-
"""Console script for turecibo_downloader."""

import sys
import click

from .turecibo_downloader import DocumentDownloader, FolderDownloader


@click.group()
def cli():
    pass


@click.argument('doc_hash')
@cli.command('by-hash')
def by_hash(doc_hash):
    """
    Download and save the document identified by HASH. See details on how to get
    hashes from turecibo.com files on the README
    """
    DocumentDownloader(doc_hash=doc_hash).download()


@click.argument('cookie')
@click.argument('folder')
@cli.command('by-inbox')
def by_inbox(cookie, folder):
    """
    Downloads and save the document identified by HASH.
    See details on how to get the cookie and folder on the README
    """
    FolderDownloader(cookie, folder).download()


if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover
