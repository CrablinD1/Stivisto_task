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


if __name__ == "__main__":
    for _ in range(10):
        request = get_random_request()
        print(request)
        if request['type'] == 'text':
            print(process_text(request))
