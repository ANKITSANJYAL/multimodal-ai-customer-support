from neo4j import GraphDatabase

class Neo4jConnector:
    """
    Connector for Neo4j database.
    """
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def get_product_info(self, product_id):
        """
        Retrieve product information from Neo4j.
        """
        with self.driver.session() as session:
            result = session.run(
                "MATCH (p:Product {id: $product_id}) RETURN p.name, p.warranty",
                product_id=product_id
            )
            return result.single()

# Example usage
if __name__ == "__main__":
    connector = Neo4jConnector("bolt://localhost:7687", "neo4j", "password")
    print(connector.get_product_info("123"))