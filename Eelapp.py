import eel

eel.init('web')

@eel.expose

def solve(val):
	res = int(eval(val))
	return res
   

eel.start('cal.html',size=(280,390)) #650,615
