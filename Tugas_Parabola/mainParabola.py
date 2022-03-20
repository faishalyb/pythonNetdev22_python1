import numpy as np
import matplotlib; matplotlib.use("TkAgg")  # untuk visualisasi animasi pada pycharm
import matplotlib.pyplot as plt
import matplotlib.animation as animation

gravitasi = 9.8

# MEMBUAT RUMUS GERAK PARABOLA PADA SUMBU X (HORIZONTAL)
def jarak_horizontal(v0,waktu,sudut):
    waktu_max = ground_t(v0, sudut)
    rad = np.radians(sudut)  # rad disini adalah ALFA
    perpindahan_arah = v0 * np.cos(rad)
    if waktu <= waktu_max:
        jarak = perpindahan_arah * waktu
    else:
        jarak = perpindahan_arah * waktu_max
    return jarak

# MEMBUAT RUMUS GERAK PRABOLA PADA SUMBU Y (VERTIKAL)
def jarak_vertikal(v0, waktu, sudut):
    rad = np.radians(sudut)             # rad disini adalah ALFA
    v_vert = v0 * np.sin(rad)
    perpindahan_arah = v_vert * waktu - (0.5 * gravitasi * waktu * waktu)
    if perpindahan_arah >= 0:
        return perpindahan_arah
    else:
        return 0

# MEMBUAT TITIK TERJAUH TEMBAKAN
def ground_t(v0, sudut):
    rad = np.radians(sudut)             # rad disini adalah ALFA
    v_vert = v0 * np.sin(rad)
    t = 2 * v_vert / gravitasi
    return t

# MEMBUAT DATA UNTUK SIMULASI GERAK PARABOLA