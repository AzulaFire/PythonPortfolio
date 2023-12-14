import pyglet
from pyglet.window import key
import os
from pyglet.gl import *

key = pyglet.window.key


#mypath = '/Users/jhornjr/Desktop/Music'
mypath = '/Users/jhornjr/Desktop/Training/Python/Mp4Testing'


files = []
#r=root, d=directories, f = files
for r, d, f in os.walk(mypath):
    for file in f:
        if '.mp4' in file:
            files.append(file)


num = 2
vidPath=files[num]

player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vidPath)
player.queue(MediaLoad)



class main(pyglet.window.Window):

    def __init__ (self, width=800, height=600, fps=False, *args, **kwargs):
        super(main, self).__init__(width, height, *args, **kwargs)

        self.keys = {}

        self.alive = 1

    def on_draw(self):
        if player.source and player.source.video_format:
            player.get_texture().blit(50,50)
        #self.render()

    def on_close(self):
        self.alive = 0

    def on_key_release(self, symbol, modifiers):
        try:
            del self.keys[symbol]
        except:
            pass

    def on_key_press(self, symbol, modifiers):
        global num, vidPath
        if symbol == key.ESCAPE: # [ESC]
            self.alive = 0
            self.close()
        elif symbol == key.N:
                num += 1

                MediaLoad = pyglet.media.load(vidPath)
                player.queue(MediaLoad)
                print(vidPath)
                player.next_source()

        vidPath=files[num]

        self.keys[symbol] = True

    def render(self):
        self.clear()

        ## Add stuff you want to render here.
        ## Preferably in the form of a batch.

        self.flip()

    def run(self):
        while self.alive == 1:
            # -----------> This is key <----------
            # This is what replaces pyglet.app.run()
            # but is required for the GUI to not freeze
            #

            player.play()
            event = self.dispatch_events()

            #self.render()


if __name__ == '__main__':
    x = main()
    x.run()






