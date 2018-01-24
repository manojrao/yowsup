from yowsup.layers.interface                           import YowInterfaceLayer, ProtocolEntityCallback
from yowsup.layers import YowLayerEvent
from yowsup.layers.network import YowNetworkLayer
import os
import sys
import io
import time
# import Image
class EchoLayer(YowInterfaceLayer):
    @ProtocolEntityCallback("message")
    def onMessage(self, messageProtocolEntity):
        if messageProtocolEntity.getType() == 'text':
            self.onTextMessage(messageProtocolEntity)
        elif messageProtocolEntity.getType() == 'media':
            self.onMediaMessage(messageProtocolEntity)

        # self.toLower(messageProtocolEntity.forward(messageProtocolEntity.getFrom()))
        self.toLower(messageProtocolEntity.ack())
        self.toLower(messageProtocolEntity.ack(True))


    # @ProtocolEntityCallback("receipt")
    # def onReceipt(self, entity):
    #     print entity
    #     self.toLower(entity.ack())

    @ProtocolEntityCallback("iq")
    def onIq(self, entity):
        self.broadcastEvent(YowLayerEvent(YowNetworkLayer.EVENT_STATE_DISCONNECT))

    def onTextMessage(self,messageProtocolEntity):
        # just print info
        print messageProtocolEntity
        print("Echoing %s to %s" % (messageProtocolEntity.getBody(), messageProtocolEntity.getFrom(False)))
        # sys.exit(0)

    def onMediaMessage(self, messageProtocolEntity):
        # just print info
        # print messageProtocolEntity.getMediaType()
        # sys.exit(0)
        if messageProtocolEntity.getMediaType() == "image":
            print("Echoing image %s to %s" % (messageProtocolEntity.url, messageProtocolEntity.getFrom(False)))
            filename=messageProtocolEntity.getMediaSize()
            typemedia=messageProtocolEntity.getMimeType()
            filename1=typemedia.split("/")
            
            filename=str(time.time())+str(filename)+'.'+str(filename1[1])
            bytes1=messageProtocolEntity.getMediaContent()
            path='/usr/local/lib/python2.7/site-packages/yowsup2-2.5.7-py2.7.egg/yowsup/'+str(messageProtocolEntity.getFrom(False))
            if os.path.isdir(path):
                pass
            else:
                os.mkdir( path, 0755 )
            file = open(path+'/'+filename,'w') 
            file.write(bytes1)
            file.close() 
        elif messageProtocolEntity.getMediaType() == "location":
            print("Echoing location (%s, %s) to %s" % (messageProtocolEntity.getLatitude(), messageProtocolEntity.getLongitude(), messageProtocolEntity.getFrom(False)))

        elif messageProtocolEntity.getMediaType() == "vcard":
            print("Echoing vcard (%s, %s) to %s" % (messageProtocolEntity.getName(), messageProtocolEntity.getCardData(), messageProtocolEntity.getFrom(False)))
