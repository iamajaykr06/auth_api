from flask import jsonify

class APIError(Exception):
    def __init__(self, message, status_code=400):
        self.message = message
        self.status_code = status_code
        super().__init__(message)


def register_error_handlers(app):

    @app.errorhandler(APIError)
    def handle_api_error(error):
        return jsonify({
            "error": error.message
        }), error.status_code

    @app.errorhandler(404)
    def handle_404(error):
        return jsonify({
            "error": "Not Found"
        }), 404

    @app.errorhandler(Exception)
    def handle_500(error):
        # IMPORTANT: don't swallow APIError
        if isinstance(error, APIError):
            return handle_api_error(error)

        return jsonify({
            "error": "Internal Server Error"
        }), 500
