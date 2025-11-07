# No more os.add_dll_directory needed!
# Conda takes care of it.
import opensim as osim
import math
import os

print(f"✅ Successfully imported opensim version: {osim.GetVersion()}")

# --- 1. Load Your Model ---
model_filename = "biceps_curl_model.osim"

    
# Load the model you created
model = osim.Model("../models/biceps_curl_model.osim")
    
# --- 2. Add an External Force (The "Dumbbell") ---
dumbbell_torque = osim.Constant(30.0) 
elbow_joint = model.getCoordinateSet().get("r_elbow_flex")
torque_actuator = osim.CoordinateActuator()
torque_actuator.setCoordinate(elbow_joint)
torque_actuator.setOptimalForce(1.0)
torque_actuator.setName("dumbbell_torque")
model.addForce(torque_actuator)

dumbbell_torque = osim.Constant(30.0) 
dumbbell_torque.setName("DumbbellControlSignal") # Optional: give it a name
model.addComponent(dumbbell_torque) # Add the constant to the model hierarchy

model.updComponent("dumbbell_torque").connectInput_control(dumbbell_torque.getOutput("output"))

# --- 3. Setup the Simulation ---
state = model.initSystem()
elbow_joint.setValue(state, 0.0)
    
# --- 4. Run a Forward Dynamics Simulation ---
print("\nRunning Forward Dynamics simulation...")
manager = osim.Manager(model)
manager.setInitialTime(0.0)
manager.setFinalTime(1.0) # Simulate for 1 second
    
state.setTime(0.0)
manager.integrate(state)
    
# --- 5. Get and Print Results ---
final_angle_rad = elbow_joint.getValue(state)
final_angle_deg = math.degrees(final_angle_rad)
    
print("\n--- Simulation Complete ---")
print(f"Final Time: {state.getTime()} s")
print(f"Final Elbow Angle: {final_angle_deg:.2f} degrees")