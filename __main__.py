from json import dumps, loads
from base64 import decodestring, decodebytes
from os import mkdir, system
from contextlib import suppress

def readTL(tl_loc):
    with open(tl_loc) as tlfile:
        return loads(tlfile.read())

def remove_none_screenshots(timeline):
    return list(filter(lambda a: a['name'] != 'Screenshot', timeline))


def main(tl_loc, video: ('Outputs a video (requires ffmpeg)', 'flag', 'v') = False):
    timeline = readTL(tl_loc)
    frame = 0
    with suppress(FileExistsError):
        mkdir('render')
    for point in timeline:
        if point['name'] == 'Screenshot':
            with open('render/image' + str(frame) + '.jpg', 'wb') as p:
                asbytes = bytearray(point['args']['snapshot'], 'utf-8')
                p.write(decodebytes(asbytes))
                frame = frame + 1
    if video:
        system("ffmpeg -r 60 -i render/image%01d.jpg -vcodec mpeg4 -y movie.mp4")



    

if __name__ == '__main__':
    import plac; plac.call(main)