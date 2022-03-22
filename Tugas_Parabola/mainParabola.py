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
v0 = 80.88 # Kecepatan Awal
sudut = [15,30,45,60,75,90] # Dalam Derajat
t_grounds = [ground_t(v0, d) for d in sudut]  # Kalkulasi lama waktu diudara pada setiap sudut
t_ground = max(t_grounds)

time_interval = 0.1  # Membuat jarak antara titik ke titik yang digunakan pada kalkulasi waktu
t_steps = np.arange(0, t_ground + time_interval, time_interval)  # Membuat titik awal pada sumbu x dan y
hls = [[jarak_horizontal(v0, t, d) for t in t_steps] for d in sudut] # Membuat List pada posisi Horizontal pada tiap waktu untuk setiap sudut
vls = [[jarak_vertikal(v0, t, d) for t in t_steps] for d in sudut] # Membuat List pada posisi Vertikal pada tiap waktu untuk setiap sudut

h_max = max([max(l) for l in hls])  # Jarak Maksimum Horizontal
h_max = np.ceil(h_max)
v_max = max([max(l) for l in vls])  # Jarak Maksimum Vertikal
v_max = np.ceil(v_max)


# MEMBUAT ANIMASI GERAK PARABOLA
fig, ax = plt.subplots()

plt.gca().set_aspect("equal")  # Membuat scale yang sama persis pada sumbu x dan y
plt.xlabel('Jarak tempuh horizontal (m)')  # Membuat Title pada sumbu X
plt.ylabel('Ketinggian (m)')  # Membuat Title pada sumbu Y
plt.grid(True, which='both')  # Membuat Grid pada Tabel X dan Y

lines = [ax.plot([], [], label='{} derajat'.format(d))[0] for d in sudut]  # Membuat Plot pada setiap Sudut
ax.axis([0, h_max, 0, v_max])  # Set plot axis range
ax.legend()

def update(num, lines):  # FUNGSI UPDATE AGAR SETIAP PLOT BERJALAN DAPAT DIUPDATE
    for i in range(len(lines)):
        l = lines[i]
        l.set_data(hls[i][:num], vls[i][:num])
    tm = np.round(num * time_interval, 1)
    plt.title('Kecepatan Awal: {} m/s | Waktu simulasi: {} detik'.format(v0, tm))
    return lines

ani = animation.FuncAnimation(fig, update, frames=len(t_steps), fargs=[lines], interval=1000 * time_interval)
plt.show()