import networkx as nx
import matplotlib.pyplot as plt

class ConnectionsManager:
    def __init__(self):
        self.graph = nx.Graph()

    def add_user(self, username):
        if username in self.graph:
            print(f"⚠️ User '{username}' already exists.")
        else:
            self.graph.add_node(username)
            print(f"✅ User '{username}' added successfully!")

    def add_connection(self, user1, user2):
        if user1 not in self.graph or user2 not in self.graph:
            print("⚠️ Both users must exist before creating a connection.")
        else:
            self.graph.add_edge(user1, user2)
            print(f"🔗 Connection created between {user1} and {user2}")

    def view_all_users(self):
        if not self.graph.nodes:
            print("⚠️ No users found.")
        else:
            print("\n👥 All Users:")
            for user in self.graph.nodes:
                print(f"- {user}")

    def view_all_connections(self):
        if not self.graph.edges:
            print("⚠️ No connections found.")
        else:
            print("\n🔗 All Connections:")
            for user1, user2 in self.graph.edges:
                print(f"- {user1} ↔ {user2}")

    def display_graph(self):
        if not self.graph.nodes:
            print("⚠️ No users to display.")
            return
        plt.figure(figsize=(6, 6))
        nx.draw(self.graph, with_labels=True, node_color='skyblue', node_size=1500, font_size=10, font_weight='bold')
        plt.title("Social Media Network Graph")
        plt.show()


def main():
    manager = ConnectionsManager()

    while True:
        print("\n=== SOCIAL MEDIA MANAGER MENU ===")
        print("1. Add User")
        print("2. Add Connection")
        print("3. View All Users")
        print("4. View All Connections")
        print("5. Display Network Graph")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            manager.add_user(username)

        elif choice == '2':
            user1 = input("Enter first username: ")
            user2 = input("Enter second username: ")
            manager.add_connection(user1, user2)

        elif choice == '3':
            manager.view_all_users()

        elif choice == '4':
            manager.view_all_connections()

        elif choice == '5':
            manager.display_graph()

        elif choice == '6':
            print("👋 Exiting Social Media Manager...")
            break

        else:
            print("⚠️ Invalid choice, try again.")


if __name__ == "__main__":
    main()
