class StatusCode():
    OK = 200
    BAD_REQUEST = 400
    UNAUTHORIZED = 401
    FORBIDDEN = 403
    NOT_FOUND = 404
    INTERNAL_SERVER_ERROR = 500
    
class ClientUrls():
    # TODO: Change this to prod url or set based on env
    VERIFIED_PAGE = 'http://localhost:3000/verified'