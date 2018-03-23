#returns 'Terrace' if it's Wednesday and this person likes orange chicken or if
#it's any day of the week and this person likes Pho.  Otherwise returns
#'Trillium'.
def terrace_or_trillium(is_wednesday, likes_orange_chicken, likes_pho):
	pass
	if(is_wednesday==True and likes_orange_chicken==True) or (likes_pho==True):
		result=('Terrace')
	else:
		result=('Trillium')
	print(result)
	return result