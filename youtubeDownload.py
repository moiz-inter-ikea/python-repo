from pytube import YouTube

link = "https://www.youtube.com/watch?v=VNs_cCtdbPc"

yt = YouTube(link)  

try:
    yt.streams.filter(progressive = True, 
file_extension = "mp4").first().download(output_path = "/home/moiz/youtube-videos", 
filename = "brown-munde")
except:
    print("Some Error!")
print('Task Completed!')