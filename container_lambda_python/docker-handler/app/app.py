def handler(event, context):
    if event:
        print(event)
    else:
        print("no event found")

    return "container-lambda-python completed."
