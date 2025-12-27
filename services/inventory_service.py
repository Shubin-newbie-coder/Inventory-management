from database import get_connection

class InventoryService:

    def add_product(self, product):
        conn = get_connection()
        cur = conn.cursor()

        query = """
        INSERT INTO products (name, price, quantity)
        VALUES (%s, %s, %s)
        """
        cur.execute(query, (product.name, product.price, product.quantity))
        conn.commit()

        cur.close()
        conn.close()

    def get_all_products(self):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, name, price, quantity FROM products")
        products = cur.fetchall()

        cur.close()
        conn.close()
        return products

    def delete_product(self, product_id):
        conn = get_connection()
        cur = conn.cursor()

        cur.execute("DELETE FROM products WHERE id = %s", (product_id,))
        conn.commit()

        cur.close()
        conn.close()
