from MozioClient import MozioClient
from api_helpers import search_url
mozio_client = MozioClient("6bd1e15ab9e94bb190074b4209e6b6f9")


data = {
    "start_address": "44 Tehama Street, San Francisco, CA, USA",
    "end_address": "SFO",
    "mode": "one_way",
    "pickup_datetime": "2023-09-01 15:00",
    "num_passengers": 2,
    "currency": "USD",
    "campaign": "Cristhian Ferreira"
}


# search_response = mozio_client.search(search_url, data)
# search_data = search_response.json()
# search_id = search_data.get("search_id")
# url = f"https://api-testing.mozio.com/v2/search/{search_id}/poll/"
# poll_search_response = mozio_client.poll_search(url)


# def get_result_id(result):
#     return result.get("result_id")


# results = poll_search_response.json()["results"]

# ids = list(map(get_result_id, results))

# for id in ids:
#     reservation_data = {
#         "search_id": search_id,
#         "result_id": id,
#         "email":"jon@mail.com",
#         "country_code_name": "US",
#         "phone_number": "8776668544",
#         "first_name": "Happy",
#         "last_name": "Traveler",
#         "airline": "AA",
#         "flight_number": "567",
#         "customer_special_instructions": "My doorbell is broken, please yell"
#     }

#     print(id)
#     create_reservations_url = "https://api-testing.mozio.com/v2/reservations/"
#     reservation_response = mozio_client.reservations(create_reservations_url,reservation_data )
#     print(reservation_response.json())


reservations_poll_url = "https://api-testing.mozio.com/v2/reservations/9c1f737406c84145a2a0b3d22398c848/poll/"


def get_reservetion_id(reservation):
  return reservation.get("id")

# response = mozio_client.reservations_poll(reservations_poll_url)

# reservation_ids = map(get_reservetion_id, response.json()["reservations"])
# print(list(reservation_ids))

url = "https://api-testing.mozio.com/v2/reservations/a0c11b9c7cf94d9ebb794f8a045c9d07/"

response = mozio_client.delete(url)
print(response.json())

# 8d956ff50264124dfaa83d8dc5e21775
# 2d52a9bc86cab317066d1329b68432ac