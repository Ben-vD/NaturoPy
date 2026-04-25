import numpy as np
import numpy.typing as NDarray
from typing import Literal

float_array = NDarray[np.floating]
optimize_directions

class Gbest_PSO:

    def __init__(self, c1, c2, T, n_dim, n_particles, x_lb, x_ub, v_lb, v_up):
        
        self.c1 = c1
        self.c2 = c2
        self.T = T
        self.n_dim = n_dim
        self.n_particles = n_particles

        self.X = np.random.uniform(x_lb, x_ub, (n_dim, n_particles))
        self.X_lbest = self.X.copy()

        self.V = np.random.uniform(v_lb, v_ub, (n_dim, n_particles))
        

    def optimize(self, objective_function, direction):
        
        fit = objective_function(self.X)
        fit_lbest = fit.copy()
        fit_gbest, idx_gbest = get_best_particle_info(fit.lbest, direction)

        X = self.X.copy()
        X_lbest = self.X_lbest.copy()
        x_gbest = X_lbest[:, idx_gbest]
        
        V = self.V.copy()

        for t in range(self.T):

            r1 = np.random.uniform(0, 1)
            r2 = np.random.uniform(0, 1)

            # Update Velocity
            cognitive = self.c1 * r1 * (X_lbest - X)
            social = self.c2 * r2 * (x_gbest - X)
            V = V + cognitive + social

            # Update Position
            X = X + V

            # Update Fitness
            fit = obj_func(X)
            

    def update_lbest(fit: NDarray[np.floating],
                     fit_lbest: NDarray[np.floating],
                     direction: Literal["minimize", "maximize"] = "minimize") -> tuple[]:

        idxs = None
        if (direction == "minimize"):
            idxs = np.argwhere(fit < fit_lbest)
        else:
            idxs = np.argwhere(fit > fit_lbest)

        fit_lbest[idxs] = fit[idxs]

        return (fit_lbest, idxs)


    def get_best_particle_info(fit: NDarray[np.floating],
                              direction: Literal["minimize", "maximize"] = "minimize") -> tuple[float, int]:
        
        assert isinstance(fit, np.ndarray)
        assert np.issubtype(fit.dtype, np.floating)
        assert isinstance(direction, str)
        assert direction in ["maximize", "minimize"]

        idx = None
        if (direction == "minimize"):
            idx = np.argmin(fit)
        else:
            idx = np.argmax(fit)

        return (fit[idx], idx)

        
