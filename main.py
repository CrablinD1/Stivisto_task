import emoji
from datetime import datetime, timedelta

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


if __name__ == "__main__":
    for _ in range(10):
        request = get_random_request()
        print(request)
        if request['type'] == 'text':
            print(process_text(request))
        elif request['type'] == 'image':
            print(process_image(request))
