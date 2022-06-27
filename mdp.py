from ffmpeg_streaming import Formats
import ffmpeg_streaming

VIDEO_DIR = 'IMDB/index/static/index/videos'
DASH_DIR = 'DASH'
MOVIE_TITLES = [
    'The Shawshank Redemption',
    'The Godfather',
]


def generate_DASH(video, output_path = '/'):

    dash = video.dash(Formats.h264())
    dash.auto_generate_representations()
    dash.output(output_path)



if __name__ == '__main__':
    for Title in MOVIE_TITLES:

        input_path = VIDEO_DIR + '/' + Title + '.mp4'
        output_path = DASH_DIR + '/' + Title + '.mpd'

        video = ffmpeg_streaming.input(input_path)
        generate_DASH(video, output_path)