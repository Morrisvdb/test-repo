import os
SECRET = os.environ['SECRET']
if SECRET == "TrustNo1":
    print("No one can be trusted")
print(SECRET)
