"""
create a mp4 with 3 layers side by side
in: folder with layers, pattern
out:mp4
"""
import sys
import os


def main(args):
    print("parameters: \n0 -> pathIn (folder ../folder/) \n1 -> pattern (holes, solitons,...) \n2 -> pathOut (folder ../) \n3 -> step \n4 -> step max \n4 -> mameVideo")
    pathInFolder, pattern , pathOut ,step, stepMax = args[0],args[1],args[2],int(args[3]) ,int(args[4])

    t = 0
    while t <= stepMax:
        # crop
        sizeX , sizeY , cropX,cropY = 800,562, 146, 27
        cropSpace = str(sizeX-2*cropX)+"x"+str(sizeY-2*cropY)+"+"+str(cropX)+"+"+str(cropY)
        os.system("magick convert {0}{1}_net_{2:0>4}.png -crop {3} {0}{1}_net_crop_{2:0>4}.png".format(pathInFolder,pattern,t,cropSpace))
        print("magick convert {0}{1}_net_{2:0>4}.png -crop {3} {0}{1}_net_crop_{2:0>4}.png".format(pathInFolder,pattern,t,cropSpace))
        # mount images
        os.system("{0} -geometry 512x512+2+2 {2}{1}_lcRD_{3:0>4}.png {2}{1}_vfRD_{3:0>4}.png {2}{1}_net_crop_{3:0>4}.png -size 800x256 {4}{1}_layers_{3:0>4}.jpg".format("magick montage",pattern,pathInFolder,t,pathOut))
        t += step
#
    # make video
    print ("ffmpeg -framerate 2 -i %4d.png " +pathOut+pattern+".mp4")
    os.system("ffmpeg -framerate 10 -i "+ pathOut +pattern+"%*.jpg " +pathOut+pattern+".mp4")




if __name__ == "__main__":
    main(sys.argv[1:])
