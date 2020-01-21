import key.fff
import key.test

def post(access_token):
    print("Введите путь до ssh-key")
    json_file = str(input())
    with open(json_file, "r") as read_file:
        for line in read_file:
            encode = key.test.EncodeUTF8(line)

            url = "https://api.vk.com/method/wall.post?owner_id=554411787&friends_only=0&from_group=1&message=" \
                      "{0}&services=twitter&psigned=0&mark_as_ads=0&close_comments=0&mute_notifications=0&ac" \
                      "cess_token={1}&v=5.103".format(encode.encode_to_utf8(), access_token)

            parsed_string = key.fff.get(url)
            post_id = parsed_string['response']['post_id']
            print("post_id = {0}".format(post_id))


post(access_token="")
