import requests
import sys


def loop():
    for word in sys.stdin:
        res = requests.get(url=f"http://localhost:8888/{word}")
        if res.status_code == 404 or res.status_code == 400:
            loop()
        else:
            print(res.status_code)
            print(res.url)


def main():
    loop()


if __name__ == '__main__':
    main()
