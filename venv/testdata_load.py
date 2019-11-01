import mapstorage_api_pb2

def data():
    campus = mapstorage_api_pb2.Campus()

    gatewayPosition = mapstorage_api_pb2.GatewayPosition()

    gatewayPosition.code = '1'

    site = mapstorage_api_pb2.Site()

    site.id = '2'
    site.name = 'hospital'
    site.type = 12

    room = mapstorage_api_pb2.Room()

    room.id = '3'
    room.name = 'clin'
    room.type = 13
    room.sites.append(site)
    room.gatewayPositions.append(gatewayPosition)

    ward = mapstorage_api_pb2.Ward()

    ward.id = '14'
    ward.name = 'sergery'
    ward.rooms.append(room)

    floor = mapstorage_api_pb2.Floor()

    floor.id = '15'
    floor.name = 'OG'
    floor.level = 15
    floor.roomsWithoutWard.append(room)
    floor.wards.append(ward)

    building = mapstorage_api_pb2.Building()
    building.id = '16'
    building.name = 'a1'
    building.floors.append(floor)

    campus.id = '17'
    campus.organizationCode = '117'
    campus.name = 'a17'
    campus.code = '1711'
    campus.buildings.append(building)
    return campus

def campusexport():

    campus_export = mapstorage_api_pb2.CampusExport
    campus_export.requestId = '1'
    campus_export.Campus = data()
    return campus_export, campus_export.requestId

def campus_input():
    campus_input = mapstorage_api_pb2.CampusInput().code = '1711'
    return campus_input
