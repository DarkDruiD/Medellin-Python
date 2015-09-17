import sys
import json
import time
import random
import uav_pb2


if __name__ == '__main__':

    pb_str = open('pb.txt', 'r+b').read()
    js_str = open('js.txt', 'r+b').read()

    js_s_t = time.time()
    js_dec = json.loads(js_str)
    js_f_t = time.time()
    js_del = js_f_t - js_s_t


    dr_pkg = uav_pb2.DronePackage()

    pb_s_t = time.time()
    pb_dec = dr_pkg.ParseFromString(pb_str)
    pb_f_t = time.time()
    pb_del = pb_f_t - pb_s_t

    print "JSON object decodes in {}".format(js_del)
    print "Protocol Buffer decodes in {}".format(pb_del)
