import grpc
import mapstorage_api_pb2
import mapstorage_api_pb2_grpc
import testdata_load

def run():
    "The run method, that sends gRPC conformant messsages to the server"

    with grpc.insecure_channel("localhost:9999") as channel:
        stub = mapstorage_api_pb2_grpc.MapExporterStub(channel)
        while True:
            try:
                response = stub.importCampus(testdata_load.data())
                #print(response)
                return response.requestId
            except KeyboardInterrupt:
                print("KeyboardInterrupt")
                channel.unsubscribe(close)
                exit()


def close(channel):
    "Close the channel"
    channel.close()


if __name__ == "__main__":
    run()