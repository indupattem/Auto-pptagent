from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("search")


@mcp.tool()
def search_topic(query: str) -> str:
    try:
        url = "https://en.wikipedia.org/api/rest_v1/page/summary/" + query.replace(" ", "_")

        response = requests.get(url, timeout=5)
        data = response.json()

        if "extract" in data:
            text = data["extract"]

            # Split into meaningful lines
            sentences = text.split(". ")

            # Return 6–7 lines
            points = [s.strip() for s in sentences if len(s) > 20][:7]

            return "\n".join(points)

        else:
            return f"No data found for {query}"

    except Exception as e:
        return f"Error fetching data for {query}"
    

if __name__ == "__main__":
    mcp.run()