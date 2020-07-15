import youtube_dl

def download(url, type_, sub_filename):
    ydl_opts = {
        'format': type_,
        'outtmpl': '%(title)s' + sub_filename
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        result = ydl.extract_info(url, download=True)
        

if __name__ == '__main__':
    flag = input("請輸入你要下載的編號 : 音訊(1)、影音(2)、匯入檔案(3)、結束(-1)。或直接貼上連結，載音訊\n")
    while flag != "-1":
        if flag == "1":
            url = input("請貼上連結\n")
            download(url, "bestaudio", ".mp3")
        elif flag == "2":
            url = input("請貼上連結\n")
            download(url, "best", ".mp4")
        elif flag == "3":
            txt = open('匯入.txt','r')
            url_list = txt.read().split('\n')
            for url in url_list:
                download(url, "bestaudio", ".mp3")
        else :
            download(flag, "bestaudio", ".mp3")
            print("直接下載")
        
        flag = input("請輸入你要下載的編號 : 音訊(1)、影音(2)、匯入檔案(3)、結束(-1)。或直接貼連結載音訊\n")
    
    print("結束")
