{
    "Records": [{
        "cos": {
            "cosSchemaVersion": "1.0",
            "cosObject": {
                "url": "http://testpic-1253970026.cos.ap-guangzhou.myqcloud.com/testfile",
                "meta": {
                    "x-cos-request-id": "NWMxOWY4MGFfMjViMjU4NjRfMTUyMV8yNzhhZjM=",
                    "Content-Type": ""
                },
                "vid": "",
                "key": "/1253970026/testpic/testfile",
                "size": 1029
            },
            "cosBucket": {
                "region": "gz",
                "name": "testpic",
                "appid": "1253970026"
            },
            "cosNotificationId": "unkown"
        },
        "event": {
            "eventName": "cos:ObjectCreated:Post",
            "eventVersion": "1.0",
            "eventTime": 1545205770,
            "eventSource": "qcs::cos",
            "requestParameters": {
                "requestSourceIP": "59.37.125.38",
                "requestHeaders": {
                    "Authorization": "q-sign-algorithm=sha1&q-ak=AKIDQm6iUh2NJ6jL41tVUis9KpY5Rgv49zyC&q-sign-time=1545205709;1545215769&q-key-time=1545205709;1545215769&q-header-list=host;x-cos-storage-class&q-url-param-list=&q-signature=098ac7dfe9cf21116f946c4b4c29001c2b449b14"
                }
            },
            "eventQueue": "qcs:0:lambda:cd:appid/1253970026:default.printevent.$LATEST",
            "reservedInfo": "",
            "reqid": 179398952
        }
    }]
}