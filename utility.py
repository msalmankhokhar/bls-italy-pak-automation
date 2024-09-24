from win10toast import ToastNotifier

toaster = ToastNotifier()
def notify(msg : str, duration : int = 3):
	toaster.show_toast(title='Automation Script', msg=msg, duration=duration)