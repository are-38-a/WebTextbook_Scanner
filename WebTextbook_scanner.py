import pyautogui
import sys
import time
import os
import img2pdf
from PIL import Image
from PIL import ImageEnhance

def enhance_image(filename):
    image1 =Image.open(filename)
    con1 = ImageEnhance.Contrast(image1)
    image2 = con1.enhance(1.5)
    con2 = ImageEnhance.Sharpness(image2)
    image3 = con2.enhance(1.5)
    image3.save(filename)

def main():
    print("左ボタンの位置")
    os.system('PAUSE')
    hidari_x,hidari_y = pyautogui.position()
    print("右ボタンの位置")
    os.system('PAUSE')
    migi_x,migi_y = pyautogui.position()

    print("左ページ左上")
    os.system('PAUSE')
    hidari_page_1,hidari_page_2 = pyautogui.position()
    print("左ページ右下")
    os.system('PAUSE')
    hidari_page_3,hidari_page_4 = pyautogui.position()

    print("右ページ左上")
    os.system('PAUSE')
    migi_page_1,migi_page_2 = pyautogui.position()
    print("右ページ右下")
    os.system('PAUSE')
    migi_page_3,migi_page_4 = pyautogui.position()

    print("フォルダ名を入力")
    dirname = input()

    print("総ページ数を入力")
    max_number = int(input())

    print("10秒後に開始します")
    time.sleep(10)
    
    dirpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), dirname)
    os.makedirs(dirpath, exist_ok=True)

    #総ページ数に達するまでスクリーンショットを撮る
    i = 0
    while i < max_number:
        time.sleep(2)

        #左側ページ
        filename = dirpath + "/" + "{:03}".format(i) + ".png"
        sc = pyautogui.screenshot(region=(hidari_page_1,hidari_page_2, hidari_page_3-hidari_page_1, hidari_page_4-hidari_page_2))
        sc.save(filename)
        enhance_image(filename) #明瞭化
        i += 1

        #右側ページ
        filename = dirpath + "/" + "{:03}".format(i) + ".png"
        sc = pyautogui.screenshot(region=(migi_page_1,migi_page_2, migi_page_3-migi_page_1, migi_page_4-migi_page_2))
        sc.save(filename)
        enhance_image(filename) #明瞭化
        i += 1

        pyautogui.click(migi_x,migi_y)
    
    # 画像フォルダの中にあるPNGファイルを取得し配列に追加
    extension  = ".png" # 拡張子がPNGのものを対象
    
    list_image = []    
    for j in os.listdir(dirpath+"/"):
        if j.endswith(extension):
            list_image.append(Image.open(dirpath+"/"+j).filename)
    
    #pdf形式で書き込み
    pdf_filename = dirpath + "/" + dirname + ".pdf" # 出力するPDFの名前
    with open(pdf_filename,"wb") as f:
        f.write(img2pdf.convert(list_image))

    print("完了")
    os.system('PAUSE')



if __name__ == "__main__":
    main()