import time
import os
import sys

def count_down(minutes):
    total_seconds = minutes * 60

    print(f" 番茄钟开启：开始专注{minutes}分钟！")
    print("----------------------------------")

    try:
        while total_seconds >=0:
            #计算剩余的分钟和秒数
            mins,secs = divmod(total_seconds,60)

            #格式化为00：00的样式
            timer = f"{mins:02d}:{secs:02d}"
            sys.stdout.write(f"\r 距离休息还剩：{timer}")
            sys.stdout.flush()

            #每隔一秒倒计时减一
            time.sleep(1)
            total_seconds -= 1

        #倒计时结束后的提示
        print("\n\n 时间到！太棒了，你完成了一次专注！")
        
    except KeyboardInterrupt:
        # 如果中途按下 Ctrl+C 退出，优雅地结束程序
        print("\n\n⏹️ 番茄钟已被手动终止。休息一下吧！")

if __name__ == "__main__":
    # 为了方便今晚测试，你可以先设置成专注 1 分钟（甚至 0.1 分钟测试 6 秒）
    # 后面真正使用时可以改成 25
    focus_time = 1 
    count_down(focus_time)


                               