import json


a = {"@context":"http://schema.org","@type":"SingleFamilyResidence","name":"Stunning | Backing Pool Park | 3 BR + Maid","url":"https://dubai.dubizzle.com/property-for-sale/residential/villahouse/2020/6/25/stunning-backing-pool-park-3-br-maid-2/","address":{"@type":"PostalAddress","addressLocality":"Dubai","addressRegion":"Dubai"},"":{"@type":"Product","name":"Stunning | Backing Pool Park | 3 BR + Maid","url":"https://dubai.dubizzle.com/property-for-sale/residential/villahouse/2020/6/25/stunning-backing-pool-park-3-br-maid-2/","offers":{"@type":"Offer","price":1200000,"priceCurrency":"AED"}},"floorSize":1820,"numberOfRooms":3,"image":"https://images.dubizzle.com/v1/files/eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbiI6ImdjczJ1eDc0enlzeC1EVUJJWlpMRSIsInciOlt7ImZuIjoiNWpldWk3cWZ6aWU2MS1EVUJJWlpMRSIsInMiOjMwLCJwIjoiY2VudGVyLDEiLCJhIjo4MH1dfQ.8rXCLj51SNAZ5-wdHOcmWxPHSBvTTl03pf_O-M9EnAE/image;p=thumb_retina","geo":{"@type":"GeoCoordinates","latitude":55.2870918641,"longitude":25.0359940685}}


b = json.dumps(a)
c = json.loads(b)

print(c['name'])
