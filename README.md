# Digital Dumbbell Project: Torque Profile Optimization for Biceps Curl

This project aims to design optimal torque resistance profiles, $\tau(\theta, \omega)$, for a robotic/digital dumbbell to maximize training stimulus in the biceps muscle while adhering to joint safety limits.

---

## 1. Project Goal

The core objective is to use computational optimization within the OpenSim musculoskeletal simulator to find the parameters for a resistance function $\tau(\theta, \omega)$ that:

1.  **Maximizes** the integrated muscle activation (Training Stimulus) of the target muscles (Biceps/Brachialis).
2.  **Caps** the peak joint reaction forces at the elbow (Joint Load Constraint).
3.  **Obeys** the maximum torque output of the actuator (Actuator Limit Constraint).

The final optimized torque profile should result in a "smarter," safer, and more effective resistance curve than simple free weights.

---

## 2. Environment and Setup

The environment setup was completed using Conda to manage complex C++ dependencies.

### 2.1. Required Software

* **Anaconda / Miniconda**
* **OpenSim GUI (4.5)** (Required for model visualization and providing the underlying C++ libraries).
* **Visual Studio C++ 2015-2022 Redistributable (x64)** (Essential for C++ runtime dependencies).

### 2.2. Installation Process

The robust solution was to create a **pure `conda-forge` environment**:

```bash
# 1. Create and install all packages from conda-forge
conda create -n opensim_proj -c conda-forge python=3.8 opensim numpy

# 2. Activate the environment before running any scripts
conda activate opensim_proj

# 3. Inside <OPENSIM_INSTALL_DIR>/sdk/Python directory
python setup_win_python38.py

# 4. In the same directory
python -m pip install .

# 5. For testing the installation process
python
>>> import opensim as osim
>>> osim.GetVersionAndDate()
```

---

## 3. Troubleshooting and Known Errors

| Error Message | Cause | Solution |
| :--- | :--- | :--- |
| `ImportError: DLL load failed... _simbody` | **Missing C++ Runtime / Environment Mismatch.** Failed to link to the OpenSim core library. | 1. **Re-run Conda Setup** (Section 2). 2. Ensure **VC++ 2015-2022 Redistributable (x64)** is installed/repaired. |
| `RuntimeError: No object with name ...` | Coordinate name in script doesn't match name in the `.osim` file. | **Verify the Name:** Open the `.osim` file, search for `<Coordinate name="...`, and update the script to match exactly. |
| `TypeError: in method 'Component_addComponent'...` | Unreliable component addition method. | **Use `osim.PrescribedForce`** and its `setFunction()` method, which safely handles component ownership (current script design). |
| `[warning] Couldn't find file 'ground_ribs.vtp'.` | Missing visualization geometry files. | **Ignore this warning.** It does not affect physics or simulation results. |

---

## 4. Citation & Acknowledgment
If you use or extend this code, please cite:

@software{fattahi2025digitaldumbbell,  
  author = {Amirhossein Fattahi},  
  title = {Digital Dumbbell},  
  year = {2025},  
  url = {https://github.com/amirhossein-fattahi/digital-dumbbell}  
}

---

## 5. Contact
Amirhossein Fattahi  
M.Sc. Student – Control Systems Engineering

📧 Contact via GitHub Issues or direct email (see profile)
