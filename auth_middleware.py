# auth_middleware.py

import jwt
from jwt import PyJWKClient
from fastmcp import AuthMiddleware

class Auth0JWTMiddleware(AuthMiddleware):
    def __init__(self, domain: str, audience: str):
        self.issuer = f"https://{domain}/"
        self.audience = audience
        self.jwks_url = f"{self.issuer}.well-known/jwks.json"
        self.jwk_client = PyJWKClient(self.jwks_url)

    def authenticate(self, token: str):
        try:
            signing_key = self.jwk_client.get_signing_key_from_jwt(token)

            payload = jwt.decode(
                token,
                signing_key.key,
                algorithms=["RS256"],
                audience=self.audience,
                issuer=self.issuer
            )

            return payload  # valid Auth0 token

        except Exception as e:
            raise PermissionError(f"Invalid Auth0 JWT: {e}")
