# U2_downloader
Semi-finished products
Because it is found that when the image quality is 1080p or above, many of them are Adaptive and need to be downloaded and merged separately, so the current version directly provides separate downloading and merging.
If it is progressive, you can download and install it directly. The following code is an example.
Ps. I will add and organize it later, I just put it up to share first.

# Setup
pip install ffmpeg,pytubefix

# Progressive streams contain both audio and video, so they can be downloaded directly  
for stream in yt.streams.filter(progressive=True, file_extension='mp4'):  
    fps = getattr(stream, 'fps', 'N/A')  # Use getattr to avoid AttributeError, returns 'N/A' if fps attribute is not present  
    print(f"Resolution: {stream.resolution}, FPS: {fps}, Mime Type: {stream.mime_type}, Stream Type: Progressive")  
# Download the highest resolution directly  
yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution().download(filename='AAA.mp4')  
  
# Select a specific resolution video stream, e.g., 1080p  
desired_resolution = "1080p"  
stream = yt.streams.filter(progressive=True, file_extension='mp4', res=desired_resolution).first()  
  
# Check if the specific resolution video stream is found  
if stream:  
    # Download the video  
    stream.download()  
    print(f"Downloaded video at {desired_resolution} with audio included.")  
else:  
    print(f"No progressive stream available with resolution {desired_resolution}.")  


# Adaptive streams have audio and video separated, so they need to be downloaded separately and then merged  
for stream in yt.streams.filter(file_extension='mp4'):  
    fps = getattr(stream, 'fps', 'N/A')  # Use getattr to avoid AttributeError, returns 'N/A' if fps attribute is not present  
    stream_type = 'Progressive' if getattr(stream, 'is_progressive', False) else 'Adaptive'  
    print(f"Resolution: {stream.resolution}, FPS: {fps}, Mime Type: {stream.mime_type}, Stream Type: {stream_type}")  
  
