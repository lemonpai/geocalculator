#/usr/bin/python3
from tkinter import *
from geographiclib.geodesic import Geodesic
from geographiclib.geomath  import Math

class ui(object):
    def __init__(self):
        self.ui = Tk()
        self.ui.title('Geo-Calculator')
        self.ui.geometry('440x350')
        self.__AddWidget()
        self.__SetPlace()
    
    def __AddWidget(self):
        self.__lat_src_label  = Label(self.ui, text = 'latitude  src (deg)')
        self.__lng_src_label  = Label(self.ui, text = 'longitude src (deg)')
        self.__lat_des_label  = Label(self.ui, text = 'latitude  dest (deg)')
        self.__lng_des_label  = Label(self.ui, text = 'longitude dest (deg)')
        self.__lat_src_entry  = Entry(self.ui)
        self.__lng_src_entry  = Entry(self.ui)
        self.__lat_des_entry  = Entry(self.ui)
        self.__lng_des_entry  = Entry(self.ui)
        self.__distance_entry = Entry(self.ui)
        self.__azimuth_entry  = Entry(self.ui)
        self.__distance_label = Label(self.ui, text = 'distance ( m )')
        self.__azimuth_label  = Label(self.ui, text = 'azimuth (deg)')
        self.__calc_inverse   = Button(self.ui, text = 'get realtion', command = self.__CalcInverse)
        self.__calc_direct    = Button(self.ui, text = 'get point',    command = self.__CalcDirect)

    def __SetPlace(self):
        self.__lat_src_label.place( x =  40, y =  40, width = 150, height = 30)
        self.__lng_src_label.place( x =  40, y =  80, width = 150, height = 30)
        self.__lat_des_label.place( x =  40, y = 120, width = 150, height = 30)
        self.__lng_des_label.place( x =  40, y = 160, width = 150, height = 30)
        self.__distance_label.place(x =  40, y = 200, width = 150, height = 30)
        self.__azimuth_label.place( x =  40, y = 240, width = 150, height = 30)
        self.__lat_src_entry.place( x = 200, y =  40, width = 200, height = 30)
        self.__lng_src_entry.place( x = 200, y =  80, width = 200, height = 30) 
        self.__lat_des_entry.place( x = 200, y = 120, width = 200, height = 30) 
        self.__lng_des_entry.place( x = 200, y = 160, width = 200, height = 30) 
        self.__distance_entry.place(x = 200, y = 200, width = 200, height = 30)
        self.__azimuth_entry.place( x = 200, y = 240, width = 200, height = 30)
        self.__calc_inverse.place(  x =  60, y = 280, width = 140, height = 30)
        self.__calc_direct.place(   x = 240, y = 280, width = 140, height = 30)


    def Show(self):
        self.ui.mainloop()

    def __CalcInverse(self):
        lat_src = float(self.__lat_src_entry.get())
        lng_src = float(self.__lng_src_entry.get())
        lat_des = float(self.__lat_des_entry.get())
        lng_des = float(self.__lng_des_entry.get())
        inv = Geodesic.WGS84.Inverse(lat_src, lng_src, lat_des, lng_des,
                     Geodesic.ALL | Geodesic.LONG_UNROLL)
        self.__distance_entry.delete(0, END)
        self.__azimuth_entry.delete(0, END)
        self.__distance_entry.insert(0, '{:.2f}'.format(inv['s12']))
        self.__azimuth_entry.insert( 0, '{:.2f}'.format(inv['azi1']))

    def __CalcDirect(self):
        lat_src  = float(self.__lat_src_entry.get())
        lng_src  = float(self.__lng_src_entry.get())
        distance = float(self.__distance_entry.get())
        azimuth  = float(self.__azimuth_entry.get())
        dir = Geodesic.WGS84.Direct(lat_src, lng_src, azimuth, distance,
                    Geodesic.ALL | Geodesic.LONG_UNROLL)
        self.__lat_des_entry.delete(0, END)
        self.__lng_des_entry.delete(0, END)
        self.__lat_des_entry.insert(0, '{:.7f}'.format(dir['lat2']))
        self.__lng_des_entry.insert(0, '{:.7f}'.format(dir['lon2']))

_ = ui()
_.Show()


