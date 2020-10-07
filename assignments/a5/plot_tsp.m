function plot_tsp()
    A = load('data/tsp.mat');
    X = A(:,1);
    Y = A(:,2);
    scatter(X, Y, 'filled');
end