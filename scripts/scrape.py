import json
from urllib import request


def main():
    # https://youtu.be/FrH9s3eB6fU
    video_id = "FrH9s3eB6fU"
    with open("secrets.txt") as read_file:
        content = read_file.read()
    api_key = content.split("\n")[1]
    search_url = (
        "https://www.googleapis.com/youtube/v3/videos?id="
        + video_id
        + "&key="
        + api_key
        + "&part=contentDetails"
    )
    response = request.urlopen(search_url).read()
    data = json.loads(response)
    all_data = data["items"]
    contentetails = all_data[0]["contentDetails"]
    duration = contentetails["duration"]
    print(duration)


if __name__ == "__main__":
    main()
