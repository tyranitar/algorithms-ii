#include <iostream>
#include <fstream>
#include <vector>
#include <string>

double euclidian(double x1, double y1, double x2, double y2) {
	double delta_x = x1 - x2;
	double delta_y = y1 - y2;

	return sqrt(pow(delta_x, 2) + pow(delta_y, 2));
}

std::vector<int> get_powers_of_2(int n) {
	std::vector<int> v(n);

	for (int i = 0; i < n; i++) {
		v[i] = 1 << i;
	}

	return v;
}

double tsp(std::vector<std::vector<double>> g, int n) {
	std::vector<int> powers_of_2 = get_powers_of_2(n);

	int S = 3;
	int V = 1 << n;

	std::vector<std::vector<double>> A(V >> 1, std::vector<double>(n, INFINITY));

	V -= 1;
	A[0][0] = 0;

	while (S <= V) {
		for (int j = 1; j < n; j++) {
			double min_candidate = INFINITY;

			if (powers_of_2[j] & S) {
				for (int k = 0; k < n; k++) {
					if ((powers_of_2[k] & S) && (k != j)) {
						double k_without_j = A[(S ^ powers_of_2[j]) >> 1][k];

						if (k_without_j != INFINITY) {
							double candidate = k_without_j + g[k][j];

							if (candidate < min_candidate) {
								min_candidate = candidate;
							}
						}
					}
				}

				A[S >> 1][j] = min_candidate;
			}
		}

		S += 2;
	}

	double min_final_candidate = INFINITY;

	V >>= 1;

	for (int j = 1; j < n; j++) {
		double final_candidate = A[V][j] + g[j][0];

		if (final_candidate < min_final_candidate) {
			min_final_candidate = final_candidate;
		}
	}

	return min_final_candidate;
}

int main() {
	std::ifstream infile("data/tsp.txt");

	if (!infile.is_open()) {
		return 0;
	}

	int n;
	double x;
	double y;
	std::vector<std::vector<double>> nodes;

	infile >> n;

	while (infile >> x >> y) {
		std::vector<double> x_y(2);
		x_y[0] = x;
		x_y[1] = y;
		nodes.push_back(x_y);
	}

	infile.close();

	std::cout << "enter the n for which you would like tsp to run: ";
	std::cin >> n;

	std::vector<std::vector<double>> g(n, std::vector<double>(n, 0));

	for (int i = 0; i < n; i++) {
		for (int j = i + 1; j < n; j++) {
			double x1 = nodes[i][0];
			double y1 = nodes[i][1];
			double x2 = nodes[j][0];
			double y2 = nodes[j][1];

			double distance = euclidian(x1, y1, x2, y2);

			g[i][j] = distance;
			g[j][i] = distance;
		}
	}

	std::cout << tsp(g, n);

	return 0;
}