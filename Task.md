Prompt:

As Mozio expands internationally, we have a growing problem that many transportation suppliers would like their API to be integrated into Mozio platform, to allow them to sell their transfers.

Integrating many APIs from scratch and selling their content in a unified approach is not a simple task and Mozio built its own Transfers Framework to facilitate that. Nevertheless, we still need to check the supplier's API documentation, communicate with them and integrate their code into our framework.

To assess your API knowledge, we would like you to implement Mozio API to handle the core methods that we have available. You can see the API working (under the hood, inspecting the requests made on the Network tab) on our testing website. 

Requirement:

    Read Mozio API Integration guide
    Implement Python methods to do search, booking (reservation) and cancellation;
    Do one booking with the following search parameters, cancel it, and share its confirmation number:

    {
      "start_address": "44 Tehama Street, San Francisco, CA, USA",
      "end_address": "SFO",
      "mode": "one_way",
      "pickup_datetime": "2023-12-01 15:30",
      "num_passengers": 2,
      "currency": "USD",
      "campaign": "{your full name}"
    }

                For the reservation, select the provider with the name "Dummy External Provider", and pick the cheapest vehicle available.

    Create a Github account (if you don’t have one), push all your code, and share the link with us;

 

Considerations - API Integration:

    API KEY to use: 6bd1e15ab9e94bb190074b4209e6b6f9
    Mozio API endpoints that should be implemented:

        POST /v2/search/
        GET /v2/search/{search_id}/poll/
        POST /v2/reservations/
        GET /v2/reservations/{search_id}/poll/
        DELETE /v2/reservations/{confirmation_number}
    No need to inform any payment information for the booking flow;

 

Considerations - General:

    All of this should be built in Python;
    Use any extra libraries you think will help;
    Ensure that your code is clean, follows standard PEP8 style (though you can use 120 characters per line) and has comments where appropriate;
    We will not look at any attachments, screenshots or files sent by you, only Github.

 

Best of luck!