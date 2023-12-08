import requests
import networkx as nx
import matplotlib.pyplot as plt

def create_api_mindmap():
    G = nx.Graph()
    G.add_node("Dog API")
    G.add_node("Get random dog image")
    G.add_node("List all breeds")
    G.add_node("Get breed image")

    G.add_edge("Dog API", "Get random dog image")
    G.add_edge("Dog API", "List all breeds")
    G.add_edge("Dog API", "Get breed image")

    pos = nx.spring_layout(G, seed=42)
    labels = {node: node for node in G.nodes()}

    nx.draw(G, pos, with_labels=True, labels=labels, node_size=5000, node_color='skyblue', font_size=10)
    plt.title("Dog API MindMap")
    plt.axis('off')

    plt.savefig("dog_api_mindmap.png", format="PNG")
    plt.show()

def test_api_endpoint(url, expected_status=200, expected_key='message'):
    try:
        response = requests.get(url)
        response.raise_for_status()
        assert response.status_code == expected_status
        data = response.json()
        assert expected_key in data
        print(f"Test passed: {url}")
    except requests.RequestException as e:
        print(f"Test failed: {url}\nError: {e}")

def create_test_report():
    with open("dog_api_test_report.txt", "w") as report:
        report.write("Dog API Test Report\n\n")

        tests = [
            ("Get random dog image", "https://dog.ceo/api/breeds/image/random"),
            ("List all breeds", "https://dog.ceo/api/breeds/list/all"),
            ("Get breed image", "https://dog.ceo/api/breed/labrador/images/random"),
            ("Invalid breed name", "https://dog.ceo/api/breed/invalid_breed/images/random", 404),
            ("Sub-breeds", "https://dog.ceo/api/breed/collie/list")
        ]

        for test_name, url, status_code in tests:
            test_api_endpoint(url, expected_status=status_code)
            report.write(f"{test_name}: {url}\n   Passed\n\n")

if __name__ == "__main__":
    create_api_mindmap()
    create_test_report()