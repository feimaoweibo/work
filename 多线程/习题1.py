# 使用 _thread 线程去播放两个播放列表，一个是movie，一个是music
import _thread as thread
import time
movie_list = ["豆粕.mp4", "复仇者联盟.avi", "钢铁雨.rmvb", "xxx.mp4"]
music_list = ["周杰伦.mp3", "五月天.mp3"]
movie_format = ['mp4', 'avi']
music_format = ['mp3']
def play(playlist):
    for i in playlist:
        # 先用split('.')方法将字符串以"."开割形成一个字符串数组，然后再通过索引[1]取出所得数组中的第二个元素的值
        # 如果得到切片后的第二个值为： mp4,avi,,rmvb，存在视频格式集合里
        if i.split('.')[1] in movie_format:
            print("你现在收看的是：{}".format(i))
            time.sleep(3)
        # 如果得到切片后的第二个值为：mp3，存在歌曲格式集合里
        elif i.split('.')[1] in music_format:
            print("你现在收听的是：{}".format(i))
            time.sleep(3)
        else:
            print("没有能播放的格式")

def thread_run():
    thread.start_new_thread(play, (movie_list, ))
    thread.start_new_thread(play, (music_list, ))

if __name__ == '__main__':
    thread_run()
