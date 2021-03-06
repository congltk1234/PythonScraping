# Các thư viện cần thiết:
import os
import codecs
import re


# Các hàm:
# Hàm tạo thư mục:
def creat_dir():
    """
    Tạo và chuyển vị trí lưu đến thư mục vừa tạo
    : directory:
    """
    while True:
        folder = input('Nhập tên thư mục bạn muốn tạo:')
        if not os.path.exists(folder):
            os.mkdir(folder)
            print("Folder '{}' đã được tạo.".format(folder))
            os.chdir(folder)
            print('-' * 50)
            break
        else:
            check = input("Folder '{}' tồn tại. Bạn có muốn lưu tại Folder này không? (y/n) ".format(folder))
            if check == 'y' or check == 'Y':
                print("Đã chuyển vị trí lưu đến thư mục '{}'.".format(folder))
                os.chdir(folder)
                print('-' * 50)
                break


# Tạo file HTML
def saveHTML(domain, url, index, data):
    index = str(index)
    if ('.html' in url) or ('.htm' in url) or ('.chn' in url):
        name = data.title.string
        name = index + '_' + name
    else:
        if url == domain:
            name = 'TRANG CHỦ'+'_'+index
        else:
            name = re.sub(domain, 'MỤC_'+ index , url)
    name = re.sub('\W', '_', name)
    name = name + '.html'
    if not os.path.isfile(name):
        file = codecs.open(name, 'w', 'utf8')
        file.write(str(data))
        file.close()


def write_txt(index,url):
    index = str(index)
    f = open('0_URL đã tìm được.txt', 'a+')
    f.write(index + ' : ' + url + '\n')
    f.close()
