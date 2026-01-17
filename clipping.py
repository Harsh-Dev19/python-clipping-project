from moviepy.video.io.VideoFileClip import VideoFileClip
import math

def split_into_two_minute_clips(input_file):
    # Load the video
    video = VideoFileClip(input_file)
    duration = video.duration  # total video length in seconds

    clip_length = 120  # 2 minutes = 120 seconds
    num_clips = math.ceil(duration / clip_length)

    print(f"Total Duration: {duration:.2f} seconds")
    print(f"Splitting into {num_clips} clips of {clip_length} seconds each...")

    for i in range(num_clips):
        start = i * clip_length
        end = min((i + 1) * clip_length, duration)  # don’t go past the video length
        clip = video.subclip(start, end)
        output_name = f"clip_{i+1}.mp4"
        clip.write_videofile(output_name, codec="libx264")
        print(f"Saved {output_name} ({start:.2f}s to {end:.2f}s)")

    video.close()
    print("✅ Done! All clips saved.")
# Example usage:
split_into_two_minute_clips(r"C:\Users\Admin\Documents\clipping_projects\input.mp4")
