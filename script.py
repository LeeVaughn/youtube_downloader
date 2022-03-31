from pytube import YouTube

urls = ['https://youtu.be/vYQy8-7Ut1E', 'https://youtu.be/7NECN3x8XTY', 'https://youtu.be/lJf1qaGVVuY', 'https://youtu.be/LK4cWp2AHxY']

def download_audio(url):
    yt = YouTube(url)

    # properties on the yt object like .author, .title, and .description can be accessed if needed (https://pytube.io/en/latest/api.html#youtube-object)
    # print(yt.author)
    # print(yt.title)
    # print(yt.description)
    # print(yt.keywords)

    yt.streams.filter(only_audio=True).first().download(output_path="./audio")

    print(f'\n{yt.title} successfully downloaded.\n')


for url in urls:
    download_audio(url)

# print('Video downloads complete.')