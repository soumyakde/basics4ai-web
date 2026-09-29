"""Static file server for the Basics4AI research site.

A thin wrapper around http.server that adds a Cache-Control header to
every response. Plain http.server sends none at all, so browsers fall
back to heuristic caching and can keep serving a stale page/asset to a
returning visitor long after a deploy changes it. "no-cache" still lets
the browser cache the response, but forces a revalidation (a cheap
conditional GET) on every use, so updates are always picked up.
"""
import os
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer


class NoCacheHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header("Cache-Control", "no-cache")
        super().end_headers()


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    ThreadingHTTPServer(("0.0.0.0", port), NoCacheHandler).serve_forever()
