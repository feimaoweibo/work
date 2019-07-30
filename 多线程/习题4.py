# 使用 多进程 去播放2个播放列表，一个是movie，一个是music
import time
import multiprocessing

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

if __name__ == '__main__':
    t1 = multiprocessing.Process(target=play, args=(movie_list, ))
    t2 = multiprocessing.Process(target=play, args=(music_list, ))
    t1.start()
    t2.start()