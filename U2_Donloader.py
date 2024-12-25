from pytubefix import YouTube  
import os  
import subprocess  
  
print(f"Current path: {os.getcwd()}")  
  
# Set the video URL  
url = input("Please enter the YouTube video URL: ")  
yt = YouTube(url)  
  
# Set the file name to the video title or video url ID  
video_title = yt.title.replace(" ", "_").replace("/", "_")  # Replace spaces and illegal characters  
video_id = url.split('=')[-1]  # Get video ID  
  
# Create download folder  
output_path = './downloads'  
os.makedirs(output_path, exist_ok=True)  
  
# Download video stream  
video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()  
video_file = os.path.join(output_path, 'video.mp4')  
video_stream.download(output_path=output_path, filename='video.mp4')  
  
# Download audio stream  
audio_stream = yt.streams.filter(only_audio=True).order_by('abr').desc().first()  
audio_file = os.path.join(output_path, 'audio.m4a')  
audio_stream.download(output_path=output_path, filename='audio.m4a')  
  
try:  
    merged_file = os.path.join(output_path, f"{video_title}.mp4")  
    ffmpeg_command = [  
        'ffmpeg', '-i', video_file, '-i', audio_file, '-c:v', 'copy', '-c:a', 'aac', '-strict', 'experimental', merged_file]  
    subprocess.run(ffmpeg_command, check=True)  
    print(f"Merging completed! File saved at: {merged_file}")  
except subprocess.CalledProcessError as e:  
    print(f"Merging failed, reason: {e}, changing file name to use url_ID")  
    merged_file = os.path.join(output_path, f"{video_id}.mp4")  
    ffmpeg_command[-1] = merged_file  
    subprocess.run(ffmpeg_command, check=True)  
    print(f"Merging completed! File saved at: {merged_file}")  
  
# Remove temporary files  
os.remove(video_file)  
os.remove(audio_file)  