def stream_response(response):

    for chunk in response:

        if chunk.choices:

            delta = chunk.choices[0].delta

            if delta.content:

                yield delta.content