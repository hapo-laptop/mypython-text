import glob,os,time
from PIL import Image

class Text(object):
    def __init__(self,inputdir):
        self.inputdir=inputdir
        self.piclist=glob.glob(self.inputdir+os.path.sep+'*.bmp')
        self.piclist=sorted(self.piclist,key=os.path.getmtime)
                            
    def pictotext(self,picpath):
        pic=Image.open(picpath)
        pic=pic.resize((80,30))
        pic=pic.convert('L')
        width,height=pic.size
        text=''
        pix=pic.load()
        for row in xrange(height):
            for col in  xrange(width):
                if (int(pix[col,row])<128) :
                    text+='#'
                else:
                    text+=' '
            text+='\n'
        return text
        
def main():
    display=Text('image')
    choice=raw_input('play it or not y/n?\n')
    if choice is 'y':
        for i in display.piclist:
            time.sleep(0.028)
            os.system('clear')
            char=display.pictotext(i)
            print char
            
main()
