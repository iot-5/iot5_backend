import json


old_data = [
  {
    "name": "4-1(아르테크네)",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -46 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -48 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -50 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -55 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -57 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -62 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -64 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -73 },
      { "GC_free_WiFi 94:64:24:9e:05:72": -78 },
      { "GC_free_WiFi 94:64:24:9e:05:52": -79 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -79 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -81 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -83 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -88 },
      { "GC_free_WiFi 94:64:24:a1:22:80": -89 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -90 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -91 }
    ]
  },
  {
    "name": "4-2()",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -46 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -48 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -50 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -55 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -57 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -62 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -64 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -73 },
      { "GC_free_WiFi 94:64:24:9e:05:72": -78 },
      { "GC_free_WiFi 94:64:24:9e:05:52": -79 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -79 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -81 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -83 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -88 },
      { "GC_free_WiFi 94:64:24:a1:22:80": -89 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -90 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -91 }
    ]
  },
  {
    "name": "4-3(425)",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -46 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -48 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -50 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -55 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -57 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -62 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -64 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -73 },
      { "GC_free_WiFi 94:64:24:9e:05:72": -78 },
      { "GC_free_WiFi 94:64:24:9e:05:52": -79 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -79 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -81 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -83 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -88 },
      { "GC_free_WiFi 94:64:24:a1:22:80": -89 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -90 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -91 }
    ]
  },
  {
    "name": "4-4()",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -72 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -65 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -71 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -66 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -72 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -57 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -77 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -69 },
      { "GC_free_WiFi 94:64:24:9e:05:72": -90 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -72 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -81 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -82 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -88 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -90 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -90 },
      { "GC_free_WiFi 94:64:24:9e:3e:e0": -63 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -74 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -85 },
      { "GC_free_WiFi 94:64:24:9e:8a:72": -85 }
    ]
  },
  {
    "name": "4-5(424)",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -74 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -72 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -74 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -65 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -70 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -51 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -74 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -67 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -74 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -84 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -85 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -88 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -90 },
      { "GC_free_WiFi 94:64:24:9e:3e:e0": -51 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -74 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -86 },
      { "GC_free_WiFi 94:64:24:9e:8a:72": -83 },
      { "GC_free_WiFi 94:64:24:a0:3d:02": -91 }
    ]
  },
  {
    "name": "4-6()",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -79 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -73 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -76 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -69 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -72 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -52 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -83 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -64 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -72 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -82 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -82 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -82 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -92 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -87 },
      { "GC_free_WiFi 94:64:24:9e:3e:e0": -52 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -70 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -88 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -84 }
    ]
  },
  {
    "name": "4-7(423)",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -79 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -73 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -76 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -69 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -72 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -52 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -83 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -64 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -72 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -82 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -82 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -82 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -92 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -87 },
      { "GC_free_WiFi 94:64:24:9e:3e:e0": -52 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -70 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -88 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -84 }
    ]
  },
  {
    "name": "4-8()",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -79 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -73 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -76 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -69 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -72 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -52 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -83 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -64 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -72 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -82 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -82 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -82 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -92 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -87 },
      { "GC_free_WiFi 94:64:24:9e:3e:e0": -52 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -70 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -88 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -84 }
    ]
  },
  {
    "name": "4-9(422)",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -79 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -79 },
      { "GC_free_WiFi 94:64:24:9f:12:00": -74 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -70 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -78 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -66 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -83 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -53 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -65 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -72 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -78 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -86 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -90 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -90 },
      { "GC_free_WiFi 94:64:24:9e:3e:e0": -74 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -61 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -84 },
      { "GC_free_WiFi 94:64:24:9e:8a:72": -78 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -77 },
      { "GC_free_WiFi 94:64:24:9e:72:d2": -84 },
      { "GC_free_WiFi 94:64:24:9d:f1:12": -89 }
    ]
  },
  {
    "name": "4-10()",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -82 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -75 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -83 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -60 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -73 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -88 },
      { "GC_free_WiFi 94:64:24:9e:8a:72": -76 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -68 },
      { "GC_free_WiFi 94:64:24:9e:72:d2": -86 },
      { "GC_free_WiFi 94:64:24:9f:83:72": -85 },
      { "GC_free_WiFi 94:64:24:9f:fb:12": -90 }
    ]
  },
  {
    "name": "4-11(421)",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -78 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -86 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -57 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -74 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -87 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -58 },
      { "GC_free_WiFi 94:64:24:9e:8a:72": -76 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -63 },
      { "GC_free_WiFi 94:64:24:9f:c4:22": -79 }
    ]
  },
  {
    "name": "4-12()",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:c2": -77 },
      { "GC_free_WiFi 94:64:24:9f:03:e2": -86 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -81 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -75 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -62 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -55 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -68 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -69 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -80 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -87 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -84 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -62 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -76 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -59 },
      { "GC_free_WiFi 94:64:24:9f:83:72": -80 },
      { "GC_free_WiFi 94:64:24:9f:ea:b0": -81 },
      { "GC_free_WiFi 94:64:24:9d:f1:32": -84 },
      { "GC_free_WiFi 94:64:24:9e:84:32": -88 },
      { "GC_free_WiFi 94:64:24:9f:38:92": -90 },
      { "GC_free_WiFi 94:64:24:9e:2d:02": -92 }
    ]
  },
  {
    "name": "4-13(420)",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:e2": -79 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -72 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -84 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -77 },
      { "GC_free_WiFi 94:64:24:9f:45:c0": -78 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -64 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -57 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -68 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -67 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -84 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -89 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -84 },
      { "GC_free_WiFi 94:64:24:a0:1f:70": -69 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -79 },
      { "GC_free_WiFi 94:64:24:9e:8a:72": -74 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -49 },
      { "GC_free_WiFi 94:64:24:9e:72:d2": -74 },
      { "GC_free_WiFi 94:64:24:9f:83:72": -82 },
      { "GC_free_WiFi 94:64:24:9f:fb:12": -80 },
      { "GC_free_WiFi 94:64:24:9f:ea:b0": -87 },
      { "GC_free_WiFi 94:64:24:a0:34:f0": -88 }
    ]
  },
  {
    "name": "4-14()",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:e2": -86 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -60 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -64 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -80 },
      { "GC_free_WiFi 94:64:24:9e:8a:72": -67 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -58 },
      { "GC_free_WiFi 94:64:24:9e:72:d2": -66 },
      { "GC_free_WiFi 94:64:24:9f:83:72": -76 },
      { "GC_free_WiFi 94:64:24:9f:ea:b0": -80 },
      { "GC_free_WiFi 94:64:24:a0:34:d0": -84 }
    ]
  },
  {
    "name": "4-15(419)",
    "point": [
      { "GC_free_WiFi 94:64:24:9f:03:e2": -88 },
      { "GC_free_WiFi 94:64:24:9f:12:20": -82 },
      { "GC_free_WiFi 94:64:24:9f:45:e0": -84 },
      { "GC_free_WiFi 94:64:24:9e:3f:00": -82 },
      { "GC_free_WiFi 94:64:24:a0:1f:90": -82 },
      { "GC_free_WiFi 94:64:24:a1:6f:92": -67 },
      { "GC_free_WiFi 94:64:24:9e:8a:92": -58 },
      { "GC_free_WiFi 94:64:24:9e:72:f2": -50 },
      { "GC_free_WiFi 94:64:24:9f:fb:32": -79 },
      { "GC_free_WiFi 94:64:24:a1:22:80": -89 },
      { "GC_free_WiFi 94:64:24:9f:c4:42": -87 },
      { "GC_free_WiFi 94:64:24:a0:fe:e0": -67 },
      { "GC_free_WiFi 94:64:24:9f:83:92": -69 },
      { "GC_free_WiFi 94:64:24:9e:8a:72": -62 },
      { "GC_free_WiFi 94:64:24:a1:6f:72": -65 },
      { "GC_free_WiFi 94:64:24:9e:72:d2": -62 },
      { "GC_free_WiFi 94:64:24:9f:ea:b0": -77 },
      { "GC_free_WiFi 94:64:24:9d:f1:32": -85 },
      { "GC_free_WiFi 94:64:24:a0:34:f0": -74 },
      { "GC_free_WiFi 94:64:24:a0:34:d0": -75 },
      { "GC_free_WiFi 94:64:24:9e:2c:e2": -68 },
      { "GC_free_WiFi 94:64:24:a1:00:c2": -89 }
    ]
  }
]


def convert_dataset_data(dataset):
    converted_dataset = []

    for data in dataset:
        name = data['name']
        points = data['point']
        converted_points = []

        for point in points:
            mac = list(point.keys())[0]
            rssi = list(point.values())[0]
            converted_points.append({'mac': mac, 'rssi': rssi})

        converted_dataset.append((name, converted_points))

    return converted_dataset


def convert_input(input_list):
  output = {"data": []}

  for item in input_list:
    print(item)
    mac_address, rssi = list(item.items())[0]
    mac_address = mac_address.split()[1]
    output["data"].append({"mac": mac_address, "rssi": int(rssi)})

  return output


# 주어진 dataset을 변환합니다.
converted_dataset = convert_dataset_data(old_data)

# 변환된 dataset을 JSON 형식으로 출력합니다.
converted_json = json.dumps(converted_dataset)
print(converted_json)






inputs = [
  { "GC_free_WiFi 94:64:24:9f:03:c2": "-79" },
  { "GC_free_WiFi 94:64:24:9f:03:e2": "-78" },
  { "GC_free_WiFi 94:64:24:9f:12:00": "-67" },
  { "GC_free_WiFi 94:64:24:9f:12:20": "-61" },
  { "GC_free_WiFi 94:64:24:9f:45:e0": "-68" },
  { "GC_free_WiFi 94:64:24:9e:3f:00": "-56" },
  { "GC_free_WiFi 94:64:24:9f:45:c0": "-76" },
  { "GC_free_WiFi 94:64:24:a0:1f:90": "-63" },
  { "GC_free_WiFi 94:64:24:9e:05:72": "-89" },
  { "GC_free_WiFi 94:64:24:a1:6f:92": "-74" },
  { "GC_free_WiFi 94:64:24:9e:8a:92": "-81" },
  { "GC_free_WiFi 94:64:24:9e:72:f2": "-83" },
  { "GC_free_WiFi 94:64:24:9f:c4:42": "-89" },
  { "GC_free_WiFi 94:64:24:a0:fe:e0": "-90" },
  { "GC_free_WiFi 94:64:24:9e:3e:e0": "-57" },
  { "GC_free_WiFi 94:64:24:a0:1f:70": "-59" },
  { "GC_free_WiFi 94:64:24:9f:83:92": "-87" },
  { "GC_free_WiFi 94:64:24:9e:8a:72": "-86" },
  { "GC_free_WiFi 94:64:24:a1:6f:72": "-79" }
]

# 주어진 input을 변환합니다.
converted_input = convert_input(inputs)

# 변환된 input을 JSON 형식으로 출력합니다.
converted_json = json.dumps(converted_input)
print(converted_json)