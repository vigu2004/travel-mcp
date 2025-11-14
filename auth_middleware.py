import jwt
from jwt import PyJWKClient

class Auth0JWTMiddleware:
    """
    Simple callable middleware for FastMCP 0.4.x
    FastMCP will call: auth(token_str)
    """

    def __init__(self, domain: str, audience: str):
        self.issuer = f"https://{domain}/"
        self.audience = audience
        self.jwks_url = f"{self.issuer}.well-known/jwks.json"
        self.jwk_client = PyJWKClient(self.jwks_url)

    def __call__(self, token: str):
        """FastMCP calls this for authentication."""
        try:
            signing_key = self.jwk_client.get_signing_key_from_jwt(token)

            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=self.audience,
                issuer=self.issuer
            )

            return payload   # Auth0 user data

        except Exception as e:
            raise PermissionError(f"Invalid Auth0 JWT: {e}")
