from flask import Flask, request, jsonify
import numpy as np
# from whereami import learn
# from whereami import get_pipeline
# from whereami import predict, predict_proba, crossval, locations

app = Flask(__name__)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


dataset = [["4-1(\uc544\ub974\ud14c\ud06c\ub124)", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -46}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -48}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -50}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -55}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -57}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -62}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -64}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -73}, {"mac": "GC_free_WiFi 94:64:24:9e:05:72", "rssi": -78}, {"mac": "GC_free_WiFi 94:64:24:9e:05:52", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -81}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:a1:22:80", "rssi": -89}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -91}]], ["4-2()", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -46}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -48}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -50}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -55}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -57}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -62}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -64}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -73}, {"mac": "GC_free_WiFi 94:64:24:9e:05:72", "rssi": -78}, {"mac": "GC_free_WiFi 94:64:24:9e:05:52", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -81}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:a1:22:80", "rssi": -89}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -91}]], ["4-3(425)", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -46}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -48}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -50}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -55}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -57}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -62}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -64}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -73}, {"mac": "GC_free_WiFi 94:64:24:9e:05:72", "rssi": -78}, {"mac": "GC_free_WiFi 94:64:24:9e:05:52", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -81}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:a1:22:80", "rssi": -89}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -91}]], ["4-4()", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -65}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -71}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -66}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -57}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -77}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -69}, {"mac": "GC_free_WiFi 94:64:24:9e:05:72", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -81}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:9e:3e:e0", "rssi": -63}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -85}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:72", "rssi": -85}]], ["4-5(424)", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -65}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -70}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -51}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -67}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -85}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:9e:3e:e0", "rssi": -51}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -86}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:72", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:a0:3d:02", "rssi": -91}]], ["4-6()", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -73}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -76}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -69}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -52}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -64}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -92}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -87}, {"mac": "GC_free_WiFi 94:64:24:9e:3e:e0", "rssi": -52}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -70}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -84}]], ["4-7(423)", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -73}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -76}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -69}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -52}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -64}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -92}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -87}, {"mac": "GC_free_WiFi 94:64:24:9e:3e:e0", "rssi": -52}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -70}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -84}]], ["4-8()", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -73}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -76}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -69}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -52}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -64}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -92}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -87}, {"mac": "GC_free_WiFi 94:64:24:9e:3e:e0", "rssi": -52}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -70}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -84}]], ["4-9(422)", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9f:12:00", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -70}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -78}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -66}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -53}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -65}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -78}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -86}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:9e:3e:e0", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -61}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:72", "rssi": -78}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -77}, {"mac": "GC_free_WiFi 94:64:24:9e:72:d2", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:9d:f1:12", "rssi": -89}]], ["4-10()", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -75}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -83}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -60}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -73}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:72", "rssi": -76}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -68}, {"mac": "GC_free_WiFi 94:64:24:9e:72:d2", "rssi": -86}, {"mac": "GC_free_WiFi 94:64:24:9f:83:72", "rssi": -85}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:12", "rssi": -90}]], ["4-11(421)", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -78}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -86}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -57}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -87}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -58}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:72", "rssi": -76}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -63}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:22", "rssi": -79}]], ["4-12()", [{"mac": "GC_free_WiFi 94:64:24:9f:03:c2", "rssi": -77}, {"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -86}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -81}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -75}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -62}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -55}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -68}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -69}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -80}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -87}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -62}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -76}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -59}, {"mac": "GC_free_WiFi 94:64:24:9f:83:72", "rssi": -80}, {"mac": "GC_free_WiFi 94:64:24:9f:ea:b0", "rssi": -81}, {"mac": "GC_free_WiFi 94:64:24:9d:f1:32", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:9e:84:32", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:9f:38:92", "rssi": -90}, {"mac": "GC_free_WiFi 94:64:24:9e:2d:02", "rssi": -92}]], ["4-13(420)", [{"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -72}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -77}, {"mac": "GC_free_WiFi 94:64:24:9f:45:c0", "rssi": -78}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -64}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -57}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -68}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -67}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -89}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:70", "rssi": -69}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:72", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -49}, {"mac": "GC_free_WiFi 94:64:24:9e:72:d2", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:9f:83:72", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:12", "rssi": -80}, {"mac": "GC_free_WiFi 94:64:24:9f:ea:b0", "rssi": -87}, {"mac": "GC_free_WiFi 94:64:24:a0:34:f0", "rssi": -88}]], ["4-14()", [{"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -86}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -60}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -64}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -80}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:72", "rssi": -67}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -58}, {"mac": "GC_free_WiFi 94:64:24:9e:72:d2", "rssi": -66}, {"mac": "GC_free_WiFi 94:64:24:9f:83:72", "rssi": -76}, {"mac": "GC_free_WiFi 94:64:24:9f:ea:b0", "rssi": -80}, {"mac": "GC_free_WiFi 94:64:24:a0:34:d0", "rssi": -84}]], ["4-15(419)", [{"mac": "GC_free_WiFi 94:64:24:9f:03:e2", "rssi": -88}, {"mac": "GC_free_WiFi 94:64:24:9f:12:20", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:9f:45:e0", "rssi": -84}, {"mac": "GC_free_WiFi 94:64:24:9e:3f:00", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:a0:1f:90", "rssi": -82}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:92", "rssi": -67}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:92", "rssi": -58}, {"mac": "GC_free_WiFi 94:64:24:9e:72:f2", "rssi": -50}, {"mac": "GC_free_WiFi 94:64:24:9f:fb:32", "rssi": -79}, {"mac": "GC_free_WiFi 94:64:24:a1:22:80", "rssi": -89}, {"mac": "GC_free_WiFi 94:64:24:9f:c4:42", "rssi": -87}, {"mac": "GC_free_WiFi 94:64:24:a0:fe:e0", "rssi": -67}, {"mac": "GC_free_WiFi 94:64:24:9f:83:92", "rssi": -69}, {"mac": "GC_free_WiFi 94:64:24:9e:8a:72", "rssi": -62}, {"mac": "GC_free_WiFi 94:64:24:a1:6f:72", "rssi": -65}, {"mac": "GC_free_WiFi 94:64:24:9e:72:d2", "rssi": -62}, {"mac": "GC_free_WiFi 94:64:24:9f:ea:b0", "rssi": -77}, {"mac": "GC_free_WiFi 94:64:24:9d:f1:32", "rssi": -85}, {"mac": "GC_free_WiFi 94:64:24:a0:34:f0", "rssi": -74}, {"mac": "GC_free_WiFi 94:64:24:a0:34:d0", "rssi": -75}, {"mac": "GC_free_WiFi 94:64:24:9e:2c:e2", "rssi": -68}, {"mac": "GC_free_WiFi 94:64:24:a1:00:c2", "rssi": -89}]]]

def calculate_euclidean_distance(pattern, rssi_values):
    distance = np.sqrt(np.sum((np.array(pattern) - np.array(rssi_values)) ** 2))
    return distance


@app.route('/addpoint', methods=['POST'])
def add_point():
    learn()
    point_data = request.json
    name = point_data['name']
    data = [{'mac': ap['mac'], 'rssi': ap['rssi']} for ap in point_data['data']]
    dataset.append((name, data))
    print(dataset)
    return jsonify({'message': 'Point added successfully.'})


@app.route('/getpoint', methods=['POST'])
def get_point():
    rssi_values = [ap['rssi'] for ap in request.json['data']]
    matched_location = match_pattern(rssi_values)
    return jsonify({'location': matched_location})



def match_pattern(rssi_values):
    distances = []
    for data in dataset:
        print(data)
        dataset_ap_values = [ap['rssi'] for ap in data[1]]
        min_length = min(len(rssi_values), len(dataset_ap_values))
        distance = calculate_euclidean_distance(dataset_ap_values[:min_length], rssi_values[:min_length])
        distances.append(distance)

    min_index = np.argmin(distances)
    matched_location = dataset[min_index][0]
    return matched_location

if __name__ == '__main__':
    app.run()