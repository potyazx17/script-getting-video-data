
user = input("specify the path to the file: ")

video = mp.VideoFileClip(user)
height_video = video.h
width_video = video.w
audio = video.audio
audio.write_audiofile("audio_video.mp3")
data_info_video = {'file_name': video.filename,
                   'fps': video.fps,
                   'height': height_video,
                   'width': width_video,
                   'video_resolution': str(height_video) + 'x' + str(width_video),
                    'video_aspect_ratio': video.aspect_ratio,
                    'memoized_frame': video.memoized_frame,
                    'has_constant_size': video.has_constant_size,
                    'len_video': video.end,
                    'size_video': video.size,
                   }
with open('data_info_video.json', 'w') as outfile:
    json.dump(data_info_video, outfile, indent=4, sort_keys=True, ensure_ascii=False, separators=(',', ': '))


print('video info saved to jason in file data_info_video.json')