from app.core.rate_limiter import RateLimiter


def test_rate_limit():
    limiter = RateLimiter(limit=2)

    ip = "1.1.1.1"

    assert limiter.allow_request(ip)
    assert limiter.allow_request(ip)
    assert not limiter.allow_request(ip)