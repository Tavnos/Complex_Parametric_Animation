import numpy as np
import random as rd
import primes_list
import matplotlib.pyplot as plt
from matplotlib import animation, rc
#from IPython.display import HTML


pot = primes_list.primesofthousands

class Animate_Plot:
    def param(self, min_x, max_x, min_y, max_y, v_from, v_to, v_steps):
        self.fig, self.ax = plt.subplots()
        self.ax.set_xlim((min_x,max_x))
        self.ax.set_ylim((min_y,max_y))
        self.line, = self.ax.plot([],[],lw=2)
        self.t_var = np.linspace(v_from,v_to,v_steps)
    def init(self):
        self.line.set_data([],[])
        return (self.line,)
    def animate(self, i_var):
        func_var_a = np.e**(2*np.pi*1j*pot[4]*(self.t_var+i_var*.1)) 
        func_var_b = np.e**(2*np.pi*1j*pot[6]*(self.t_var+i_var*.1)) 
        func_var_c = np.e**(2*np.pi*1j*pot[8]*(self.t_var+i_var*.1)) 
        self.x_var = (np.real(func_var_a+func_var_b+func_var_c))
        self.y_var = (np.imag(func_var_a+func_var_b+func_var_c)) # 
        self.line.set_data(self.x_var,self.y_var)
        return (self.line,)
    def anim_def(self, f_var, i_var):
        self.anim = animation.FuncAnimation(self.fig, self.animate, init_func=self.init, 
                                            frames=f_var, interval=i_var, blit=True)
    #def b_render(self):
    #    return HTML(self.anim.to_jshtml())
    def g_render(self, f_name='test_a'):
        self.anim.save('{}.gif'.format(f_name))
        
call_anim = Animate_Plot()
call_anim.param(-3, 3, -3, 3, -2*np.pi, 2*np.pi, 998)
call_anim.anim_def(100, 100)
call_anim.g_render('cool_anim_8')