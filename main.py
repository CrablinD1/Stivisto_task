from collections import Counter
from datetime import datetime, timedelta

import emoji

from dummy_server.server import get_random_request


def process_text(request):
    request_date = request['ts'].weekday()
    if request_date == 5:
        return 'Saturday: ' + emoji.emojize(":keycap_6:")
    elif request_date == 6:
        return 'Sunday: ' + emoji.emojize(":keycap_7:")
    else:
        content = request['content'].lower().split()
        return len(set(content))


def process_image(request):
    request_date = request['ts']
    content = request['content'].split('.')
    if request_date.weekday() in range(5, 7):
        return content[0]
    else:
        return datetime.timestamp(request_date - timedelta(days=1))


def count_extension(extension, number):
    if len(extension) == number:
        return 'OK'
    else:
        return 'REJECT'


def process_video(request):
    request_date = request['ts']
    content = request['content'].split('.')
    if request_date.weekday() in range(5, 7):
        return count_extension(content[1], 4)
    else:
        return count_extension(content[1], 3)


def process_sound(request):
    # Took algorithm from
    # geeksforgeeks.org/given-a-string-find-its-first-non-repeating-character

    content = request['content']
    freq = Counter(content)

    for i in content:
        if freq[i] == 1:
            return i

    return 'None'


if __name__ == "__main__":
    count = {
        'text': 0,
        'image': 0,
        'video': 0,
        'sound': 0
    }
    for _ in range(10):
        request = get_random_request()
        print()
        print(request)
        if request['type'] == 'text':
            count['text'] += 1
            print(process_text(request))
        elif request['type'] == 'image':
            count['image'] += 1
            print(process_image(request))
        elif request['type'] == 'video':
            count['video'] += 1
            print(process_video(request))
        elif request['type'] == 'sound':
            count['sound'] += 1
            print(process_sound(request))
    print('\n', count)
