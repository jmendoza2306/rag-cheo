import hashlib
import hmac

def verify_signature(payload_body: bytes, signature: str, verification_token: str) -> bool:
    """
    Verifies the webhook signature using the verification_token
    """
    if not signature or not signature.startswith("sha256="):
        return False

    expected_signature = signature[7:]  # Remove "sha256="

    # Calculate the expected signature using the verification_token
    computed_signature = hmac.new(
        verification_token.encode('utf-8'),
        payload_body,
        hashlib.sha256
    ).hexdigest()

    # Safe comparison
    return hmac.compare_digest(computed_signature, expected_signature)