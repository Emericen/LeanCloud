import leancloud
import geocoder

print("Connecting to server..")
leancloud.init("Yf3MSyqMdVjhofKx5vflC4eF-MdYXbMMI","n63Ne1Jj2bs17yGUPzSuYq7K")

# myloc = geocoder.ip('me')
# print(myloc.latlng)
current_location = geocoder.ip('me').latlng

pin = leancloud.Object.extend('Pinpoint')
current = pin()
current.set('Location',leancloud.GeoPoint(current_location[0], current_location[1]))
current.save()
print("Pinpoint complete!")
