from src.sdn_controller import SDNRoutingController

def run_sdn_demo():
    controller = SDNRoutingController()
    
    # Construct network mesh topology (Core, Edge, Access switches)
    controller.add_link("Switch_A", "Switch_B", latency_ms=2.5, bandwidth_gbps=10.0)
    controller.add_link("Switch_B", "Switch_C", latency_ms=15.0, bandwidth_gbps=1.0) # High latency link
    controller.add_link("Switch_A", "Switch_D", latency_ms=3.0, bandwidth_gbps=10.0)
    controller.add_link("Switch_D", "Switch_C", latency_ms=4.0, bandwidth_gbps=10.0)

    print("\n=============================================")
    print("      SDN OPTIMAL ROUTE CONTROLLER           ")
    print("=============================================\n")
    
    source, dest = "Switch_A", "Switch_C"
    optimal_path, cost = controller.calculate_optimal_path(source, dest)
    
    print(f"Routing Request: {source} ➔ {dest}")
    print(f"Computed SDN Path:  {' ➔ '.join(optimal_path)}")
    print(f"Path Metric Cost:   {cost}")

if __name__ == "__main__":
    run_sdn_demo()
  
