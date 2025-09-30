"""Simple web server exposing Docker command references."""
from __future__ import annotations

import argparse
import http.server
import socketserver
from typing import Iterable

DOCKER_COMMANDS = [
    {
        "title": "ตรวจสอบเวอชั่นของ Docker",
        "command": "docker version",
        "description": "Show the version of Docker installed on the machine.",
    },
    {
        "title": "ตรวจสอบ images ในเครื่องของเรา",
        "command": "docker images",
        "description": "List Docker images that are currently stored locally.",
    },
    {
        "title": "ลบ images ในเครื่องของเรา",
        "command": "docker image rm [OPTIONS] IMAGE [IMAGE...]",
        "description": "Remove one or more Docker images from the local image cache.",
    },
    {
        "title": "ตรวจสอบรายละเอียดเพิ่มเติม",
        "command": "docker inspect <container name>",
        "description": "Display low-level details about a specific container or image.",
    },
    {
        "title": "แสดงรายการ container",
        "command": "docker ps -a",
        "description": "List all Docker containers, including stopped ones.",
    },
    {
        "title": "ตรวจสอบ volume",
        "command": "docker volume ls",
        "description": "List Docker volumes available on the host.",
    },
    {
        "title": "ลบ volume",
        "command": "docker volume rm <volume name>",
        "description": "Remove a Docker volume by name.",
    },
    {
        "title": "สั่งเริ่มการทำงานcontainer จาก container id",
        "command": "docker start <container id>",
        "description": "Start an existing Docker container using its ID or name.",
    },
    {
        "title": "หยุดการทำงาน container จาก container id",
        "command": "docker stop <container id>",
        "description": "Stop a running Docker container by ID or name.",
    },
    {
        "title": "ลบ container จาก container id",
        "command": "docker rm <container id>",
        "description": "Remove a Docker container from the host using its ID or name.",
    },
]


def build_command_list(commands: Iterable[dict[str, str]]) -> str:
    """Return HTML representing the command list."""
    items = []
    for entry in commands:
        items.append(
            f"""
            <article class=\"command\">
                <h2>{entry['title']}</h2>
                <pre><code>{entry['command']}</code></pre>
                <p>{entry['description']}</p>
            </article>
            """
        )
    return "\n".join(items)


def build_page(commands: Iterable[dict[str, str]]) -> bytes:
    """Build the full HTML page that will be served."""
    command_list = build_command_list(commands)
    html = f"""
    <!DOCTYPE html>
    <html lang=\"en\">
        <head>
            <meta charset=\"utf-8\" />
            <title>Docker Command Reference</title>
            <style>
                body {{
                    font-family: system-ui, -apple-system, BlinkMacSystemFont, \
                                 'Segoe UI', sans-serif;
                    margin: 0;
                    padding: 2rem;
                    background-color: #0f172a;
                    color: #e2e8f0;
                }}

                header {{
                    margin-bottom: 2rem;
                }}

                h1 {{
                    font-size: 2.5rem;
                    margin-bottom: 0.25rem;
                }}

                p.lead {{
                    margin-top: 0;
                    color: #cbd5f5;
                }}

                main {{
                    display: grid;
                    gap: 1.5rem;
                }}

                .command {{
                    background: rgba(15, 23, 42, 0.6);
                    border: 1px solid rgba(148, 163, 184, 0.2);
                    border-radius: 12px;
                    padding: 1.25rem;
                    box-shadow: 0 10px 30px rgba(15, 23, 42, 0.35);
                }}

                pre {{
                    background: rgba(15, 23, 42, 0.85);
                    padding: 0.75rem;
                    border-radius: 8px;
                    overflow-x: auto;
                }}

                code {{
                    font-family: 'Fira Code', 'SFMono-Regular', Consolas, 'Liberation Mono', monospace;
                    font-size: 0.95rem;
                    color: #38bdf8;
                }}

                @media (min-width: 768px) {{
                    main {{
                        grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
                    }}
                }}
            </style>
        </head>
        <body>
            <header>
                <h1>Docker Command Reference</h1>
                <p class=\"lead\">A quick reference for frequently-used Docker commands.</p>
            </header>
            <main>
                {command_list}
            </main>
        </body>
    </html>
    """
    return html.encode("utf-8")


class DockerCommandHandler(http.server.SimpleHTTPRequestHandler):
    """Serve the Docker command reference page regardless of the path."""

    def do_GET(self) -> None:  # noqa: N802 - method name required by BaseHTTPRequestHandler
        if self.path not in {"/", "/index.html"}:
            self.send_error(404, "File not found")
            return

        body = build_page(DOCKER_COMMANDS)
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Serve a Docker command reference web page.")
    parser.add_argument("--host", default="0.0.0.0", help="Host/IP address to bind the server to.")
    parser.add_argument("--port", type=int, default=8000, help="Port number to listen on.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    with socketserver.TCPServer((args.host, args.port), DockerCommandHandler) as httpd:
        print(f"Serving Docker command reference at http://{args.host}:{args.port}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nShutting down server...")


if __name__ == "__main__":
    main()
