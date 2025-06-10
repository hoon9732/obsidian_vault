```
% Define link lengths
a1 = 1; 
a2 = 2;

% Start and end points in Cartesian space
p_start = [3; 0];
p_end   = [1; 5];

% Total distance and time
L = norm(p_end - p_start);   % sqrt( (1-3)^2 + (5-0)^2 ) = sqrt(29)
T = L;  % speed = 1 => time = distance

% Discretize time
dt = 0.01;
t_vec = 0:dt:T;
N = length(t_vec);

% Preallocate arrays for joint angles
theta1_array = zeros(1,N);
theta2_array = zeros(1,N);

for i = 1:N
    t = t_vec(i);
    % Parametric interpolation in Cartesian space
    x_des = p_start(1) + (p_end(1)-p_start(1))*(t/T);
    y_des = p_start(2) + (p_end(2)-p_start(2))*(t/T);
    
    % --- Solve IK ---
    r2 = x_des^2 + y_des^2;
    D  = (r2 - a1^2 - a2^2)/(2*a1*a2);
    % Elbow-down solution for example:
    theta2_sol = acos(D);  % or -acos(D) for elbow-up
    
    % Use standard "two-arc-tan" formula:
    phi = atan2( a2*sin(theta2_sol), a1 + a2*cos(theta2_sol) );
    theta1_sol = atan2(y_des, x_des) - phi;
    
    % Store
    theta1_array(i) = theta1_sol;
    theta2_array(i) = theta2_sol;
end

% Approximate joint velocities via finite differences
theta1dot_array = diff(theta1_array)/dt;
theta2dot_array = diff(theta2_array)/dt;
t_vel = t_vec(1:end-1);

% Plot results
figure;
subplot(2,1,1);
plot(t_vec, theta1_array, 'b', t_vec, theta2_array, 'r');
xlabel('Time (s)'); ylabel('Joint angle (rad)');
legend('\theta_1','\theta_2');
title('Joint Angles vs Time');

subplot(2,1,2);
plot(t_vel, theta1dot_array, 'b', t_vel, theta2dot_array, 'r');
xlabel('Time (s)'); ylabel('Joint velocity (rad/s)');
legend('\dot{\theta}_1','\dot{\theta}_2');
title('Joint Velocities vs Time');

```
#MATLAB
