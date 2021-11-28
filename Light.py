from manim import *
import math
import numpy as np

class Light(ThreeDScene):
    def construct(self):
        se=0.5
        nu=100
        k=20
        A=2.2
        ecolor=RED_C
        mcolor=BLUE_C
        tracker = ValueTracker(0)

        def update_elec(obj):
            t=tracker.get_value()
            xx=obj.get_x()
            pos=xx/se+nu/2
            new=Vector([0,A*np.sin(np.pi*2/k * pos + t),0],color=ecolor)
            new.shift([xx,0,0])
            new.rotate(90*DEGREES,[1,0,0],about_point=[xx,0,0])
            obj.become(new)

        def update_mag(obj):
            t=tracker.get_value()
            xx=obj.get_x()
            pos=xx/se+nu/2
            new=Vector([0,A*np.sin(np.pi*2/k * pos + t),0],color=mcolor)
            new.shift([xx,0,0])
            obj.become(new)

        Electric=VGroup()
        Magnetic=VGroup()

        for i in range(nu):
            elec=Vector([0,A*np.sin(np.pi*2/k * i),0],color=ecolor)
            elec.shift([(-nu/2+i)*se,0,0])
            elec.rotate(90*DEGREES,[1,0,0],about_point=[(-nu/2+i)*se,0,0])
            elec.add_updater(update_elec)
            Electric.add(elec)
            mag=Vector([0,A*np.sin(np.pi*2/k * i),0],color=mcolor)
            mag.shift([(-nu/2+i)*se,0,0])
            mag.add_updater(update_mag)
            Magnetic.add(mag)

        self.move_camera(frame_center=Electric.get_center(), focal_distance=60, zoom=0.8)
        print(self.camera.get_focal_distance())
        self.set_camera_orientation(phi=80 * DEGREES,theta=150*DEGREES,gamma = 0*DEGREES)
        
        #text = always_redraw(lambda: Tex("{:.2f}".format(self.camera.get_theta()/DEGREES)))
        #self.camera.add_fixed_in_frame_mobjects(text)

        #self.add(text)
        self.begin_ambient_camera_rotation(rate=-0.01, about="theta")
        self.add(Electric, Magnetic)
        self.play(tracker.animate.set_value(TAU), run_time=15, rate_func=linear)
