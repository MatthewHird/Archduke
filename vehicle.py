import math


class Vehicle:
    alpha_front
    velocity_lateral
    velocity_long
    axel_front_to_cm
    alpha_rear
    axel_rear_to_cm
    force_lateral_front
    force_lateral_rear
    constant_stiffness
    force_corner
    radius_actual
    torque_front
    torque_rear
    angular_acceleration
    inertia_moment_square

    def __init__(self, engine_power, coefficient_brake, constant_brake, rho_drag, area_drag, constant_drag,
                 mass_vehicle, axel_front_to_cm, axel_rear_to_cm, delta_steering, radius_steering):
        self.delta_time = 1
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
        self.radius_steering = radius_steering

        self.force_long = 0
        self.force_engine = 0
        self.force_brake = 0
        self.force_drag = 0
        self.force_road_friction = 0
        self.acceleration = 0
        self.velocity_0 = 0
        self.velocity_1 = 0
        self.position_0 = 0
        self.position_1 = 0
        self.omega_steering = 0

    def force(self, engine_state, brake_state):
        self.force_engine = self.engine_power * engine_state
        self.force_brake = brake_state * self.coefficient_brake * self.constant_brake
        self.force_drag = 0.5 * self.rho_drag * self.area_drag * self.constant_drag * self.velocity_0 ^ 2
        self.force_road_friction = 30 * self.force_drag / self.velocity_0
        self.force_long = self.force_engine + self.force_brake + self.force_drag + self.force_road_friction

    def avd(self):
        self.acceleration = self.force_long / self.mass_vehicle
        self.velocity_1 = self.velocity_0 + self.delta_time * self.acceleration
        self.position_1 = self.position_0 + self.delta_time * self.velocity_1

    def steering(self, turning_state):
        self.radius_steering = self.delta_axel / math.sin(self.delta_steering * turning_state)
        self.omega_steering = self.velocity_1 / self.radius_steering * turning_state
