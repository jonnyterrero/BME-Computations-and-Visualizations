"""
Biomedical Instrumentation Visualizations
Target Audience: Senior BME (Physics + CS minors)
Reference Sources: 
- Webster, "Medical Instrumentation: Application and Design"
- Northrop, "Analysis and Application of Analog Electronic Circuits..."

This script generates a 4-panel figure illustrating:
1. Source Impedance Loading (Skin-Electrode Interface)
2. Sensor Linearity (Thermistor vs. Piezoresistive Strain Gauge)
3. Common-Mode Rejection in an Instrumentation Amplifier (InAmp)
4. Fundamental Thermal (Johnson) Noise Limits
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as signal

# ============================================================================
# 1. SYNTHETIC ECG SIGNAL GENERATION
# ============================================================================
def generate_synthetic_ecg(t):
    """
    Generates a simplified synthetic ECG pulse using Gaussian distributions.
    Variables:
    t: time array (s)
    Returns: V_bio in Volts (V)
    """
    # P, Q, R, S, T wave parameters: (amplitude in V, center in s, width in s)
    # Peak amplitude ~1.0 mV (0.001 V) [Webster]
    waves = [
        (0.15e-3, 0.2, 0.02),   # P wave
        (-0.1e-3, 0.35, 0.01),  # Q wave
        (1.0e-3,  0.37, 0.015), # R wave
        (-0.2e-3, 0.40, 0.015), # S wave
        (0.3e-3,  0.55, 0.04)   # T wave
    ]
    v_bio = np.zeros_like(t)
    for amp, center, width in waves:
        v_bio += amp * np.exp(-0.5 * ((t - center) / width)**2)
    return v_bio

# Time vector: 0 to 1 second, sampled at 1000 Hz
fs = 1000.0 # Sampling frequency (Hz)
t = np.arange(0, 1.0, 1/fs) 
V_bio = generate_synthetic_ecg(t)

# ============================================================================
# PLOT SETUP
# ============================================================================
fig, axs = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('Biomedical Instrumentation: System Constraints & Models', fontsize=16, fontweight='bold')

# ============================================================================
# PANEL 1: SOURCE IMPEDANCE & LOADING EFFECTS
# Cross-link: Circuits I (Thevenin Equivalents & Voltage Dividers)
# ============================================================================
# The human skin acts as a high source impedance (Z_skin). 
# V_measured = V_bio * [Z_in / (Z_in + Z_skin)] + V_noise
Z_skin = 100e3 # Skin impedance (100 kOhms) [Webster]

# Case A: Poor amplifier design (low Z_in)
Z_in_bad = 50e3 # 50 kOhms
V_measured_bad = V_bio * (Z_in_bad / (Z_in_bad + Z_skin))

# Case B: Proper Biopotential Buffer (high Z_in)
Z_in_good = 10e6 # 10 MOhms
V_measured_good = V_bio * (Z_in_good / (Z_in_good + Z_skin))

axs[0, 0].plot(t, V_bio * 1000, 'k--', label='True V_{bio} (Ideal)')
axs[0, 0].plot(t, V_measured_good * 1000, 'g-', label=f'High Z_{{in}} (10 MΩ)')
axs[0, 0].plot(t, V_measured_bad * 1000, 'r-', label=f'Low Z_{{in}} (50 kΩ)')
axs[0, 0].set_title('Constraint: Skin-Electrode Source Loading')
axs[0, 0].set_xlabel('Time (s)')
axs[0, 0].set_ylabel('Amplitude (mV)')
axs[0, 0].legend()
axs[0, 0].grid(True)

# ============================================================================
# PANEL 2: SENSOR LINEARITY (THERMISTOR VS STRAIN GAUGE)
# ============================================================================
# Thermistor (Nonlinear): R(T) = R_0 * exp(beta * (1/T - 1/T_0))
# T is absolute temperature (K), R is resistance (Ohms)
T_celsius = np.linspace(20, 50, 100) # Physiological range and beyond
T_kelvin = T_celsius + 273.15
T_0 = 25 + 273.15 # Reference temp (298.15 K)
R_0 = 10e3        # Resistance at T_0 (10 kOhms)
beta = 3900       # Material constant (K)

R_thermistor = R_0 * np.exp(beta * (1/T_kelvin - 1/T_0))

# Strain Gauge (Linear): V_out = K * P * V_exc
# P is pressure (mmHg) mapped here linearly for visual comparison
P_mmHg = np.linspace(0, 300, 100) # Blood pressure range
K_sensor = 5e-6 # 5 uV/V/mmHg
V_exc = 10.0    # 10 V excitation
V_strain = K_sensor * P_mmHg * V_exc * 1000 # Convert to mV

ax2_1 = axs[0, 1]
ax2_2 = ax2_1.twiny() # Create a twin axis for the linear strain gauge

ax2_1.plot(T_celsius, R_thermistor / 1000, 'r-', linewidth=2, label='Thermistor $R(T)$')
ax2_1.set_xlabel('Temperature (°C) [Thermistor]', color='r')
ax2_1.set_ylabel('Resistance (kΩ)', color='r')
ax2_1.tick_params(axis='x', labelcolor='r')
ax2_1.tick_params(axis='y', labelcolor='r')

ax2_2.plot(P_mmHg, V_strain, 'b-', linewidth=2, label='Strain Gauge $V(P)$')
ax2_2.set_xlabel('Pressure (mmHg) [Strain Gauge]', color='b')
# Using right y-axis for voltage
ax2_2.spines['right'].set_color('b')

axs[0, 1].set_title('Linear vs. Nonlinear Transduction')
axs[0, 1].grid(True, alpha=0.5)

# ============================================================================
# PANEL 3: INSTRUMENTATION AMPLIFIER & CMRR
# ============================================================================
# V_d = V_1 - V_2 (Differential signal, e.g., 1 mV ECG)
# V_cm = (V_1 + V_2)/2 (Common-mode signal, e.g., 60Hz powerline)
# V_out = A_d*V_d + A_cm*V_cm
# CMRR_dB = 20 * log10(|A_d / A_cm|)

A_d = 1000.0 # Differential Gain (V/V)
CMRR_dB = 80.0 # 80 dB CMRR (standard monolithic InAmp like AD620)
A_cm = A_d / (10**(CMRR_dB / 20)) # Common-mode gain

# Simulate 60 Hz mains coupling to the body (100 mV amplitude)
f_mains = 60.0 # Hz
V_cm = 100e-3 * np.sin(2 * np.pi * f_mains * t) # 100 mV interference

# Output with finite CMRR
V_out_real = (A_d * V_bio) + (A_cm * V_cm)
# Ideal output (infinite CMRR)
V_out_ideal = A_d * V_bio

axs[1, 0].plot(t, V_out_real, 'r-', alpha=0.7, label=f'Real InAmp (CMRR={CMRR_dB}dB)')
axs[1, 0].plot(t, V_out_ideal, 'k-', linewidth=2, label='Ideal InAmp (CMRR=∞)')
axs[1, 0].set_title('InAmp: 60Hz Common-Mode Rejection')
axs[1, 0].set_xlabel('Time (s)')
axs[1, 0].set_ylabel('Output Voltage (V)')
axs[1, 0].legend()
axs[1, 0].grid(True)

# ============================================================================
# PANEL 4: JOHNSON (THERMAL) NOISE LIMITS
# Cross-link: Thermodynamics / Solid State Physics
# ============================================================================
# V_n,rms = sqrt(4 * k_B * T * R * delta_f)
# k_B: Boltzmann constant (J/K)
# T: Absolute temp (K)
# R: Source resistance (Ohms)
# delta_f: System bandwidth (Hz)

k_B = 1.38e-23 # J/K
T = 300.0      # K (approx 27 deg C)
delta_f = 500.0 # Hz (Typical EMG bandwidth)

R_array = np.logspace(3, 8, 100) # Electrode impedance from 1 kOhm to 100 MOhm
V_n_rms = np.sqrt(4 * k_B * T * R_array * delta_f)

axs[1, 1].loglog(R_array, V_n_rms * 1e6, 'm-', linewidth=2)
axs[1, 1].set_title(f'Thermal Noise vs. Electrode Impedance (Δf={delta_f}Hz)')
axs[1, 1].set_xlabel('Electrode Source Resistance $R$ (Ω)')
axs[1, 1].set_ylabel('RMS Noise Voltage $V_{n,rms}$ (μV)')
axs[1, 1].grid(True, which="both", ls="--", alpha=0.5)

# Add an annotation for a typical microelectrode limit
R_micro = 10e6 # 10 MOhms
V_micro = np.sqrt(4 * k_B * T * R_micro * delta_f) * 1e6
axs[1, 1].plot(R_micro, V_micro, 'ko')
axs[1, 1].annotate(f' Microelectrode\n ({V_micro:.1f} μV floor)', 
                   (R_micro, V_micro), xytext=(R_micro*0.1, V_micro*2),
                   arrowprops=dict(facecolor='black', shrink=0.05, width=1, headwidth=5))

plt.tight_layout()
plt.savefig("instrumentation_constraints.png", dpi=160, bbox_inches="tight")
# plt.show()  # Uncomment to render locally