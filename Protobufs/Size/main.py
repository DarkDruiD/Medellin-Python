import sys
import json
import time
import random
import uav_pb2


def read_gps_ptrb():
    gps = uav_pb2.GPS()

    gps.time_stamp = time.strftime("%H:%M:%S")
    gps.longitude = random.randint(0, 360)
    gps.latitude = random.randint(0, 360)

    return gps


def read_height_ptrb():
    height = uav_pb2.Height()

    height.time_stamp = time.strftime("%H:%M:%S")
    height.height = random.randint(0, 100)

    return height


def read_gyro_ptrb():
    gyro = uav_pb2.Gyroscope()

    gyro.time_stamp = time.strftime("%H:%M:%S")
    gyro.pitch = random.randint(0, 100)
    gyro.roll = random.randint(0, 100)

    return gyro


def read_accel_ptrb():
    accel = uav_pb2.Accelerometer()

    accel.time_stamp = time.strftime("%H:%M:%S")
    accel.x = random.randint(0, 100)
    accel.y = random.randint(0, 100)
    accel.z = random.randint(0, 100)

    return accel


def build_drone_ptrb():
    drn_pkg = uav_pb2.DronePackage()

    drn_pkg.time_stamp = time.strftime("%H:%M:%S")
    drn_pkg.gps.CopyFrom(read_gps_ptrb())
    drn_pkg.height.CopyFrom(read_height_ptrb())
    drn_pkg.gyro.CopyFrom(read_gyro_ptrb())
    drn_pkg.accel.CopyFrom(read_accel_ptrb())

    return drn_pkg


def read_gps_js():
    gps = {}

    gps["time_stamp"] = time.strftime("%H:%M:%S")
    gps["longitude"] = random.randint(0, 360)
    gps["latitude"] = random.randint(0, 360)

    return gps


def read_height_js():
    height = {}

    height["time_stamp"] = time.strftime("%H:%M:%S")
    height["height"] = random.randint(0, 100)

    return height


def read_gyro_js():
    gyro = {}

    gyro["time_stamp"] = time.strftime("%H:%M:%S")
    gyro["pitch"] = random.randint(0, 100)
    gyro["roll"] = random.randint(0, 100)

    return gyro


def read_accel_js():
    accel = {}

    accel["time_stamp"] = time.strftime("%H:%M:%S")
    accel["x"] = random.randint(0, 100)
    accel["y"] = random.randint(0, 100)
    accel["z"] = random.randint(0, 100)

    return accel


def build_drone_js():
    drn_pkg = {}

    drn_pkg["time_stamp"] = time.strftime("%H:%M:%S")
    drn_pkg["gps"] = read_gps_js()
    drn_pkg["height"] = read_height_js()
    drn_pkg["gyro"] = read_gyro_js()
    drn_pkg["accel"] = read_accel_js()

    return drn_pkg


if __name__ == '__main__':
    js_size = sys.getsizeof(json.dumps(build_drone_js()))
    pb_size = sys.getsizeof(build_drone_ptrb().SerializeToString())

    print "{} size of the JSON object".format(js_size)
    print "{} size of the Protocol Buffer object".format(pb_size)
    print "The Protocol Buffer is {} times smaller than the JSON".format(js_size/float(pb_size))
