import grpc
import mapstorage_api_pb2
import mapstorage_api_pb2_grpc
import testdata_load

def run():

    with grpc.insecure_channel("localhost:9999") as channel:
        stub = mapstorage_api_pb2_grpc.MapExporterStub(channel)
        while True:
            try:
                response = stub.exportUnassignedGateways(mapstorage_api_pb2.CampusInput(code='1711'))
                #print(response)
                return response.requestId
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                exit()


def close(channel):

    channel.close()


if __name__ == "__main__":
    run()