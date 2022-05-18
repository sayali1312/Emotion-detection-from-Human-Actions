import pafy
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.youtube.com/watch?v=uAPUkgeiFVY"
videoPafy = pafy.new(url)
best = videoPafy.getbest(preftype="mp4")
