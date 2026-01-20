import json
from http.server import HTTPServer
from request_handler import HandleRequests, status


# Add your imports below this line
from views import create_user, login_user


class JSONServer(HandleRequests):
    """Server class to handle incoming HTTP requests for Rare Publishing API"""

    def do_POST(self):
        """Handle POST requests from a client"""

        response_body = ""
        url = self.parse_url(self.path)

        content_len = int(self.headers.get("content-length", 0))
        request_body = self.rfile.read(content_len)
        request_body = json.loads(request_body)

        if url["requested_resource"] == "register":
            response_body = create_user(request_body)
            return self.response(response_body, status.HTTP_201_SUCCESS_CREATED.value)
        elif url["requested_resource"] == "login":
            response_body = login_user(request_body)
            return self.response(response_body, status.HTTP_200_SUCCESS.value)

        return self.response(
            response_body, status.HTTP_400_CLIENT_ERROR_BAD_REQUEST_DATA.value
        )


#
# THE CODE BELOW THIS LINE IS NOT IMPORTANT FOR REACHING YOUR LEARNING OBJECTIVES
#
def main():
    host = ""
    port = 8088
    HTTPServer((host, port), JSONServer).serve_forever()


if __name__ == "__main__":
    main()
