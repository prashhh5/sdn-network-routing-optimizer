import networkx as nx
from typing import List, Tuple, Dict

class SDNRoutingController:
    """Software-Defined Networking topology controller for dynamic packet routing."""
    
    def __init__(self):
        self.topology = nx.Graph()

    def add_link(self, node1: str, node2: str, latency_ms: float, bandwidth_gbps: float):
        """Adds or updates a network link with weight based on latency and congestion."""
        # Cost metric inversely proportional to bandwidth, directly proportional to latency
        cost = latency_ms / max(0.1, bandwidth_gbps)
        self.topology.add_edge(node1, node2, weight=cost, latency=latency_ms, bandwidth=bandwidth_gbps)

    def calculate_optimal_path(self, source: str, destination: str) -> Tuple[List[str], float]:
        """Calculates shortest path using Dijkstra's algorithm based on cost weights."""
        if not self.topology.has_node(source) or not self.topology.has_node(destination):
            raise ValueError("Source or Destination node does not exist in topology.")
            
        path = nx.dijkstra_path(self.topology, source=source, target=destination, weight="weight")
        total_cost = nx.dijkstra_path_length(self.topology, source=source, target=destination, weight="weight")
        return path, round(total_cost, 2)
  
