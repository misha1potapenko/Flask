from pathlib import Path
import requests
import threading
import multiprocessing
import argparse
import os
import time
import asyncio

final_async = 0.0
final_threading = 0.0
final_multiprocessing = 0.0

data_images = []
with open("images.txt", "r") as images:
    for image in images.readlines():
        data_images.append(image.strip())

image_path = Path("./images/")


def download_image(url):
    start_time = time.time()
    response = requests.get(url, stream=True)
    filename = image_path.joinpath(os.path.basename(url))
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    end_time = time.time() - start_time
    print(f'Загрузка {filename} завершена за {end_time:.2f} секунд')


async def download_image_async(url):
    start_time = time.time()
    response = await asyncio.get_event_loop().run_in_executor(None, requests.get, url, {"stream": True})
    filename = image_path.joinpath(os.path.basename(url))
    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    end_time = time.time() - start_time
    print(f'Загрузка {filename} завершена за {end_time:.2f} секунд')


def download_image_multiprocessing(urls):
    start_time = time.time()
    processes = []
    for url in urls:
        t = multiprocessing.Process(target=download_image, args=(url,))
        t.start()
        processes.append(t)
        for t in processes:
            t.join()
    end_time = time.time() - start_time
    print(f'Загрузка завершена за {end_time:.2f} секунд')


def download_image_threading(urls):
    start_time = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download_image, args=(url,))
        t.start()
        threads.append(t)
        for t in threads:
            t.join()
    end_time = time.time() - start_time
    print(f'Загрузка завершена за {end_time:.2f} секунд')


async def download_image_asyncio(url):
    start_time = time.time()
    tasks = []
    for url in urls:
        task = asyncio.ensure_future(download_image_async(url))
        tasks.append(task)
    await asyncio.gather(*tasks)
    end_time = time.time() - start_time
    print(f'Загрузка завершена за {end_time:.2f} секунд')


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Парсер изображений")
    parser.add_argument("--urls", default=data_images, nargs="+", help="Список адресов для загрузки")
    args = parser.parse_args()
    urls = args.urls
    if not urls:
        urls = data_images
    print(f'Загрузка {len(urls)} изображений потоки')
    download_image_threading(urls)
    print(f'Загрузка {len(urls)} изображений мультипроцессинг')
    download_image_multiprocessing(urls)
    print(f'Загрузка {len(urls)} изображений асинхронно')
    asyncio.run(download_image_asyncio(urls))
