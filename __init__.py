from Main_Window import *

class MainApp(Frame,Main_Window,Functionality,Emerging_Windows):

	def __init__(self, Window , *args , **kwargs):
		Frame.__init__(self, *args, **kwargs)
		self.User=StringVar()
		self.Password=StringVar()
		self.Create_Window_Login(Window)
			
	def Create_Main_Window(self):
		Privilege_Value=self.Privilege_Value
		Default=self.Default
		window=Tk()
		Main_Window(window,Privilege_Value,Default)
		window.mainloop()
		
if __name__=="__main__":
	window=Tk()
	MainApp(window)
	window.mainloop()
