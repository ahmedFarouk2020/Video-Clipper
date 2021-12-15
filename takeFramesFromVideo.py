import cv2 as cv

'''
    This Class can be used to take a number of frames from 
    a video and save them to a certain location 
'''
class VideoCapturer():
    def __init__(self, pathToVideo, savePath='',
     frameBaseName='frame') -> None:

        self.pathToVideo = pathToVideo
        self.savePath = savePath
        self.frameBaseName = frameBaseName
        self.frameID = 0
        self.relativeCounter = 0

    """
        calculate number of frames between each saved image

        args:
            fps: frame per second -> int

            peroidInSec: time peroid between 2 saved imgs -> int

        return:
            None
    """
    def _calculateCounterValue(self, fps, periodInSec):
        self.relativeCounter = fps * periodInSec
        print(self.relativeCounter)
        print("_calculateCounterValue")

    """
        create a full image path with its file name
        EX: ./images/dog0.png

        args: None

        return:
            Full path: -> str
    """
    def _createFullImgName(self):
        print("_createFullImgName")
        return self.savePath+self.frameBaseName+str(self.frameID)+'.png'


    """
        start operation of capturing and saving of images

        args:
            numberOfImages: number of output saved imgs -> int

            peroidInSec: time peroid in section between 2 saved imgs -> int

            fps: frame per second -> int
        return:
            None
    """

    def start(self, numberOfImages, peroidInSec, fps=40):

        try:
            self.video = cv.VideoCapture(self.pathToVideo)
            print("capture the video successfully")
        except:
            Exception('''Error in openning video \n
            concatinate the video_name.mp4 with the path''')


        if (self.video.isOpened()== False):
            Exception("Error in opening video stream choose \
            a working video")

        self._calculateCounterValue(peroidInSec,fps)

        relativeCounter = self.relativeCounter

        while(self.video.isOpened()==True):


            ret, frame = self.video.read()

            if ret == True and numberOfImages>0:
            
                relativeCounter-=1

                if relativeCounter == 0:

                    print("relativeCounter = 0")

                    fullName = self._createFullImgName()
                    cv.imwrite(fullName, frame)

                    print("image saved!")

                    # reset counter
                    relativeCounter = self.relativeCounter

                    numberOfImages-=1

                    self.frameID+=1
            else:
                break

        print("End of the program")
        # When everything done, release the video capture object
        self.video.release()

        # Closes all the frames
        cv.destroyAllWindows()

#------------- Example ---------------------  
c1 = VideoCapturer('Videos\Racism.mp4')
c1.start(2, 30, fps=30)





