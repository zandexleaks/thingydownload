import os
import subprocess

def download_youtube_shorts(channel_urls, base_output_dir):
    for index, channel_url in enumerate(channel_urls, start=1):
        channel_output_dir = os.path.join(base_output_dir, 'movies', str(index))
        if not os.path.exists(channel_output_dir):
            os.makedirs(channel_output_dir, exist_ok=True)

        command = [
            'yt-dlp',  # Changed from 'youtube-dl' to 'yt-dlp'
            '--ignore-errors',
            '-f', 'best',
            '--output', f'{channel_output_dir}/%(title)s.%(ext)s',
            '--merge-output-format', 'mp4',
            '--postprocessor-args', '-c:v libx264 -c:a aac',
            '--match-filter', 'duration < 100',
            '--no-playlist',
            '--verbose',
            channel_url + '/shorts'
        ]

        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            print(f'Error downloading shorts from {channel_url}: {e}')

if __name__ == '__main__':
    channel_urls = [
             'https://www.youtube.com/channel/UCvLZSZGK88zLOe8R2sO5KKA',
             'https://www.youtube.com/channel/UCtc7rzdsalXrtQGIQra7LtA',

]

    base_output_dir = './downloaded_shorts'

    download_youtube_shorts(channel_urls, base_output_dir)
