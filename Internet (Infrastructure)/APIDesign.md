# API Design

## REST
- clients do not construct URLs from other information—they just use the URLs that are passed out by the server as-is
- does not construct the URLs it uses from piece parts, and it does not understand the website-specific formats of the URLs it uses
e.g.,
```
POST /accounts <headers> (username, contact_email, password)> -> account_URL
POST /subscriptions <headers> (account_URL, subscription_type) -> subscription_URL
POST /activation-reminder-outbox <headers> (account_URL) -> email_URL
POST /cancellations <headers> (subscription_URL, reason, immediate=True) -> cancellaton_URL
GET {account_URL} ->  {full data tree}
```

## gRPC
- gRPC-generated stubs and skeletons hide HTTP from the client and server too, so nobody has to worry how the RPC concepts are mapped to HTTP—they just have to learn gRPC. 

The way a client uses a gRPC API is by following these three steps:

1. Decide which procedure to call
2. Calculate the parameter values to use (if any)
3. Use a code-generated stub to make the call, passing the parameter values

e.g.,
```
createAccount(username, contact_email, password) -> account_id
addSubscription(account_id, subscription_type) -> subscription_id
sendActivationReminderEmail(account_id) -> null
cancelSubscription(subscription_id, reason, immediate=True) -> null
getAccountDetails(account_id) -> {full data tree}
```
## OpenAPI (formerly swagger)
- clients use the API by constructing URLs from other information. The way a client uses an OpenAPI API is by following these three steps:

1. Decide which OpenAPI URL path template to use
2. Calculate the parameter values to use (if any)
3. Plug the parameter values into the URL path template and send an HTTP request.

e.g.,
```
paths:
  /pets/{petId}:
    get:
      operationId: getPetById
      parameters:
        - name: petId
          in: path
          required: true
          description: The id of the pet to retrieve
          schema:
            type: string
```