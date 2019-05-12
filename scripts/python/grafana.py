#! /usr/bin/env python
# coding=UTF-8

import urllib
import urllib2
import json


def _get_metric_sum():
    api_url = u"http://10.3.204.91:4242/api/query?start=1508342400&end=1508428800&m=sum:1h-sum:durian.adx.bidding.throughput"
    req = urllib2.Request(url=api_url)
    resp = urllib2.urlopen(req)
    resp_data = json.loads(resp.read())
    print("--> %s" % resp_data)
    dps_data = resp_data[0]['dps']
    for key in dps_data.keys():
        print("--> %s, %s" %(key, dps_data[key]))

    vs = tuple(dps_data.values())
    print("values: type: %s, value: %s" % (type(vs), vs))
    dps_total = reduce(lambda x,y: x+y, vs)

    print("--> %s" % dps_total)

if __name__ == "__main__":
    #_get_metric_sum() 
   
    sss = Person()
    sss.set('name', 'ljx')
    print("--> %s" % sss.name)
