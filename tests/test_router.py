import pytest
from src.sdn_controller import SDNRoutingController

def test_sdn_shortest_path():
    controller = SDNRoutingController()
    controller.add_link("R1", "R2", latency_ms=10.0, bandwidth_gbps=1.0)
    controller.add_link("R2", "R3", latency_ms=10.0, bandwidth_gbps=1.0)
    controller.add_link("R1", "R3", latency_ms=5.0, bandwidth_gbps=10.0)
    
    path, cost = controller.calculate_optimal_path("R1", "R3")
    assert path == ["R1", "R3"]

def test_missing_node_exception():
    controller = SDNRoutingController()
    with pytest.raises(ValueError):
        controller.calculate_optimal_path("R1", "R99")
      
