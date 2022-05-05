from deCasteljau import *
import matplotlib.pyplot as plt

def main():
    #points from a graph paper. Edges at the letter E.
    Ep = np.matrix("-3 5; -1 5; 3 5; 3 3; -1 3; -1 1; 1 1; 1 -1; -1 -1; -1 -3; 3 -3; 3 -5; -1 -5; -3 -5; -3 -3; -3 0; -3 3")
    Ep = Ep.tolist()

    E1 = interpolate_periodic(Ep, point_velocity(Ep)) #creating periodic interpolation points
    E2 = interpolate_periodic(Ep, point_velocity(Ep, 3))

    t = np.arange(0, len(E1), 0.01)

    E1_bezier = np.array([compositeBézier(E1, i) for i in t]) #creating qubic composite bezier curve
    E2_bezier = np.array([compositeBézier(E2, i) for i in t]) #creating qubic composite bezier curve with less curvature

    #plotting the letter:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
    ax1.plot(E1_bezier[:, 0], E1_bezier[:, 1], label = "sharpness = 1", color="black", linewidth=3)
    ax2.plot(E2_bezier[:, 0], E2_bezier[:, 1], label = "sharpness = 20", color="black", linewidth=3)
    ax1.legend()
    ax2.legend()
    plt.plot()

if __name__ == "__main__":
    main()