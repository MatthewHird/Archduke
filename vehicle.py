import math


class Vehicle:
    def __init__(self, position_x_init, position_y_init, psi_init, engine_power, coefficient_brake, constant_brake,
                 rho_drag, area_drag, constant_drag, mass_vehicle, axel_front_to_cm, axel_rear_to_cm, delta_steering,
                 constant_stiffness, inertia_moment_square):
        self.delta_time = 1
        self.position_x = position_x_init
        self.position_y = position_y_init
        self.psi_facing = psi_init
        self.engine_power = engine_power
        self.coefficient_brake = coefficient_brake
        self.constant_brake = constant_brake
        self.rho_drag = rho_drag
        self.area_drag = area_drag
        self.constant_drag = constant_drag
        self.mass_vehicle = mass_vehicle
        self.axel_front_to_cm = axel_front_to_cm
        self.axel_rear_to_cm = axel_rear_to_cm
        self.delta_axel = axel_front_to_cm + axel_rear_to_cm
        self.delta_steering = delta_steering
        self.radius_steering = self.delta_axel / math.sin(self.delta_steering)
        self.constant_stiffness = constant_stiffness
        self.inertia_moment_square = inertia_moment_square

        self.velocity_direction = 1
        self.force_long = 0
        self.force_engine = 0
        self.force_brake = 0
        self.force_drag = 0
        self.force_road_friction = 0
        self.acceleration = 0
        self.velocity_0 = 0
        self.velocity_1 = 0
        self.velocity_1_x = 0
        self.velocity_1_y = 0
        self.omega_steering = 0
        self.alpha_front = 0
        self.alpha_rear = 0
        self.velocity_lateral = 0
        self.velocity_long = 0
        self.force_lateral_front = 0
        self.force_lateral_rear = 0
        self.force_corner = 0
        self.radius_actual = 0
        self.torque_front = 0
        self.torque_rear = 0
        self.angular_acceleration = 0
        self.beta_vehicle = 0
        self.theta_vehicle = 0
        self.omega_actual = 0

    def update(self, engine_state, brake_state, turning_state):
        self.velocity_0 = self.velocity_1
        if self.velocity_0 >= 0:
            self.velocity_direction = 1
        elif self.velocity_0 < 0:
            self.velocity_direction = -1

        self.force_engine = self.engine_power * engine_state
        self.force_brake = brake_state * self.coefficient_brake * self.constant_brake
        self.force_drag = 0.5 * self.rho_drag * self.area_drag * self.constant_drag * self.velocity_0 ^ 2
        self.force_road_friction = 30 * self.force_drag / self.velocity_0
        self.force_long = self.force_engine - (self.force_brake + self.force_drag + self.force_road_friction
                                               ) * self.velocity_direction

        self.acceleration = self.force_long / self.mass_vehicle
        self.velocity_1 = self.velocity_0 + self.delta_time * self.acceleration
        self.velocity_1_x = self.velocity_1 * math.cos(self.theta_vehicle)
        self.velocity_1_y = self.velocity_1 * math.sin(self.theta_vehicle)
        self.position_x = self.position_x + self.delta_time * self.velocity_1_x
        self.position_y = self.position_y + self.delta_time * self.velocity_1_y
        if self.velocity_1 >= 0:
            self.velocity_direction = 1
        elif self.velocity_1 < 0:
            self.velocity_direction = -1

        if turning_state == 0:
            self.omega_steering = 0
        else:
            self.omega_steering = self.velocity_1 / self.radius_steering * turning_state

        self.beta_vehicle = self.theta_vehicle - self.psi_facing
        self.velocity_lateral = math.cos(self.beta_vehicle)
        self.velocity_long = math.sin(self.beta_vehicle)

        self.alpha_front = math.atan((self.velocity_lateral + self.omega_steering * self.axel_front_to_cm)
                                     / math.fabs(self.velocity_long)) - self.delta_steering * self.velocity_direction
        self.alpha_rear = math.atan((self.velocity_lateral - self.omega_steering * self.axel_rear_to_cm)
                                    / math.fabs(self.velocity_long))
        self.force_lateral_front = self.constant_stiffness * self.alpha_front
        self.force_lateral_rear = self.constant_stiffness * self.alpha_rear
        self.force_corner = math.cos(self.delta_steering) * self.force_lateral_front + self.force_lateral_rear
        self.radius_actual = self.mass_vehicle * self.velocity_1 ^ 2 / self.force_corner
        self.torque_front = math.cos(self.delta_steering) * self.force_lateral_front * self.axel_front_to_cm
        self.torque_rear = self.force_lateral_rear * self.axel_rear_to_cm

        self.angular_acceleration = (self.torque_front - self.torque_rear) / self.inertia_moment_square

        self.omega_actual = self.velocity_1 / self.radius_actual
        self.psi_facing = self.psi_facing + self.omega_actual * self.delta_time \
                          + self.angular_acceleration * self.delta_time ^ 2
