from concurrent import futures
import threading
import time
import grpc
import mapstorage_api_pb2
import mapstorage_api_pb2_grpc
import testdata_load


class Listener(mapstorage_api_pb2_grpc.MapExporterServicer):

    def __init__(self):
        self.requestId = 0
        self.last_print_time = time.time()

    def __str__(self):
        return self.__class__.__name__

    def exportCampus(self,request, context):
        return mapstorage_api_pb2.CampusExport(campus=testdata_load.data())

    def importCampus(self, request, context):
        self.requestId += 1
        if self.requestId > 1000:
            print("1000 calls in %3f seconds" % (time.time() - self.last_print_time))
            self.last_print_time = time.time()
            self.requestId = 0
        return mapstorage_api_pb2.CampusImport(report='Successfully imported new Campus', requestId=str(self.requestId))

    def exportUnassignedGateways(self, request, context):
        self.requestId += 1
        if self.requestId > 1000:
            print("1000 calls in %3f seconds" % (time.time() - self.last_print_time))
            self.last_print_time = time.time()
            self.requestId = 0
        return mapstorage_api_pb2.UnassignedGateways(gatewayCode="f84983f78f4e", requestId=str(self.requestId))


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=50))
    mapstorage_api_pb2_grpc.add_MapExporterServicer_to_server(Listener(), server)
    server.add_insecure_port("[::]:9999")
    server.start()
    try:
        while True:
            print("Server Running : threadcount %i" % (threading.active_count()))
            time.sleep(10)
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        server.stop(0)


if __name__ == "__main__":
    serve()