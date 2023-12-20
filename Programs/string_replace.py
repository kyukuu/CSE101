fn=input()
ln=input()
    
strin="Hello firstname lastname! You just delved into python."
strin=strin.replace("firstname", str(fn))
strin=strin.replace("lastname", str(ln))

print(strin)