from pathlib import Path
import requests, threading, multiprocessing, argparse, os, time, asyncio

final_async = 0.0
final_threading = 0.0
final_multiprocessing = 0.0

data_image = []
with open("images.txt", "r") as images:
    for image in images.readlines():
        data_image.append(image.strip())

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


async def download_image_threading(url):
    start_time = time.time()
    threads = []
    for url in urls:
        t = threading.Thread(target=download_image(), args=(url,))
        t.start()
        threads.append()
        for t in threads:
            t.join()
    end_time = time.time() - start_time
    print(f'Загрузка завершена за {end_time:.2f} секунд')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Парсер изображений")
    parser.add_argument("--urls", default=data_image, nargs="+", help="Список адресов для загрузки")
    args = parser.parse_args()
    urls = args.urls
    if not urls:
        urls = data_image
    print(f'Загрузка {len(urls)} изображений потоки')

    print(f'Загрузка {len(urls)} изображений мультипроцессинг')

    print(f'Загрузка {len(urls)} изображений асинхронно')