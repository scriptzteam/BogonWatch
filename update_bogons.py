#!/usr/bin/env python3
import logging
import sys
import os
from pathlib import Path

import requests

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    stream=sys.stdout
)

def download_file(url: str, dest: Path, chunk_size: int = 8192, timeout: int = 30) -> bool:
    """
    Download a file from a URL using HTTP streaming and save it locally.
    :param url: HTTP(S) URL to download from
    :param dest: Local file path (including filename) where to save content
    :param chunk_size: Size of each read chunk in bytes (default: 8 KB)
    :param timeout: Timeout in seconds for the HTTP request
    :returns: True if download succeeded and file non-empty; False otherwise
    """
    try:
        logging.info(f'Starting download: {url}')
        response = requests.get(url, stream=True, timeout=timeout, headers={
            'User-Agent': 'Mozilla/5.0 (compatible; BogonWatch/1.0)'
        })
        response.raise_for_status()

        dest.parent.mkdir(parents=True, exist_ok=True)
        total_bytes = 0

        with dest.open('wb') as fp:
            for chunk in response.iter_content(chunk_size=chunk_size):
                if chunk:  # skip keep-alive chunks
                    fp.write(chunk)
                    total_bytes += len(chunk)

        if total_bytes > 0:
            logging.info(f'Download successful: wrote {total_bytes} bytes to {dest}')
            return True
        else:
            logging.error(f'Download failed: {dest} is empty')
            return False

    except requests.exceptions.RequestException as exc:
        logging.error(f'Error downloading {url}: {exc}')
        return False

def main():
    """
    Main entry point: iterate through source URLs and download each file.
    Exits with status 1 on any failure.
    """
    sources = {
        'bogons_ipv4.txt': 'https://team-cymru.org/Services/Bogons/fullbogons-ipv4.txt',
        'bogons_ipv6.txt': 'https://team-cymru.org/Services/Bogons/fullbogons-ipv6.txt',
    }

    all_success = True

    for filename, url in sources.items():
        dest = Path(filename)
        logging.info(f'Processing {filename}')
        if not download_file(url, dest):
            all_success = False
            logging.error(f'Failed to download {filename}')
        else:
            logging.info(f'Successfully downloaded {filename}')

    if not all_success:
        logging.error('One or more downloads failed')
        sys.exit(1)
    else:
        logging.info('All files downloaded successfully')

if __name__ == '__main__':
    main()
