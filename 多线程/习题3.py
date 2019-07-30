# 使用 类 去播放2个播放列表，一个是movie，一个是music
import threading
import time

movie_list = ["斗破.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
music_list = ['周杰伦.mp3', '五月天.mp3']
movie_format = ['mp4', 'avi']
music_format = ['mp3']

def play(playlist):
    for i in playlist:
        if i.split(".")[1] in movie_format:
            print("你现在收看的是：{}".format(i))
            time.sleep(3)
        elif i.split(".")[1] in music_format:
            print("你现在收听的是:{}".format(i))
            time.sleep(2)
        else:
            print("没有能播放的格式")

class Mythread(threading.Thread):
    def __init__(self, playlist):
        super().__init__()
        self.playlist = playlist
    def run(self):
        play(self.playlist)

if __name__ == '__main__':
    m1 = Mythread(movie_list)
    m2 = Mythread(music_list)
    m1.start()
    m2.start()